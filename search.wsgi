#!/usr/bin/env python

from wsgiref.simple_server import make_server
import os
import sys
sys.path.append(os.path.dirname(__file__))

from app.httpdata import HttpData
from app.app import App


def application(environ, start_response):
    status = '200 OK'

    req = HttpData(environ)
    data = App.process(req.request(), req.body())
    output = req.response(data)
    response_headers = [('Content-type', 'text/plain'), ('Access-Control-Allow-Origin','*')]

    start_response(status, response_headers)
    return [bytes(output, encoding= 'utf-8')]


httpd = make_server('', 8000, application)
httpd.serve_forever()