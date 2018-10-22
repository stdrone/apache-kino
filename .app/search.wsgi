def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!\n' + environ['SCRIPT_NAME'] + '\nTEST'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [bytes(output, encoding= 'utf-8')]