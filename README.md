testws
======

webservices for testing/debugging

Installation
------------
    pip install spyne

    pip install -e git+https://github.com/fatrix/testws.git

add heartbeat to settings.INSTALLED_APPS

    "heartbeat",

add an url to your urls.py

    url(r"^webservice/heartbeat/", 'heartbeat.views.heartbeat_service'),


Usage
-----
Get WSDL
--------
http://127.0.0.1:8000/webservice/heartbeat/service.wsdl

Test
----
curl -v -d "<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sah="sahli_net.heartbeat">
   <soapenv:Header/>
   <soapenv:Body>
      <sah:heartbeat>
         <!--Optional:-->
         <sah:f1>?</sah:f1>
      </sah:heartbeat>
   </soapenv:Body>
</soapenv:Envelope>" http://127.0.0.1:8000/webservice/heartbeat/service
