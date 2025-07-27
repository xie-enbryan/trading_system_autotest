# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/19 22:56
# @Author: Enbryan Xie

class HomeBase:
    def wallet_switch(self):
        """
        首页的钱包开关
        """
        return "//span[contains(@class, 'el-switch')]"

    def logo(self):
        """
        进入系统后，左上角的logo标签
        """
        return "//div[contains(text(),'校园二手交易系统')]"

    def welcome(self):
        """
        首页欢迎回来的标签
        """
        return "//span[starts-with(text(),'欢迎您回来')]"

    def home_user_avator(self):
        """
        首页用户头像大图
        """
        return "//span[contains(text(),'欢迎您回来')]/parent::div/preceding-sibling::div//div[@class='el-image']"

    def home_user_avatat_2(self):
        """
        首页用户头像大图二
        """
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class, 'user_avatar')]/div/div"

    def user_balance(self):
        """
        用户首页-- 账户余额的元素定位
        :return:
        """
        return "//th[text()='账户余额']/parent::tr/following-sibling::tr/td[1]"