# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/22 22:24
# @Author: Enbryan Xie

from time import sleep

import pytest
import allure


from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage
from common.report_add_img import add_img_2_report

goods_info_list = [
    {
        "goods_title": "新增商品列表1",
        "goods_details": "新增批量商品详情1",
        "goods_number": 1,
        "goods_images": ["商品图片1.jpg"],
        "goods_price": 120,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    },
    {
        "goods_title": "新增商品列表2",
        "goods_details": "新增批量商品详情2",
        "goods_number": 2,
        "goods_images": ["商品图片1.jpg"],
        "goods_price": 200,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    },
]

class TestAddGoods:

    @pytest.mark.parametrize("goods_info", goods_info_list)
    @allure.epic("添加商品epic")
    @allure.feature("添加商品功能feature")
    @allure.story("添加商品story")
    @allure.tag("添加商品tag")
    def test_add_goods_001(self, driver, goods_info):
        # driver = DriverConfig().drvier_config()
        with allure.step("登录"):
            LoginPage().login(driver, "william")
            sleep(3)
            # add_img_2_report(driver,"登录")

        with allure.step("点击一级菜单 “产品”"):
            LeftMenuPage().click_level_one_menu(driver, "产品")
            sleep(1)
            # add_img_2_report(driver, "点击产品菜单")

        with allure.step("点击二级菜单 “新增二手商品”"):
            LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
            sleep(2)
            # add_img_2_report(driver, "点击新增二手商品")

        with allure.step("新增二手商品"):
            GoodsPage().add_new_goods(
                driver=driver,
                goods_title=goods_info["goods_title"],
                goods_details = goods_info["goods_details"],
                goods_number=goods_info["goods_number"],
                goods_images=goods_info["goods_images"],
                goods_price = goods_info["goods_price"],
                goods_status=goods_info["goods_status"],
                bottom_button_name = goods_info["bottom_button_name"]
            )
            sleep(3)
        # driver.quit()





