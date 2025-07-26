# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/22 21:24
# @Author: Enbryan Xie
import time
from time import sleep

from selenium.webdriver.common.by import By

from base.GoodsBase import GoodsBase
from base.ObjectMap import ObjectMap
from config.driver_config import DriverConfig
from common.tools import get_img_path

class GoodsPage (GoodsBase, ObjectMap):

    driver = DriverConfig().drvier_config()

    def input_goods_title(self,driver, input_value):
        """
        填入商品标题
        """
        # 先获取商品的标题输入框
        goods_title_path = self.goods_title()
        return self.element_fill_value(driver,By.XPATH,goods_title_path,input_value)

    def input_goods_details(self, driver, input_value):
        """
        填入商品详情
        """
        goods_details_path = self.goods_details()
        return self.element_fill_value(driver, By.XPATH,goods_details_path,input_value)

    def select_goods_num(self, driver, number):
        """
        选择商品数量
        """
        goods_num_path = self.goods_num(plus=True)
        for i in range(number):
            self.element_click(driver,
                               By.XPATH,
                               goods_num_path,)
            time.sleep(0.5)

    def upload_goods_img(self, driver, img_name):
        """
        上传商品图片
        """
        # 获取图片路径
        img_path = get_img_path(img_name)
        # 获取上传路径
        upload_xpath = self.goods_img()

        return self.upload(driver, By.XPATH, upload_xpath, img_path)

    def input_goods_price(self, driver, input_value):
        """
        输入商品单价
        """
        goods_price_xpath = self.goods_price()
        return self.element_fill_value(driver, By.XPATH, goods_price_xpath, input_value)

    def select_goods_status(self, driver,input_value):
        """
        选择商品状态
        """
        goods_status_xpath = self.goods_status()
        self.element_click(driver,By.XPATH, goods_status_xpath)
        sleep(1)
        goods_status_select_xpath = self.goods_status_select(input_value)
        return self.element_click(driver, By.XPATH, goods_status_select_xpath)

    def click_bottom_button(self, driver, button_name):
        """
        点击底部按钮
        """
        button_xpath = self.add_goods_bottom_button(button_name)
        return self.element_click(driver,By.XPATH,button_xpath)


    def add_new_goods(
                      self,
                      driver,
                      goods_title,
                      goods_details,
                      goods_number,
                      goods_images,
                      goods_price,
                      goods_status,
                      bottom_button_name
    ):
        """
        新增二手商品
        """
        self.input_goods_title(driver,goods_title)
        self.input_goods_details(driver, goods_details)
        self.select_goods_num(driver, goods_number)
        for goods_image in goods_images:
            self.upload_goods_img(driver, goods_image)
            sleep(5)
        self.input_goods_price(driver, goods_price)
        self.select_goods_status(driver, goods_status)
        self.click_bottom_button(driver, bottom_button_name)

        return True














