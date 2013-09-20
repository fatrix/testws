#!/usr/bin/env python
# encoding: utf8
#
import StringIO
import logging
from lxml import etree
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

logger = logging.getLogger("webservice")

@csrf_exempt
@require_http_methods(['POST'])
def dump_service(request):
    """
    This view can be used to debug a configuration on a reverse proxy oder
    xml firewall.
        - E.g. ?response_code=500 to receive a HTTP INTERNAL SERVER ERROR
        - Send an XML file to the view and it gets back to you
        - ?no_dump to omit the XML file in the response body
    """
    response = HttpResponse(mimetype="text/xml;charset=UTF-8")

    # specific response code is asked
    response_code = request.GET.get('response_code')
    if response_code:
        response.status_code = int(response_code)
        logger.debug("client asked for a response with %s" % response.status_code)
        return response

    # get data from request
    try:
        # if no file is posted, raises IndexError
        data = request.raw_post_data
    except Exception, e:
        data = None
        logger.error(e.message)
        response.status_code = 500
        response.write(e.message)

    # validate xml and return if no nodump query parameter specified
    try:
        s_data = StringIO.StringIO()
        for line in data:
            s_data.write(line.replace('encoding="utf-8"', ""))
        s_data.seek(0)
        root = etree.parse(s_data)
        logger.debug(etree.tostring(root))
        # check if nodump
        if request.META['QUERY_STRING'] == "nodump":
            logger.debug("client asked for a empty response body  %s" % response.status_code)
        else:
            for line in data:
                response.write(line)
    except Exception, e:
        logger.error(e.message)
        response.write(e.message)
        response.status_code = 500
    return response
