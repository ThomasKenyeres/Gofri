import configparser

from gofri.lib.globals import Config

class SectionWrapper:
    def __init__(self, name, confdict):
        self.name = name
        self.confdict = confdict

class LocalConfigIO(object):
    def __init__(self, filename="local.ini", fullpath=None):
        if fullpath is not None:
            self.__local_conf_path = fullpath
        else:
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

    def merge(self, source_file):
        dio = LocalConfigIO(fullpath=source_file)
        for section in dio.config():
            self[section] = dio[section]
        self.commit()