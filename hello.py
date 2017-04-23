def app(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    data = environ['QUERY_STRING']
    queries = [bytes(i + '\n', 'utf-8') for i in data.split('&')]
    return queries
