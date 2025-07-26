# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/23 13:31
# @Author: Enbryan Xie

from time import sleep
import allure

from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.AccountPage import AccountPage

# from config.driver_config import DriverConfig



class TestPersonalInfo:

    def test_upload_personal_vatar(self, driver):
        """
        测试用户头像上传保存功能
        """
        # 获取浏览器驱动
        # driver = DriverConfig().drvier_config()
        with allure.step("登录"):
            LoginPage().login(driver, "william")
            sleep(3)

        with allure.step("点击一级菜单 账户设置"):
            LeftMenuPage().click_level_one_menu(driver, "账户设置")
            sleep(3)

        with allure.step("点击二级菜单 个人资料"):
            LeftMenuPage().click_level_two_menu(driver, "个人资料")
            sleep(3)

        with allure.step("点击上传图像按钮"):
            AccountPage().upload_avatar(driver, "个人头像1.jpeg")
            sleep(3)

        with allure.step(" 点击保存按钮"):
            AccountPage().click_save(driver)
            sleep(3)

        # driver.quit()



