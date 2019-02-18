import importlib
import os
import runpy
import shutil
from configparser import ConfigParser

import pkg_resources
import sys
from clinodes.nodes import ArgNode, Switch

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

from gofri.lib.http.app import Application
from gofri.lib.pip.pip_handler import PIPHandler

try:
    from gofri.lib.global_config import Configuration
    from gofri.lib.conf.local import init_local_conf_file, load_default_config

    os.environ["GOFRI_HAS_ROOT"] = "True"
except KeyError:
    print("No root package detected! Running in standalone mode")
    os.environ["GOFRI_HAS_ROOT"] = "False"




class ApplicationWrapper:
    def __init__(self):
        self.extension_config = {}
        self.http_app = Application(static_conf={
            "enable": True,
            "dir": "/static",
            "path": os.path.join(os.path.dirname(__file__), "static"),
        })
        self.sql_alchemy_declarative_base = declarative_base()
        self.use_reloader = False

    def init_extension_config(self, filename):
        fullpath = "{}/{}".format(Configuration.ROOT_PATH, filename)
        conf = ConfigParser()
        conf.read(fullpath)
        return conf

    EXTENSION_CONFIG = {}


    Base = declarative_base()


    def integrate_extensions(self, autoconf=False):
        root_path = Configuration.ROOT_PATH
        if Configuration.EXTENSIONS is not None:
            init_local_conf_file(root_path)
            exts = Configuration.EXTENSIONS
            for cmod in Configuration.EXTENSIONS:
                ext = exts["extension"]
                name = ext["name"]
                if "autorun" in ext:
                    if ext["autorun"] == "True":
                        runpy.run_module("{}.main".format(name), run_name="__main__", alter_sys=True)
                if autoconf:
                    if "autoconf" in ext:
                        if ext["autoconf"] == "True":
                            load_default_config(root_path, name)


    USE_RELOADER = False


    def run(self):
        conf = Configuration
        if conf.HOST == None:
            conf.HOST = "127.0.0.1"
        self.http_app.run(port=int(conf.PORT), host=conf.HOST, use_reloader=ApplicationWrapper.USE_RELOADER)


    def start(self, root_path, modules, autoconf=False, auto_install=False, ):
        piphandler = PIPHandler()
        piphandler.packages = Configuration.DEPENDENCIES

        if auto_install:
            piphandler.install()

        print("All required dependencies are installed")

        CUSTOM_CONFIG = self.init_extension_config("custom-conf.ini")
        self.integrate_extensions(autoconf)

        importlib.import_module("modules", modules)

        self.run()


    def main(self, root_path, modules):
        Configuration.AUTO_INSTALL = False
        do_autoconf = False
        START = self.start

        class ReloaderSwitch(Switch):
            def run(self, *args):
                global USE_RELOADER
                USE_RELOADER = True

        class InstallerSwitch(Switch):
            def setup(self):
                self.expects_more = False

            def run(self, *args):
                Configuration.AUTO_INSTALL = True

        class UpdaterSwitch(Switch):
            def setup(self):
                self.expects_more = False

            def run(self, *args):
                do_autoconf = True

        class RootNode(ArgNode):
            def setup(self):
                self.expects_more = False
                self.switches = {
                    "--enable-default": UpdaterSwitch,
                    "-ed": UpdaterSwitch,
                    "--install": InstallerSwitch,
                    "--use-reloader": ReloaderSwitch
                }

            def run(self, *args_remained):
                do_auto_install = Configuration.AUTO_INSTALL
                START(root_path, modules, autoconf=do_autoconf, auto_install=do_auto_install)

        RootNode()
