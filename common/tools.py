# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/17 08:11
# @Author: Enbryan Xie
import os.path
import time
from datetime import datetime



def get_now_time ():
    return datetime.datetime.now ()

def get_project_path ():
    """
    获取项目绝对路径
    :return
    :return:
    """
    project_name = "trading_system_autotest"
    file_path = os.path.dirname(__file__)
    # print(file_path)
    # print(file_path.find(project_name))
    # print(file_path[:file_path.find(project_name)])
    return file_path[:file_path.find(project_name)+len(project_name)]

def get_mysql_path ():
    abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return abs_path

def sep(path, add_sep_before=False, add_sep_after=False):
    all_path = os.path.join(*path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep

    return all_path

def get_img_path(img_name):
    """
    获取商品的路径
    """
    img_dir_path=get_project_path()
    return img_dir_path + sep(["img",img_name], add_sep_before=True)



if __name__ == '__main__':
    # print(get_project_path())
    # print(get_abs_path())

    print(get_img_path("商品图片1.jpg"))

