# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/24 00:06
# @Author: Enbryan Xie

class RightCornerImg:

    def right_corner_img(self):
        """
        定位右上角图像的元素位置
        """
        return "//div[@class='el-row']//span"

    def righ_corner_img_subtree(self, function_name):
        """
        右上角下拉框的功能框定位
        """
        return f"//li[@class='el-dropdown-menu__item' and text()='{function_name}']"



