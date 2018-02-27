from inspect import signature


def generate_arg_tuple(function, path_arg_tuple, request_args):
    selected = []
    f_signature = tuple(str(val) for val in signature(function).parameters.values())
    for arg in request_args:
        if arg in f_signature:
            selected.append(request_args[arg])
    return path_arg_tuple + tuple(selected)