# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/24 23:42
# @Author: Enbryan Xie



import pytest
import  allure

from pytest_assume.plugin import assume

class TestAssume:

    def test_assume(self):
        with allure.step("新增assume假设断言"):
            with assume: assert "william" in "UI Automation"
            pytest.assume(1+1==3)
        with allure.step("新增assert绝对断言"):
            assert 1+1 == 2
            print("over")