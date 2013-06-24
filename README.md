Testws
======

Sometimes it is very helpful to have a very simple webservice running for testing and
debugging purposes.

 - heartbeat:  SOAP Webservice
 - dump:  XML Webservice

Installation
------------
    pip install -e git+https://github.com/fatrix/testws.git#egg=testws

add heartbeat or dump to settings.INSTALLED_APPS

    "heartbeat",
    "dump",

add url's to your urls.py

    url(r"^webservice/heartbeat/", 'heartbeat.views.heartbeat_service'),
    url(r"^webservice/dump/", 'dump.views.dump_service'),


Test heartbeat
--------------
The heartbeat webservice is a SOAP webservice created with spyne

    curl http://127.0.0.1:8000/webservice/heartbeat/service.wsdl

Call the service

    curl -v -d '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sah="sahli_net.heartbeat">
       <soapenv:Header/>
       <soapenv:Body>
          <sah:heartbeat>
             </sah:heartbeat>
       </soapenv:Body></soapenv:Envelope>' http://127.0.0.1:8000/webservice/heartbeat/

Test dump
--------------
Get back the POSTed XML file (must be valid).

    curl -v -d '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sah="sahli_net.heartbeat">
       <soapenv:Header/>
       <soapenv:Body>
          <sah:heartbeat>
             </sah:heartbeat>
       </soapenv:Body></soapenv:Envelope>' http://127.0.0.1:8000/webservice/dump/

Ask the webservice for a specific status code (e.g. ?response_code=500)

     curl -v -d '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sah="sahli_net.heartbeat">
       <soapenv:Header/>
       <soapenv:Body>
          <sah:heartbeat>
             </sah:heartbeat>
       </soapenv:Body></soapenv:Envelope>' http://127.0.0.1:8000/webservice/dump/?response_code=500

Don't dump back the payload

     curl -v -d '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sah="sahli_net.heartbeat">
       <soapenv:Header/>
       <soapenv:Body>
          <sah:heartbeat>
             </sah:heartbeat>
       </soapenv:Body></soapenv:Envelope>' http://127.0.0.1:8000/webservice/dump/?nodump