import os

from gofri.developer.conf import LocalConfigIO
from gofri.lib.globals import Config


def init_custom_conf_file(root_path):
    if not os.path.exists(root_path + "/local.ini"):
        with open(root_path + "/local.ini", "w") as cfile:
            cfile.close()

def load_default_config(root_path, module_name):
    path = "{}/{}".format(root_path, "local.ini")

    module = __import__("{}.config".format(module_name))
    default_cpath = module.config.get_config_path()

    io = LocalConfigIO()
    io.merge(default_cpath)