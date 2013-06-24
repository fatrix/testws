testws
======

webservices for testing/debugging

Installation
------------
    pip install -e git+https://github.com/fatrix/testws.git#egg=testws

add heartbeat or dump to settings.INSTALLED_APPS

    "heartbeat",
    "dump",

add url's to your urls.py

    url(r"^webservice/heartbeat/", 'heartbeat.views.heartbeat_service'),
    url(r"^webservice/dump/", 'dump.views.dump_service'),


Usage
-----
Get WSDL
--------
http://127.0.0.1:8000/webservice/heartbeat/service.wsdl

Test heartbeat
--------------
curl -v -d '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sah="sahli_net.heartbeat">
   <soapenv:Header/>
   <soapenv:Body>
      <sah:heartbeat>
         </sah:heartbeat>
   </soapenv:Body></soapenv:Envelope>' http://127.0.0.1:8000/webservice/heartbeat/
