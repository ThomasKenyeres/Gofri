from gofri.lib.conf.config_reader import XMLConfigReader
from gofri.lib.util.collections import WrappedDictionary


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(WrappedDictionary, metaclass=Singleton):
    def __init__(self):
        super().__init__()

def init_conf(root_path):
    C = XMLConfigReader(root_path)
    conf = Config()
    conf.ROOT_PATH = root_path
    conf.CONF = C.get_conf_xml()["configuration"]
    conf.HOST = C.get_dict_config(conf.CONF, "hosting", "host")
    conf.PORT = C.get_dict_config(conf.CONF, "hosting", "port")
    conf.DATABASE_RDBMS = C.get_dict_config(conf.CONF, "database", "rdbms")
    conf.MYSQL_CONFIG = C.get_dict_config(conf.CONF, "database", "mysql-config")
    conf.DEPENDENCIES = C.get_dict_config(conf.CONF, "dependencies", "dependency")
    conf.CUSTOM_MODULES = C.get_dict_config(conf.CONF, "custom-modules", "module")

    if isinstance(conf.DEPENDENCIES, str):
        conf.DEPENDENCIES = [conf.DEPENDENCIES]

    if isinstance(conf.CUSTOM_MODULES, str):
        conf.CUSTOM_MODULES = [conf.CUSTOM_MODULES]