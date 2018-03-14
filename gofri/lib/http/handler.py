class RequestHandler(object):
    def __init__(self, headers="", body="", json=""):
        self.path = None
        self.headers = [param.strip() for param in headers.split(";")]
        self.body = [param.strip() for param in body.split(";")]
        self.json = [param.strip() for param in json.split(";")]
