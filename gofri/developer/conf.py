import configparser

from gofri.lib.globals import Config


class LocalConfigIO(object):
    def __init__(self, filename="custom-conf.ini"):
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