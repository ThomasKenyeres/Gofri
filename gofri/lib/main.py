from flask import Flask
from flask_restful import Api

from gofri.lib.conf.config_reader import ConfigReader
from gofri.lib.pip.pip_handler import PIPHandler

ROOT = ""
ROOT_PATH = ""

C = ConfigReader(ROOT_PATH)

CONF = None
HOST = None
PORT = None
DATABASE_RDBMS = None
MYSQL_CONFIG = None
DEPENDENCIES = None


def init_config():
    global CONF, HOST, PORT, DATABASE_RDBMS, MYSQL_CONFIG, DEPENDENCIES

    CONF = C.get_conf_xml()["configuration"]
    HOST = C.get_dict_config(CONF, "hosting", "host")
    PORT = C.get_dict_config(CONF, "hosting", "port")
    DATABASE_RDBMS = C.get_dict_config(CONF, "database", "rdbms")
    MYSQL_CONFIG = C.get_dict_config(CONF, "database", "mysql-config")
    DEPENDENCIES = C.get_dict_config(CONF, "dependencies", "dependency")

class ASD:
    pass


APP = Flask(__name__)
API = Api(APP)


def run():
    global HOST
    if HOST == None:
        HOST = "127.0.0.1"
    APP.run(port=PORT, host=HOST)


def main(root_path):
    global C, ROOT_PATH
    C = ConfigReader(root_path)
    ROOT_PATH = root_path

    init_config()
    piphandler = PIPHandler()
    piphandler.package_names = DEPENDENCIES
    #print("Dependencies are loaded")
    piphandler.install()
    print("All required dependencies are installed")

    run()


if __name__ == '__main__':
    main()