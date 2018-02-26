from inspect import signature


def generate_arg_tuple(function, path_arg_tuple, request_args):
    selected = []
    f_signature = tuple(str(val) for val in signature(function).parameters.values())
    f_signature_end = f_signature[-len(request_args)::] if len(f_signature) > len(path_arg_tuple) else tuple()
    for arg in request_args:
        if arg in f_signature:
            selected.append(request_args[arg])
    return path_arg_tuple + tuple(selected)