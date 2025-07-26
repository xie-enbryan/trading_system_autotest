# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/19 01:58
# @Author: Enbryan Xie

from time import sleep
import allure
import pytest

# from config.driver_config import DriverConfig

from page.LoginPage import LoginPage

from common.report_add_img import add_img_2_report

class TestLogin:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录")
    def test_login(self, driver):
        # driver = DriverConfig().drvier_config()
        # 自己的服务器地址是：http://119.91.206.145/login?url=%2F
        # 公网的服务器地址是： http://www.tcpjwtester.top/login?url=%2F
        # driver.get("http://www.tcpjwtester.top/login?url=%2F")
        # sleep(3)
        # LoginPage().login_input_value(driver,"用户名", "jay")
        # sleep(1)
        # LoginPage().login_input_value( driver, "密码", "123456")
        # sleep(1)
        # LoginPage().click_login(driver, "登录")
        # sleep(3)
        with allure.step("登录"):
            LoginPage().login(driver,"failure")
            sleep(3)
            add_img_2_report(driver, "登录")
        # driver.quit()


