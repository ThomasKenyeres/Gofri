import importlib
import os
import runpy
import shutil
from configparser import ConfigParser

import pkg_resources
from clinodes.nodes import ArgNode, Switch

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

from gofri.developer.conf import LocalConfigIO
from gofri.lib.conf.config_reader import XMLConfigReader
import gofri.lib.globals as GLOB
from gofri.lib.conf.custom import init_custom_conf_file, load_default_config
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

def integrate_custom_modules(autoconf=False):
    root_path = GLOB.Config().ROOT_PATH
    if GLOB.Config().EXTENSIONS is not None:
        init_custom_conf_file(root_path)
        exts = GLOB.Config().EXTENSIONS
        for cmod in GLOB.Config().EXTENSIONS:
            ext = exts["extension"]
            name = ext["name"]
            if "autorun" in ext:
                if ext["autorun"] == "True":
                    runpy.run_module("{}.main".format(name), run_name="__main__", alter_sys=True)
            if autoconf:
                if "autoconf" in ext:
                    if ext["autoconf"] == "True":
                        load_default_config(root_path, name)

def run():
    conf = GLOB.Config()
    if conf.HOST == None:
        conf.HOST = "127.0.0.1"
    APP.run(port=int(conf.PORT), host=conf.HOST)

def start(root_path, modules, autoconf=False):
    banner = "GOFRI -- version: {}\n{}\n".format(
        pkg_resources.get_distribution("gofri").version,
        "#" * shutil.get_terminal_size().columns
    )
    print(banner)

    GLOB.init_conf(root_path)
    piphandler = PIPHandler()
    piphandler.package_names = GLOB.Config().DEPENDENCIES

    piphandler.install()
    print("All required dependencies are installed")

    CUSTOM_CONFIG = init_custom_config("custom-conf.ini")
    integrate_custom_modules(autoconf)

    importlib.import_module("modules", modules)

    run()


do_autoconf = False

def main(root_path, modules):

    class UpdaterSwitch(Switch):
        def run(self, *args):
            global do_autoconf
            do_autoconf = True

    class RootNode(ArgNode):
        def setup(self):
            self.expects_more = False
            self.switches = {
                "--enable-default": UpdaterSwitch,
                "-ed": UpdaterSwitch
            }

        def run(self, *args_remained):
            if len(args_remained) == 0:
                global do_autoconf
                start(root_path, modules, autoconf=do_autoconf)

    RootNode()