import os

from gofri.lib.http.app import Application


class HttpDrivers:
    GOFRI = "gofri"
    FLASK = "flask"

class DataDrivers:
    SQLALCHEMY = "sqlalchemy"
    PONY = "pony"

class ApplicationWrapper(object):
    def __init__(self, http_driver_for=HttpDrivers.GOFRI, data_driver_for=None):
        self.wsgi = http_driver_for
        self.__set_http_driver(http_driver_for)
        self.__set_data_driver(data_driver_for)

    def __set_http_driver(self, driver_for):
        if driver_for == HttpDrivers.GOFRI:
            self.wsgi_application = Application(static_conf={
                "enable": True,
                "dir": "/static",
                "path": os.path.join(os.path.dirname(__file__), "static"),
            })
        elif driver_for == HttpDrivers.FLASK:
            pass

    def __set_data_driver(self, driver_for):
        if driver_for is not None:
            pass

    def start(self, host="0.0.0.0", port=8080):
        pass

    def stop(self):
        pass