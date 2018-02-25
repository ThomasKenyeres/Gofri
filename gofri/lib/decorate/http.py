from flask_restful import Resource
from gofri.lib.main import API


class GET():
    def __init__(self, path=""):
        self.path = path

    def __call__(self, function):
        resource = type("{}_Resource".format(function.__name__), (Resource,), {})
        def get(s, *args):
            return function()
        resource.get = get
        API.add_resource(resource, self.path)
        print(API.resources)