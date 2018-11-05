#!/usr/bin/env python

from wsgiref.simple_server import make_server
import os, sys, traceback, getpass
sys.path.append(os.path.dirname(__file__))


def application(environ, start_response):
    status = '200 OK'

    for key in ['DELUGE_ADDRESS', 'DELUGE_PORT', 'DELUGE_USER', 'DELUGE_PASS']:
        os.environ[key] = environ.get(key, '')

    try:
        from app.app import App
        body_size = int(environ.get('CONTENT_LENGTH', 0))
        content = environ['wsgi.input'].read(body_size)
        http_app = App(environ['REQUEST_METHOD'], content)
        output = http_app.process()
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