#!/usr/bin/env python
# encoding: utf8

from django.views.decorators.csrf import csrf_exempt

from spyne.server.django import DjangoApplication
from spyne.model.primitive import Unicode, Integer, String
from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.decorator import rpc

class HeartbeatService(ServiceBase):
    @rpc(Unicode, Integer, _returns=String)
    def heartbeat(ctx, f1):
        return "OK"

app = Application([HeartbeatService],
    'sahli_net.heartbeat',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

heartbeat_service = csrf_exempt(DjangoApplication(app))
