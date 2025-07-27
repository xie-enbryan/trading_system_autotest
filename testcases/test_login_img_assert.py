# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/26 10:04
# @Author: Enbryan Xie

import  pytest
import allure
from time import  sleep

from page.LoginPage import LoginPage

from common.report_add_img import add_img_2_report, add_img_path_2_report


class TestLoginAssert:

    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录后断言图片")
    def test_login_assert(self, driver):
        """
        登录后， 断言图片
        """
        with allure.step("登录"):
            LoginPage().login(driver, "william")
            sleep(3)
            add_img_2_report(driver, "登录")

        with allure.step("断言图片"):
            assert LoginPage().login_assert(driver,"head_img.jpeg") > 0.9


