# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/23 00:41
# @Author: Enbryan Xie

from time import sleep
import pytest
import allure

# from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.OrderPage import OrderPage

tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
# tab_list=["全部", "待付款"]

class TestOrderBuy:

    @pytest.mark.parametrize("tab", tab_list)
    def test_order_buy(self, driver, tab):
        # driver = DriverConfig().drvier_config()
        with allure.step("登录"):
            LoginPage().login(driver, "william")
            sleep(3)

        with allure.step("点击我的订单"):
            LeftMenuPage().click_level_one_menu(driver, "我的订单")
            sleep(3)

        with allure.step("点击二级菜单 已买到的宝贝"):
            LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
            sleep(3)
        with allure.step("依次点击tab按钮"):
            OrderPage().click_order_tab(driver, tab)
            sleep(2)

        # OrderPage().click_order_tab( driver=driver,tab_name="全部")


        # driver.quit()



