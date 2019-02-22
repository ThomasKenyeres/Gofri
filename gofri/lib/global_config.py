import os

from gofri.lib.conf.config_file_analyzer import ConfigFileAnalyzer


def _getc(key):
    if key.startswith("GOFRI_"):
        return os.environ[key]
    else:
        return os.environ["GOFRI_{}".format(key)]

def _setc(key, value):
    if key.startswith("GOFRI_"):
        os.environ[key] = value
    else:
        os.environ["GOFRI_{}".format(key)] = value

def _getboolc(key):
    return bool(_getc(key))

def force_non_empty_list(obj):
    if obj is not None:
        if isinstance(obj, list):
            return obj
        else:
            return [obj]

def force_dict(obj):
    if isinstance(obj, dict):
        return obj
    else:
        return [obj]

_root_path = _getc("GOFRI_ROOT_PATH")
C = ConfigFileAnalyzer(_root_path)
_conf = C.read()

class Configuration():
    ROOT_PATH = _root_path
    CONF = _conf
    HOST = C.get_config("hosting", "host")
    PORT = C.get_config("hosting", "port")
    DATABASE_RDBMS = C.get_config("database", "rdbms")
    MYSQL_CONFIG = C.get_config("database", "mysql-config")
    EXT_CONF_ENABLE_AUTORUN = C.get_config("extension-conf", "enable-autorun") == "True"
    EXT_CONF_ENABLE_CIO = C.get_config("extension-conf", "enable-auto-config") == "True"

    DEPENDENCIES = force_non_empty_list(C.get_config("dependencies", "dependency"))
    EXTENSIONS = force_non_empty_list(C.get_config("extensions"))

    AUTO_INSTALL = False

    @staticmethod
    def get(key):
        return _getc(key)

    @staticmethod
    def set(key, value):
        _setc(key, value)

    @staticmethod
    def getbool(key):
        return _getboolc(key)