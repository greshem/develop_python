from paste import httpserver

def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    return ['Hello World\n']

httpserver.serve(application, host='0.0.0.0', port=8088)
