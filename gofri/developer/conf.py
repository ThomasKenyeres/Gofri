import configparser

from gofri.lib.globals import Config

class SectionWrapper:
    def __init__(self, name, confdict):
        self.name = name
        self.confdict = confdict

class LocalConfigIO(object):
    def __init__(self, filename="local.ini"):
        self.__local_conf_path = "{}/{}".format(Config().ROOT_PATH, filename)
        self.__config = configparser.ConfigParser()
        self.update()

    def update(self):
        self.__config.read(self.__local_conf_path)

    def __getitem__(self, item):
        return self.__config[item]

    def __setitem__(self, key, value):
        self.__config[key] = value

    def commit(self):
        with open(self.__local_conf_path, "w") as conf_file:
            self.__config.write(conf_file)

    def config(self):
        return self.__config.sections()

    def add(self, sectionw):
        self.__config[sectionw.name] = sectionw

    def add_raw(self, string):
        with open(self.__local_conf_path, "a") as conf_file:
            conf_file.write(string)

    def merge(self, source, to_file=None):
        #if Config().EXT_CONF_ENABLE_CIO:
        if to_file is None:
            to_file = "{}/{}".format(Config().ROOT_PATH, "local.ini")
        if True:
            with open(self.__local_conf_path, "a") as targetf:
                content = ""
                with open(self.__local_conf_path, "r") as sourcef:
                    content = sourcef.read()
                targetf.write(content)
        #if Config().EXT_CONF_ENABLE_CIO:
            #with open(self.__local_conf_path, )