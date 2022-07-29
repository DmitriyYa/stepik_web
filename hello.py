def app(environ, start_response):
        body = bytes('\n'.join('q=1&p=3&x=3&d=5&g=7'.split('&')), 'ascii')
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(body)))
        ])
        return iter([body])
