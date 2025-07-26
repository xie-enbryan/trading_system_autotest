# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/22 23:43
# @Author: Enbryan Xie

from base.ObjectMap import ObjectMap

class ExternalLinkPage(ObjectMap):

    def goto_imooc(self, driver):
        """
        切换窗口句柄为慕课网
        """
        self.switch_window_2_latest_handle(driver)
        return driver.title


