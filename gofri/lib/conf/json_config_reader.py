import json


class JSONConfigReader:
    def __init__(self, root_path):
        self.root_path = root_path
        self.file_path = root_path + "/conf.json"

    def get_config_dict(self):
        with open(self.file_path, "r+") as _file:
            return json.load(_file) 