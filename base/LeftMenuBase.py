# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/20 13:42
# @Author: Enbryan Xie


class LeftMenuBase:

    def level_one_menu(self, menu_name):
        """
        一级菜单栏
        菜单栏名称

        """
        return "//aside[@class='el-aside']//span[text()='"+menu_name+"']/ancestor::li"
        # return f"//aside[@class='el-aside']//span[text()='{menu_name}']/ancestor::div[@class='el-submenu__title']"

 # "//aside[@class='el-aside']//span[text()='产品']/ancestor::div[@class='el-submenu__title']"

    def level_two_menu(self,menu_name):
        """
        二级菜单栏
        """
        return f"//aside[@class='el-aside']//span[text()='{menu_name}']/parent::li"

    def sell_products_button(self, button_name):
        return f"//div[@class='el-card__body']//div[text()='{button_name}']"




if __name__ == '__main__':
    # print(LeftMenuBase().level_one_menu("产品"))
    print(LeftMenuBase().level_two_menu("我的商品列表"))
    #  print(LeftMenuBase().sell_products_button("待评价"))