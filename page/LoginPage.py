# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/19 01:42
# @Author: Enbryan Xie
import time
from time import sleep

from selenium.webdriver.common.by import By

from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf
from logs.log import log

from common.report_add_img import add_img_path_2_report
from common.ocr_identify import OcrIdentify

class LoginPage(LoginBase, ObjectMap):

    def login_input_value (self, driver, input_placeholder, input_value):
        """
        LoginBase 是用来放置定位元素的
        这里的LoginPage就是用来操作元素的
        登陆页输入值
        """
        log.info("输入" + input_placeholder + "为：" + str(input_value))
        input_xpath= self.login_input(input_placeholder)
        return self.element_fill_value(driver, By.XPATH,input_xpath,input_value)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)

    def click_login (self, driver, button_name):
       """
       点击登陆

       """
       log.info("点击登录")
       button_xpath = self.login_button(button_name)

       # return  driver.find_element_by_xpath(button_xpath).click()

       return self.element_click(driver,By.XPATH,button_xpath)

    def login(self,driver, user, need_captcha=False):
        """
        登录
        :param driver: 浏览器驱动
        :param user:  用户
        :param need_captcha:  是否需要验证码
        :return:
        """
        log.info("跳转登录页")
        self.element_to_url(driver,"/login")
        # if need_captcha:
        #     time.sleep(3)
        #     log.info("需要验证码")
        #     # 点击是否需要验证码的勾选框
        #     self.select_need_captcha(driver)
        #     # 获取到验证码的一个xpath路径
        #     captcha_xpath = self.captcha()
        #     # 将验证码进行截图保存到我们本地
        #     ele_img_path = self.element_screenshot(driver, By.XPATH, captcha_xpath)
        #     #  将得到的截图，加入到测试报告中
        #     add_img_path_2_report(ele_img_path, "图像验证码")
        #     # 使用ddddocr对截图中的验证码进行识别
        #     identify = OcrIdentify().identify(ele_img_path)
        #     # 进行日志记录
        #     log.info("验证码为：" + str(identify))
        #     # 验证码输入框的xpath路径
        #     input_captcha_xpath = self.input_captcha()
        #     # 记录日志
        #     log.info("填入验证码")
        #     # 填入验证码
        #     self.element_fill_value(driver, By.XPATH, input_captcha_xpath, identify)


        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver,"用户名",username)
        self.login_input_value(driver,"密码", password)
        self.click_login(driver, "登录")
        sleep(5)
        self.assert_login_success(driver)


    def login_assert(self, driver, img_name):
        """
        登录后 判断头像
        """

        return self.find_img_in_source(driver, img_name)

    def assert_login_success(self, driver):
        """
        验证是否登录成功
        :return:
        """
        success_xpath = self.login_success()
        return self.element_appear(driver, By.XPATH, success_xpath, timeout=5)

    def select_need_captcha(self, driver):
        """
        点击勾选是否需要验证码
        :param driver:
        :return:
        """
        log.info("点击勾选是否需要验证码")
        select_xpath = self.need_captcha()

        return self.element_click(driver, By.XPATH, select_xpath)



