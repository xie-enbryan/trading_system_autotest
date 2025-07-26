# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/26 11:29
# @Author: Enbryan Xie

from time import  sleep

import  allure


def add_img_2_report(driver, step_name, need_sleep=True):
    """
    截图并插入allure 报告中
    """
    if need_sleep:
        sleep(2)
    allure.attach(
        driver.get_screenshot_as_png(),
        step_name + ".png",
        allure.attachment_type.PNG
    )