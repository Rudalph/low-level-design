class HTTPRequest:

    def __init__(self):
        self.url = None
        self.method = "GET"
        self.headers = {}
        self.body = None
        self.auth = None
        self.timeout = 30

    def show_request(self):

        print("URL:", self.url)
        print("Method:", self.method)
        print("Headers:", self.headers)
        print("Body:", self.body)
        print("Authentication:", self.auth)
        print("Timeout:", self.timeout)


request = HTTPRequest()
request.show_request()


class HTTPRequestBuilder:

    def __init__(self):
        self.request = HTTPRequest()

    def set_url(self, url):
        self.request.url = url
        return self

    def set_method(self, method):
        self.request.method = method
        return self

    def add_header(self, key, value):
        self.request.headers[key] = value
        return self

    def set_body(self, body):
        self.request.body = body
        return self

    def set_auth(self, token):
        self.request.auth = token
        return self

    def set_timeout(self, timeout):
        self.request.timeout = timeout
        return self

    def build(self):
        return self.request

builder = HTTPRequestBuilder()    
request = (
    builder
    .set_url("https://api.example.com/users")
    .set_method("POST")
    .add_header("Content-Type", "application/json")
    .add_header("Accept", "application/json")
    .set_body({
        "name": "Rudalph",
        "email": "rudalph@example.com"
    })
    .set_auth("my_access_token")
    .set_timeout(30)
    .build()
)
request.show_request()
