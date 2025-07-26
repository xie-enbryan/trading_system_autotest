# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/23 23:08
# @Author: Enbryan Xie

class IframeBaiduMapBase:

    def search_button(self):
        """
        定义iframe中的baidu 搜索按钮
        """
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):

        return "//iframe[@src='https://map.baidu.com/']"