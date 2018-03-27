import os
import runpy
import shutil
from configparser import ConfigParser

import pkg_resources

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

from gofri.lib.conf.config_reader import XMLConfigReader
import gofri.lib.globals as GLOB
from gofri.lib.http.app import Application
from gofri.lib.pip.pip_handler import PIPHandler

def init_custom_config(filename):
    fullpath = "{}/{}".format(GLOB.Config().ROOT_PATH, filename)
    conf = ConfigParser()
    conf.read(fullpath)
    return conf

CUSTOM_CONFIG = {}


APP = Application(static_conf={
    "enable": True,
    "dir": "/static",
    "path": os.path.join(os.path.dirname(__file__), "static")
})

Base = declarative_base()

def integrate_custom_modules():
    #TODO: Check more cases
    if GLOB.Config().CUSTOM_MODULES is not None:
        for cmod in GLOB.Config().CUSTOM_MODULES:
            if isinstance(cmod, str):
                runpy.run_module("{}.main".format(cmod), run_name="__main__", alter_sys=True)

def run():
    conf = GLOB.Config()
    if conf.HOST == None:
        conf.HOST = "127.0.0.1"
    APP.run(port=int(conf.PORT), host=conf.HOST)


def main(root_path, modules):
    banner = "GOFRI -- version: {}\n{}\n".format(
        pkg_resources.get_distribution("gofri").version,
        "#"*shutil.get_terminal_size().columns
    )
    print(banner)

    GLOB.init_conf(root_path)
    piphandler = PIPHandler()
    piphandler.package_names = GLOB.Config().DEPENDENCIES

    piphandler.install()
    print("All required dependencies are installed")

    CUSTOM_CONFIG = init_custom_config("custom-conf.ini")
    integrate_custom_modules()

    run()