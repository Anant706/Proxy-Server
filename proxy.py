from urllib import request
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os


class ProxyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        filename, ext = os.path.splitext(self.path)

        resource_name = os.path.split(self.path)[1]

        if ext == '.jpg' or ext == '.jpeg' or ext=='.html':
            if ext == '.jpg' or ext == '.jpeg':
                datarate = measureserver(self, measurement_file)
                file_server_response = fileserver(self, datarate, resource_name)
            
            elif ext == '.html':
                datarate = 0
                file_server_response = fileserver(self, datarate, resource_name)

            self.send_response(200)
            self.end_headers()
            text = file_server_response.read()
            self.wfile.write(text)
        else:   
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Error!! File not found".encode('utf-8'))
        


def fileserver(self, datarate, resource_name):
    # now make a call to file server with datarate in header
    headers = {}
    headers['datarate'] = datarate
    url = "http://" + serverip + ":" + serverport + "/" + resource_name
    req = request.Request(url, headers=headers)
    return request.urlopen(req)


def measureserver(self, measurement_file):
    starttime = int(round(time.time()))
    # measure server request sent for data size calculation
    url = "http://" + measureip + ":" + measureport + "/" + measurement_file
    measure_server_response = request.urlopen(url)
    endtime = int(round(time.time()))
    # total time in second
    totaltime = endtime - starttime 
    headers = measure_server_response.info()
    # size of data in KB
    datasize = int(int(headers['Content-Length'])/1024)
    datarate = int(datasize/totaltime)
    return datarate

# init method to start


def run(server_class=HTTPServer, handler_class=ProxyServer, proxyport=20362):
    server_address = ('', proxyport)
    httpd = server_class(server_address, handler_class)
    print('Server running at port:', proxyport)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        httpd.server_close()


if __name__ == "__main__":
    from sys import argv

if len(argv) == 7:
    serverip = argv[1]
    serverport = argv[2]
    measureip = argv[3]
    measureport = (argv[4])
    measurement_file = (argv[6])
    run(proxyport=int(argv[5]))
else:
    print ('Cannot start server as all 7 required parameters are not provided.')
    #run()
