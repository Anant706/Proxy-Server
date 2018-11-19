# Proxy and Web Servers

It is a web proxy server that intelligently works with a web server to deliver the content customized for the data rate to the HTTP client.

### Installing

To install Python3.x, follow below steps:

```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
```

## Run the project

```
python3 server.py port datarate_low datarate_high

python3 measure.py port

python3 proxy.py serverip serverport measureip meaureport proxyport measurefile
```
## Limitations

* Project will handle request to .jpg/.jpeg image and .html files only.

## Built With

* [urllib](https://docs.python.org/3/library/urllib.request.html#) - Extensible library for opening URLs
* [http.server](https://docs.python.org/3/library/http.server.html) - HTTP servers creation

## Authors

* **Anant Kumar Yadav** - *Computer Science Graduate* - [University Of Houston](http://www.uh.edu/nsm/computer-science/)
* **PeopleSoft Id** - 1xxxxxxxxxxxx 
* **Email Id** - anantxxxxxxx@gmail.com

## Acknowledgments
**Special thanks to all**:
* Prof. Omprakash Gnawali
* Milad Heydariaan - TA
* Classmates
* Stackoverflow
* Python Official Site
