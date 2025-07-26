# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/22 07:37
# @Author: Enbryan Xie

class GoodsBase:
    def goods_title(self):
        """
        商品标题
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品标题']"

    def goods_details(self):
        """
        商品详情
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品详情']"

    def goods_num(self, plus=True):
        """
        商品数量
        plus: 如果plus为true，则为使用加号， 如果为False则为直接输入数量
        """
        if plus:
            return "//label[@for='product_stock']/following-sibling::div//i[@class='el-icon-plus']/parent::span"
        else:
            return "//label[@for='product_stock']/following-sibling::div//input[@placeholder='商品数量']"

    def goods_img(self):
        """
        商品图片
        """
        return "//input[@type='file']"

    def goods_price(self):
        """
        商品单价
        """
        return "//form[@class='el-form']//input[@placeholder='请输入商品单价']"

    def goods_status(self):
        """
        商品状态
        """
        return "//form[@class='el-form']//input[@placeholder='请选择商品状态']"

    def goods_status_select(self, select_name):
        """
        商品状态选择
        状态选择： 上架或下架
        """
        return f"//span[text()='{select_name}']/parent::li"


    def add_goods_bottom_button(self,button_name):
        """
        新增二手商品底部按钮
        """
        return f"//span[text()='{button_name}']/parent::button"


