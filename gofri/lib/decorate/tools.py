from inspect import signature


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
    else:
        dict_obj = obj.__dict__
        for key in dict_obj:
            dict_obj[key] = force_jsonizable(dict_obj[key])
        return dict_obj