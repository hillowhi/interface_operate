"""
fixture前后置函数
前置：
创建一个driver对象
后置：
关闭浏览器
注意！！！！！
此文件演示的是线性代码完成登录
封装基类请看keyword文件夹

"""

import pytest
import time
from selenium import webdriver

"""
线性代码示例
"""

# @pytest.fixture
# def get_browser():
#     # option = webdriver.ChromeOptions()
#     # # 隐藏窗口
#     # option.add_argument('headless')
#     # # 防止打印一些无用的日志
#     # option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
#     # driver = webdriver.Chrome(chrome_options=option)
#     # driver.set_window_size(800, 800)
#     # driver.set_window_position(1000, -100)
#     # 返回一个driver对象
#     driver = webdriver.Chrome()
#     yield driver
#     # 后置操作 关闭浏览器
#     driver.quit()

"""
工具类封装示例 
"""


@pytest.fixture
def get_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    time.sleep(6)
    # 后置操作 关闭浏览器
    driver.quit()
