#!/usr/bin/env python

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    parametrs = environ.get('QUERY_STRING', '')
#    parametrs.split('&')
    s = "\n"
    resp = s.join(parametrs.split("&")) + "\n"

    
    return [resp]