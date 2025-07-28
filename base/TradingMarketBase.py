# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/28 13:14
# @Author: Enbryan Xie


class TradingMarketBase:

    def search_input(self):
        """
        定位搜索宝贝输入框
        :return:
        """
        return "//div[text()='搜索宝贝']/following-sibling::input"

    def search(self):
        """
        定位交易界面的搜素按钮
        :return:
        """
        # //div[text()='搜索宝贝']/following-sibling::input/following-sibling::div/button
        return self.search_input() + "/following-sibling::div/button"

    def product_card(self, product_name):
        """
        商品交易卡片的定位
        :param product_name: 商品名称
        :return:
        """
        # //div[contains(text(), '交易流测试20250728001313')]/ancestor::div[@class='el-card__body']
        return "//div[contains(text(), '"+product_name+"')]/ancestor::div[@class='el-card__body']"

    def i_want_button(self):
        """
        我想要 按钮定位
        :return:
        """
        return "//span[text()='我想要']/parent::button"

    def receive_address(self):
        """
        收货地址
        :return:
        """
        return "//input[@placeholder='收货地址']"

    def receive_address_detail(self, num, address=None):
        """
        用户具体的收货地址
        :param num:
        :param address:
        :return:
        """
        if address:
            # //span[text()='南京市']/parent::li
            return  "//span[text()='"+address+"']/parent::li"
        else:
            # //ul[contains(@class, 'list')]/li[1]
            return "//ul[contains(@class, 'list')]/li["+str(num)+"]"

    def bottom_confirm(self):
        """
        底部的确定 按钮
        :return:
        """
        return "//span[text()='确 定']/parent::button"



if __name__ == '__main__':
    print(TradingMarketBase().search())