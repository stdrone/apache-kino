#!/usr/bin/env python

from wsgiref.simple_server import make_server
import os, sys, traceback, getpass
sys.path.append(os.path.dirname(__file__))


def application(environ, start_response):
    status = '200 OK'

    try:
        from app.httpdata import HttpData
        from app.app import App
        req = HttpData(environ)
        data = App.process(req)
        output = req.response(data)
    except Exception:
        status = '500 ERROR'
        (t, v, tb) = sys.exc_info()
        output = ''.join(traceback.format_exception(t, v, tb)) + getpass.getuser() + sys.version
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', 'OPTIONS,POST,PUT,DELETE'),
    ]


    start_response(status, response_headers)
    return [bytes(output, encoding= 'utf-8')]


__debug = os.environ.get('DEBUG')
if __debug is not None:
    httpd = make_server('', 8000, application)
    httpd.serve_forever()