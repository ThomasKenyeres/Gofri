import json

from flask import request
from flask_restful import Resource

from gofri.lib.decorate.tools import generate_arg_tuple
from gofri.lib.main import API

def force_jsonizable(obj):
    if isinstance(obj, (int, float, bytes, bool, str)):
        return obj
    elif isinstance(obj, (dict)):
        for key in obj:
            obj[key] = force_jsonizable(obj[key])
        return obj
    elif isinstance(obj, (list)):
        for i in range(len(obj)):
            obj[i] = force_jsonizable(obj[i])
        return obj
    else:
        dict_obj = obj.__dict__
        for key in dict_obj:
            dict_obj[key] = force_jsonizable(dict_obj[key])
        return dict_obj

class GET:
    resource_count = 0

    def __init__(self, path):
        self.path = path

    def __call__(self, function):
        GET.resource_count += 1
        resource_class = type("Resource{}".format(GET.resource_count), (Resource,), {})
        def get(s, *args, **kwargs):
            path_arg_tuple = tuple(kwargs[arg] for arg in kwargs)
            result = function(*generate_arg_tuple(function, path_arg_tuple, request.args))
            return force_jsonizable(result)
        resource_class.get = get

        API.add_resource(resource_class, self.path)
