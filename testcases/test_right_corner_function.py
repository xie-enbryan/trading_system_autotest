# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/24 00:41
# @Author: Enbryan Xie
from time import sleep
import allure


# from config.driver_config import DriverConfig
from page.LoginPage import LoginPage

from page.RightCornerImgPage import RightCornerImgPage

class TestRightCornerFunction:

    def test_user_logout(self, driver):
        """
        测试用户从右上角的图标上悬停，然后点击登出
        """
        # driver = DriverConfig().drvier_config()
        with allure.step("登录"):
            LoginPage().login(driver,"william")
            sleep(3)

        with allure.step("将鼠标悬停在右上角的图标中"):
            RightCornerImgPage().right_corner_img_hover(driver)
            sleep(3)

        with allure.step("点击退出登录按钮"):
            RightCornerImgPage().logout_user(driver, "退出登录")
            sleep(3)

        # driver.quit()