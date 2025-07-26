# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/24 00:32
# @Author: Enbryan Xie

from selenium.webdriver.common.by import By

from base.ObjectMap import  ObjectMap
from base.RightCornerImg import RightCornerImg

class RightCornerImgPage(ObjectMap, RightCornerImg):

    def right_corner_img_hover(self, driver):
        """
        将鼠标悬停在右上角图像的位置
        """
        # 获取右上角图像的位置
        img_xpath = self.right_corner_img()
        return self.element_hover(driver, By.XPATH,img_xpath)

    def logout_user(self, driver, function_name):
        """
        从右上角的图标，点击登出按钮
        """
        # 获取右上角的登出按钮
        logout_xpath = self.righ_corner_img_subtree(function_name)

        # 点击登出按钮
        return self.element_click(driver, By.XPATH, logout_xpath)





