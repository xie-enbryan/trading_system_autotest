# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/23 23:10
# @Author: Enbryan Xie


from selenium.webdriver.common.by import By

from base.IframeBaiduMapBase import IframeBaiduMapBase
from base.ObjectMap import ObjectMap

class IframeBaiduMapPage(IframeBaiduMapBase, ObjectMap):

    def get_baidu_map_search_button(self, driver):
        """
        获取百度地图搜索按钮
        """
        button_xpath = self.search_button()
        return self.element_get(driver,By.XPATH, button_xpath)

    def switch_2_baidu_map_iframe(self, driver):
        """
        切换到百度地图的iframe
        """
        iframe_xpath = self.baidu_map_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def iframe_out(self, driver):
        """
        从百度地图iframe切回校园二手交易系统
        """
        return self.switch_from_iframe_to_content(driver)