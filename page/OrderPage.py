# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/23 00:37
# @Author: Enbryan Xie

from selenium.webdriver.common.by import By

from base.OrderBase import OrderBase
from base.ObjectMap import ObjectMap

class OrderPage (OrderBase, ObjectMap):

    def click_order_tab(self, driver, tab_name):
        """
        点击已买到的宝贝tab栏按钮
        """
        tab_xpath = self.order_tab(tab_name)
        return self.element_click(driver, By.XPATH, tab_xpath)

