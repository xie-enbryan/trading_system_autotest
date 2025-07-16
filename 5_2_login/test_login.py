# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/16 07:18
# @Author: Enbryan Xie

# 用来访问我们的浏览器的
from config.driver_config import DriverConfig
from time import sleep

# 实例化一个driver对象
driver = DriverConfig().driver_config()
driver.get("http://119.91.206.145/login?url=%2F")
sleep(2)
driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("周杰伦")
sleep(2)
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("123456")
sleep(2)
driver.find_element_by_xpath("//span[text()='登录']/parent::button").click()
sleep(3)
driver.quit()







