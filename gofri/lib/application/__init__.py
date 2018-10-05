import os

from gofri.lib.http.app import Application


class WSGI:
    GOFRI = "gofri"
    FLASK = "flask"

class ApplicationWrapper(object):
    def __init__(self, wsgi=WSGI.GOFRI):
        self.wsgi = wsgi
        if wsgi == WSGI.GOFRI:
            self.wsgi_application = Application(static_conf={
                "enable": True,
                "dir": "/static",
                "path": os.path.join(os.path.dirname(__file__), "static"),
            })
        elif wsgi == WSGI.FLASK:
            pass

    def start(self, host="0.0.0.0", port=8080):
        pass

    def stop(self):
        pass