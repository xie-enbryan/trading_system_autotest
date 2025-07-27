# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/17 00:09
# @Author: Enbryan Xie

# file = open("/Users/dehuixie/Documents/trading_system_autotest/trading_system_autotest/config/environment.yaml", encoding="utf-8")
# try:
#     a = file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#    file.close()

import yaml
from common.tools import get_project_path,sep,get_mysql_path
# from tools import get_project_path, sep,get_mysql_path


class GetConf:
    def __init__(self):
        with open(get_project_path() + sep(["config","environment.yaml"],add_sep_before=True),
                   "r",encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)


    def get_username_password(self,user):
        return self.env["user"][user]["username"], self.env["user"][user]["password"]
        # return self.env["username"], self.env["password"]


    def get_mysql_data (self):
        with open (get_mysql_path()+sep(["config","environment.yaml"],add_sep_before=True),
                   "r", encoding="utf-8") as f:
            self.f = yaml.load(f, Loader=yaml.FullLoader)
            return self.f

    def get_utl (self):
        with open(get_project_path()+sep(["config","environment.yaml"], add_sep_before=True),
                  "r", encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            return self.env["url"]

    def get_mysql_config(self):
        """
        获取config里mysql的配置信息
        :return:
        """
        return self.env["mysql"]

if __name__ == '__main__':
    # print(GetConf().get_username_password())
    # print(GetConf().get_mysql_data())

    # print(GetConf().get_utl())
    print(GetConf().get_mysql_config())

