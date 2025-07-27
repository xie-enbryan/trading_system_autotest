# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/27 18:15
# @Author: Enbryan Xie

from time import  sleep

import  pytest
import allure

from common.report_add_img import add_img_2_report
from page.LoginPage import LoginPage
class TestCaotchaLogin:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("验证码登录")
    def test_captcha_login(self, driver):
        """
        验证码登录
        :param driver:
        :return:
        """
        with allure.step("登录"):
            LoginPage().login(driver, "william", need_captcha=False)
            sleep(3)
            add_img_2_report(driver, "登录")

