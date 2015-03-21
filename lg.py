import urllib2
from time import sleep
while True:
    try:
        request = urllib2.Request("http://192.168.1.201:8080/roap/api/auth", headers={'content-type': 'application/atom+xml'}, data="<?xml version=\"1.0\" encoding=\"utf-8\"?><auth><type>AuthReq</type><value>347540</value></auth>")
        urllib2.urlopen(request).read()
        request = urllib2.Request("http://192.168.1.201:8080/roap/api/command", headers={'content-type': 'application/atom+xml'}, data="<?xml version=\"1.0\" encoding=\"utf-8\"?><command><name>HandleKeyInput</name><value>29</value></command>")
        urllib2.urlopen(request).read()
    except:
        None
    sleep(50)
