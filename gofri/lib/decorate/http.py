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
        return ["POST"]

class HEAD(PostBasedRequestHandler):
    def _set_methods(self):
        return ["HEAD"]


class PUT(PostBasedRequestHandler):
    def _set_methods(self):
        return ["PUT"]


class DELETE(PostBasedRequestHandler):
    def _set_methods(self):
        return ["DELETE"]