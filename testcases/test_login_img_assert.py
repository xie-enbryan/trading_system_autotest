# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/26 10:04
# @Author: Enbryan Xie

import  pytest
import allure
from time import  sleep

from page.LoginPage import LoginPage


class TestLoginAssert:

    @pytest.mark.login
    def test_login_assert(self, driver):
        """
        登录后， 断言图片
        """
        with allure.step("登录"):
            LoginPage().login(driver, "william")
            sleep(3)

        with allure.step("进行图片断言操作，对比cnfidence的值"):
            assert LoginPage().login_assert(driver,"head_img.jpeg") > 0.9


