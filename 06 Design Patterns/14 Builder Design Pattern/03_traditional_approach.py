class HTTPRequest:

    def __init__(self, url, method, headers=None, body=None, auth=None, timeout=30):
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body
        self.auth = auth
        self.timeout = timeout
        
    def send_request(self):
        print('Making HTTPs Request')
        
request = HTTPRequest(
    "https://api.example.com/users",
    "POST",
    {"Content-Type": "application/json"},
    {"name": "Rudalph"},
    "my_access_token",
    30
)
request.send_request()