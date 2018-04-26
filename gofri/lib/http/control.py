from inspect import signature

from werkzeug.wrappers import Response as Resp

from gofri.lib.http.tools import order_filters, run_filters
from gofri.lib.http.wrappers import Response


def try_add_args(kw, f_signature, names, req, req_attr):
    spl_names = [n.strip() for n in names.split()]
    print(spl_names)
    for arg in spl_names:
        if arg in  f_signature:
            if not arg in kw:
                kw[arg] = req.__getattr__(req_attr)
    return kw

class HttpWrapper:
    def __init__(self):
        pass

    def wrap_function(self, func, is_get, request_name, param_names,
                      header_names, body_pnames, json_names, json, response_type):
        def wrapper_func(*args, **kwargs):
            request = args[0]

            order_filters()
            result = run_filters(request, Response())

            request = result["request"]
            _response = result["response"]
            _response.content_type = response_type

            args = tuple(kwargs.values())

            kwargs = {}

            is_get = request.method == "GET"
            f_signature = signature(func).parameters.keys()

            if request_name is not "":
                kwargs[request_name] = request

            if json is not "":
                kwargs[json] = request.json

            if not is_get:

                #BODY
                for name in body_pnames:
                    if name in f_signature:
                        kwargs[name] = request.form.get(name)
                    else:
                        raise Exception("asd")

                #JSON
                for name in json_names:
                    if name in f_signature:
                        kwargs[name] = request.json.get(name)
                    else:
                        raise Exception("asd")

            #HEADERS
            for name in header_names:
                if name in f_signature:
                    kwargs[name] = request.headers.get(name)
                else:
                    raise Exception("asd")

            #PARAMS
            for name in param_names:
                if name in f_signature:
                    kwargs[name] = request.args.get(name)
                else:
                    raise Exception("asd")

            resp_body = func(*args, **kwargs)

            if isinstance(resp_body, (Response, Resp)):
                return resp_body

            response = Response(
                response=resp_body,
                status=_response.status,
                headers=_response.headers,
                mimetype=_response.mimetype,
                content_type=_response.content_type
            )
            return response

        return wrapper_func

