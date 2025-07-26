# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/23 13:22
# @Author: Enbryan Xie

from selenium.webdriver.common.by import By

from base.AccountBase import AccountBase
from base.ObjectMap import ObjectMap
from common.tools import get_img_path


class AccountPage(AccountBase, ObjectMap):

    def upload_avatar(self, driver,img_name):

        """
        个人资料上传头像
        """
        # 获取图片路径
        img_path = get_img_path(img_name)
        # 获取上传路径
        upload_xpath = self.basic_info_avatar_input ()
        # 图片上传
        return self.upload(driver, By.XPATH, upload_xpath, img_path)

    def click_save(self, driver):
        """
        个人资料，点击保存按钮
        """

        # 先获得元素的路径
        click_path = self.basic_info_save_button()
        return self.element_click(driver, By.XPATH, click_path)