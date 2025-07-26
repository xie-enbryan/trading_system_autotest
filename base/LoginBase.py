# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/19 00:35
# @Author: Enbryan Xie

class LoginBase:

    def login_input(self, input_placeholder):
        """
        输入账号密码，登陆
        """
        return "//input[@placeholder='"+input_placeholder+"']"
        # return f"//input[@placeholder='{input_placeholder}']"

    def login_button (self, button_name):
        """
        登陆按钮
        return
        """
        return "//span[text()='"+button_name+"']/parent::button"
        # return f"//span[@text()='{button_name}']/parent::button"

    def login_success(self):
        """
        登录成功
        :return:
        """
        return "//p[text()='登录成功']"

# if __name__ == '__main__':
#     # print(LoginBase().Login_input("密码"))
#     print(LoginBase().login_button("登陆"))


