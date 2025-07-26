# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/23 00:32
# @Author: Enbryan Xie


class OrderBase:

    def order_tab(self,tab_name):
        """
        已买到的宝贝，tab按钮
        全部，待付款，待发货，运输中，待确认，待评价
        """
        return f"//div[@role='tab' and text()='"+tab_name+"']"

if __name__ == '__main__':
    print(OrderBase().order_tab("待发货"))