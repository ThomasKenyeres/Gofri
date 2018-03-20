import json

from werkzeug.wrappers import Request as Req, Response as Resp

from gofri.lib.decorate.tools import response_with, force_jsonizable


class Wrapper(object):
    def __getattr__(self, attr_name):
        attr = self.cls.__getattribute__(attr_name)
        if callable(attr):
            def wrap(*args, **kwargs):
                result = attr(*args, **kwargs)
                return result
            return wrap
        else:
            return attr

class Request(Wrapper):
    def __init__(self, environ, populate_request=True, shallow=False):
        Wrapper.__init__(self)
        self.cls = Req(environ, populate_request=populate_request, shallow=shallow)

    @property
    def json(self):
        decoded = self.cls.data.decode()
        try:
            return json.loads(decoded)
        except Exception:
            return {}


class Response(Wrapper):
    def __init__(self, response=None, status=None, headers=None,
                 mimetype=None, content_type=None, direct_passthrough=False):
        Wrapper.__init__(self)
        self.cls = Resp(response=self.__optimize(response), status=status, headers=headers,
                 mimetype=mimetype, content_type=content_type, direct_passthrough=direct_passthrough)

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)

    def __optimize(self, resp):
        return response_with(force_jsonizable(resp))
