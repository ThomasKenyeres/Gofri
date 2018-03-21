from gofri.lib.http.const import RequestMethod

from gofri.lib.http.filter import FILTERS
from gofri.lib.http.filter import Filter
from gofri.lib.http.handler import RequestHandler, PostBasedRequestHandler


class GofriFilter:
    def __init__(self, urls=[], filter_all=False, order=0):
        self.urls = urls
        self.filter_all = filter_all
        self.order = order

    def __call__(self, cls):
        if not Filter in cls.__bases__:
            cls._continue = Filter._continue
        filter_obj = cls()
        filter_obj.urls = self.urls
        filter_obj.filter_all = self.filter_all
        filter_obj.order = self.order
        FILTERS.append(filter_obj)

class GET(RequestHandler):
    pass


class POST(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.POST]

class HEAD(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.POST]


class PUT(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.PUT]


class DELETE(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.DELETE]


class PATCH(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.PATCH]

class COPY(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.COPY]

class OPTIONS(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.OPTIONS]

class LINK(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.LINK]

class UNLINK(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.UNLINK]

class PURGE(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.PURGE]

class LOCK(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.LOCK]

class UNLOCK(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.UNLOCK]

class PROPFIND(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.PROPFIND]

class VIEW(PostBasedRequestHandler):
    def _set_methods(self):
        return [RequestMethod.VIEW]
