import json
from collections import OrderedDict
from inspect import signature


def response_with(jsonizable):
    if isinstance(jsonizable, (int, str, float, bool, bytes)):
        return jsonizable
    else:
        return json.dumps(jsonizable)


def order_filters():
    global FILTERS
    d = {}
    rest = []
    for f_obj in FILTERS:
        if f_obj.order in d:
            rest.append(f_obj)
        else:
            d[f_obj.order] = f_obj
    FILTERS = list(OrderedDict(d).values()) + rest


def run_filters(request, response):
    _request = request
    _response = response
    for f_obj in FILTERS:
        if not f_obj.filter_all:
            if request.path in f_obj.urls:
                result = f_obj.filter(_request, _response)
                _request = result["request"]
                _response = result["response"]
        else:
            result = f_obj.filter(_request, _response)
            _request = result["request"]
            _response = result["response"]
    return {"request": request, "response": response}


def generate_arg_tuple(function, path_arg_tuple, request_args):
    selected = []
    f_signature = tuple(str(val) for val in signature(function).parameters.values())
    for arg in request_args:
        if arg in f_signature:
            selected.append(request_args[arg])
    return path_arg_tuple + tuple(selected)


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
    elif isinstance(obj, tuple):
        return list(obj)
    elif obj is not None:
        dict_obj = obj.__dict__
        for key in dict_obj:
            dict_obj[key] = force_jsonizable(dict_obj[key])
        return dict_obj
