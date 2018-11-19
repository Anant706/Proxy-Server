#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import sys

HTTP_PORT_DEFAULT = 20360


class FileServer(BaseHTTPRequestHandler):

    # file server to process the proxy request based on datarate and send back image in response
    def do_GET(self):

        # extract datarate from header
        datarate = int(self.headers.get('datarate'))

        # spliting resource url into their name and extension
        name, ext = os.path.splitext(self.path)

        # depending on the extension type, prcoess the client request
        if ext == '.jpg' or ext == '.jpeg':

            largeimage = name + '_' + 'large' + ext
            mediumimage = name + '_' + 'medium' + ext
            smallimage = name + '_' + 'small' + ext

            self.send_response(200)
            self.send_header('Content-type', 'text/x-binary')
            self.end_headers()

            if datarate <= datarate_low:
                with open('./' + smallimage, 'rb') as f:
                    self.wfile.write(f.read())
            elif datarate_low < datarate <= datarate_high:
                with open('./' + mediumimage, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                with open('./' + largeimage, 'rb') as f:
                    self.wfile.write(f.read())

        # respond client with customised html file
        elif ext == '.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            file = open('.' + self.path, 'r')
            response_text = file.read()
            file.close()

            response_text = response_text.replace(
                "<body>", "<body>Ya you are right place")
            self.wfile.write(response_text.encode('utf-8'))


# initialize to start
try:
    if len(sys.argv) == 4:
        http_port = int(sys.argv[1])
        datarate_low = int(sys.argv[2])
        datarate_high = int(sys.argv[3])
    else:
        http_port = HTTP_PORT_DEFAULT
    # Create HTTP server with customized class
    server = HTTPServer(('', http_port), FileServer)
    print('Started httpserver on port', http_port)

    # Wait forever for incoming HTTP requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
