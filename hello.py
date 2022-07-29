def app(environ, start_response):
    body = '\n'.join(environ['QUERY_STRING'].split('&'))
    body1 = bytes(body+'\n', 'ascii')
    # body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(body1)))
    ])
    # print(body)
    # print(body1)
    return iter([body1])
