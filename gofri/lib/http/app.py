import os

import werkzeug.exceptions as E
from jinja2 import Environment, FileSystemLoader
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple
from werkzeug.wsgi import SharedDataMiddleware

from gofri.lib.http.control import HttpWrapper
from gofri.lib.http.cors import cors_is_valid
from gofri.lib.http.wrappers import Response, Request


class Application(object):
    endp_count = 0

    def __init__(self, jinja_template_path=os.path.join(os.path.dirname(__file__), 'templates'),
                 jinja_dir="templates",
                 static_conf={ "enable": False, "dir": "/static", "path": ""}):
        self.jinja_template_path = jinja_template_path
        self.jinja_dir = jinja_dir
        self.jinja_env = self._setup_jinja()
        self.urls = Map([])
        self.endpoints = {}
        self.methods = {}
        self.calldata = {}
        self.cors_endpoints = []
        self.wrapper = HttpWrapper()
        self._setup_wsgi(enable_static=True, static_dir=static_conf["dir"], static_path=static_conf["path"])

    def run(self, host="127.0.0.1", port=8080, use_reloader=False):
        run_simple(host, port, self, use_reloader=use_reloader)

    def _setup_jinja(self):
        env = Environment(
            loader=FileSystemLoader(self.jinja_template_path),
            autoescape=True
        )
        env.trim_blocks = True
        return env

    def _setup_wsgi(self, enable_static, static_dir, static_path):
        if enable_static:
            self.wsgi_app = SharedDataMiddleware(self.wsgi_app, {
                static_dir: static_path
            })

    def render_template(self, template_name, **kwargs):
        kwargs.update(globals())
        print(globals())
        return self.jinja_env.get_template(template_name).render(**kwargs)

    def set_url_endpoint(self, path, func, methods, request_nm="",
                         params_nm="", headers_nm="", body_nm="",
                         json_nm="", json="", response_type="", cors=False):

        endp_name = "endp{}".format(Application.endp_count)
        Application.endp_count += 1
        self.urls.add(Rule(path, endpoint=endp_name))

        param_names = [p.strip() for p in params_nm.split(";") if p.strip() != ""]
        header_names = [h.strip() for h in headers_nm.split(";") if h.strip() != ""]
        body_names = [b.strip() for b in body_nm.split(";") if b.strip() != ""]
        json_names = [j.strip() for j in json_nm.split(";") if j.strip() != ""]

        is_get = False

        func = self.wrapper.wrap_function(
            func, is_get,
            request_nm,
            param_names,
            header_names,
            body_names,
            json_names,
            json,
            response_type,
            cors
        )

        self.endpoints[endp_name] = func
        self.methods[endp_name] = methods

        if cors:
            self.cors_endpoints.append(endp_name)

    def render(self, name, **context):
        template = self.jinja_env.get_template(name)
        return Response(template.render(context), mimetype="text/html", content_type="text/html")

    def dispatch_request(self, request):
        adapter = self.urls.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            cors_enabled = endpoint in self.cors_endpoints
            if not request.method in self.methods[endpoint]:

                if not cors_is_valid(request, self.methods):
                    raise E.MethodNotAllowed()


            resp = self.endpoints[endpoint](request, *(), **values)

            if cors_enabled:
                origin_present = "Access-Control-Allow-Origin" in resp.headers
                headers_present = "Access-Control-Allow-Headers" in resp.headers
                if not origin_present:
                    resp.headers["Access-Control-Allow-Origin"] = "*"
                if not headers_present:
                    resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Accept"

            return resp
        except E.HTTPException as e:
            return Response(
                status=e.code,
                response=e.get_body(),
                mimetype="application/xml",
                content_type="application/xml"
            )

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)