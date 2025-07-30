# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/17 08:11
# @Author: Enbryan Xie
import os.path
import time
from datetime import datetime

import requests


def get_now_time ():
    return datetime.now()

def get_now_date_time_str():
    """
    将时间转成字符串，
    :return:
    """
    return datetime.now().strftime("%Y%m%d%H%M%S")

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

def get_every_wallpaper():
    """
    从bing获取每日壁纸
    Returns:

    """
    everyday_wallpaper_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&mkt=zh-CN"
    try:
        res = requests.get(url=everyday_wallpaper_url)
        wallpaper_url = "https://cn.bing.com" + res.json()["images"][0]["url"][:-7]
    except Exception as e:
        print(e)
        wallpaper_url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.jj20.com%2Fup%2Fallimg%2Ftp09%2F210F2130512J47-0-lp.jpg&refer=http%3A%2F%2Fimg.jj20.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1660141794&t=23615f6a8b4ca7aa42662f53c93c7717"
    return wallpaper_url





if __name__ == '__main__':
    # print(get_project_path())
    # print(get_abs_path())

    print(get_every_wallpaper())

