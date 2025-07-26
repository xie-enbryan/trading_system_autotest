# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/24 22:01
# @Author: Enbryan Xie

import pytest
from config.driver_config import DriverConfig

@pytest.fixture()
def driver():
    get_driver = DriverConfig().drvier_config()
    yield get_driver
    get_driver.quit()

# 钩子： 在pytest收集测试用例时调用
def pytest_collection_modifyitems(config, items):
    # 获取当前测试用例所有的个数
    num_tests = len(items)

    # 打印当前需要执行的测试用例的个数
    print(f"\n Total number of test cases to be expected: {num_tests}")

