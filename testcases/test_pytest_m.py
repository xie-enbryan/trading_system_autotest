# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/24 08:26
# @Author: Enbryan Xie

from time import sleep
import pytest
import allure

# from config.driver_config import DriverConfig


class TestPytestMClass:

    @pytest.fixture(scope="class")
    def scope_class(self):
        print("我是class级别，我只执行一次")

    # @pytest.fixture(scope="function")
    # def driver(self):
    #     get_driver=DriverConfig().drvier_config()
    #     return get_driver

    @pytest.mark.bing
    def test_open_bing(self, driver, scope_class):
        # driver = DriverConfig().drvier_config()
        with allure.step("测试pytest mark功能，打开bing网站"):
            driver. get("https://www.bing.com/?mkt=zh-CN")
            sleep(3)
        # driver.quit()

    @pytest.mark.baidu
    def test_open_baidu(self, driver, scope_class):
        with allure.step("测试pytest mark功能，打开百度网站"):
            print("test_open_baidu")
        # driver = DriverConfig().drvier_config()
            driver.get("https://www.baidu.com")
            sleep(3)
        # driver.quit()

    @pytest.mark.google
    def test_open_google(self, driver, scope_class):

        # driver = DriverConfig().drvier_config()
        with allure.step("测试pytest mark功能，打开google网站"):
            driver.get("https://www.google.com/")
            sleep(3)
        # driver.quit()

