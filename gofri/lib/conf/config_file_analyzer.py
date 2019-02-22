import os

from gofri.lib.conf.config_reader import XMLConfigReader
from gofri.lib.conf.json_config_reader import JSONConfigReader


class ConfigFileAnalyzer:
    def __init__(self, root_path):
        self.root_path = root_path
        self.conf_xml_path = self.root_path + "/conf.xml"
        self.conf_json_path = self.root_path + "/conf.json"
        self.conf_py_path = self.root_path + "/conf.py"

        self.xml_config_reader = XMLConfigReader(root_path)
        self.json_config_reader = JSONConfigReader(root_path)

    def read(self):
        if os.path.isfile(self.conf_py_path):
            return self._read_python()
        elif os.path.isfile(self.conf_json_path):
            return self._read_json()
        elif os.path.isfile(self.conf_xml_path):
            return self._read_xml()

    def _read_python(self):
        raise NotImplementedError("Python main configuration support is not implemented")

    def _read_json(self):
        return self.json_config_reader.get_config_dict()["configuration"]

    def _read_xml(self):
        return self.xml_config_reader.get_conf_xml()["configuration"]

    def _get_dict_config(self, d, *keys):
        result = dict(d)
        for key in keys:
            try:
                if (isinstance(result, list)):
                    return None
                else:
                    if result[key] is None:
                        return None
            except KeyError:
                return None
            result = result[key]
        return result

    def get_config(self, *keys):
        d = self.read()
        return self._get_dict_config(d, *keys)


