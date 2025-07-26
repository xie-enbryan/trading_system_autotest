# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/24 23:32
# @Author: Enbryan Xie

import random
import pytest
import allure

class TestRandom:

    # @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_random(self):
        with allure.step("测试随机数"):
            num = random.randint(1, 3)
            print("num:" , num)

            if num !=1:
                print("失败")
                raise Exception("出错了")
            else:
                print("成功")


