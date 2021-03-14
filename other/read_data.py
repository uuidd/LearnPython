import os
import yaml


class ReadData:
    
    def __ret_yaml_data(self, file_name):
        file_path = os.getcwd() + os.sep + "dev_title" + os.sep + "data" +os.sep + file_name + ".yml"
        with open(file_path, "r") as f:
            return yaml.load(f)

    def login_data(self):
        rd = ReadData()
        data_list = []
        data = rd.__ret_yaml_data("login_data").get("login_data")
        for i in data.keys():
            data_list.append((data.get(i).get("phb"), data.get(i).get("pwd")))
        return data_list