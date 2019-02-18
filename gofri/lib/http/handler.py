from gofri.lib.main import ApplicationWrapper


class RequestHandler(object):
    def __init__(self, path, request="", response_type="text/plain",
                 headers="", params="", cors=False):
        self.path = path
        self.headers = headers
        self.params= params
        self.request = request
        self.response_type = response_type
        self.cors = cors
        self.app_wrapper = ApplicationWrapper()

    def __call__(self, func):
        self.app_wrapper.http_app.set_url_endpoint(
            self.path, func, ["GET"],
            request_nm=self.request,
            params_nm=self.params,
            headers_nm=self.headers,
            response_type=self.response_type,
            cors=self.cors
        )
        return func

class PostBasedRequestHandler(RequestHandler):
    def __init__(self, path, request="", response_type="text/plain",
                 headers="", params="", body="", json="", json_obj=""):
        RequestHandler.__init__(self, path, request=request, response_type=response_type,
                                headers=headers, params=params)
        self.body = body
        self.json = json
        self.json_obj = json_obj
        self.__methods = self._set_methods()

    def __call__(self, func):
        return  self.app_wrapper.http_app.set_url_endpoint(
            self.path, func, self.__methods,
            request_nm=self.request,
            params_nm=self.params,
            headers_nm=self.headers,
            body_nm=self.body,
            json_nm=self.json,
            json=self.json_obj,
            response_type=self.response_type
        )

    def _set_methods(self):
        pass