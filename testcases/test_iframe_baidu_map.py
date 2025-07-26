# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/23 23:13
# @Author: Enbryan Xie

import allure

from time import sleep

# from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.IframeBaiduMapPage import IframeBaiduMapPage

class TestIframeBaiduMap:

    def test_iframe_baidu_map(self, driver):

        # driver = DriverConfig().drvier_config()
        with allure.step("登录"):
            LoginPage().login(driver, "william")
            sleep(3)
        with allure.step("点击一级菜单 “iframe测试”"):
            LeftMenuPage().click_level_one_menu(driver,"iframe测试")
            sleep(2)

        with allure.step("切换到百度的iframe中"):
            # 切到百度iframe
            IframeBaiduMapPage().switch_2_baidu_map_iframe(driver)
        with allure.step("定位到百度iframe中的百度搜索按钮"):
            # 定位到iframe的baidu搜索按钮
            IframeBaiduMapPage().get_baidu_map_search_button(driver)

        with allure.step(" 从首页切回主页"):
            # 从首页切回主页
            IframeBaiduMapPage().iframe_out(driver)

        with allure.step("切回测试系统的主页"):
            # 回到我们的主页
            LeftMenuPage().click_level_one_menu(driver, "首页")
            sleep(3)

        # driver.quit()
