import os

import allure
import pytest

# @allure.step("开始输入用户名：")
# def input_username():
#     print("请输入用户名")
#
#
# @allure.step("请输入密码：")
# def input_password():
#     print("请输入密码：")
#
#
# class TestAllureLogin:
#     def test_allure_login(self):
#         print("开始运行登录自动化脚本：")
#         input_username()
#         input_password()
#         assert 1 == 2
from allure_report_po.KeyValue import KEY_VALUE
from allure_report_po.logic_service.logic_login import SetUpLogic


def test_title_compare(get_browser):
    driver = get_browser
    driver.get('https://www.baidu.com/')
    driver.find_element('id', 'kw').send_keys('大笨钟')
    driver.find_element('id', 'su').click()
    title = driver.title
    assert title == '大笨钟-百度搜索'  # 实际是 大笨钟_百度搜索


@pytest.fixture(scope='session')
def login_fix():
    with allure.step('前置登录辣'):
        setup_login = SetUpLogic
        setup_login.login(*KEY_VALUE.LOCATER)


@allure.title("登录流程用例")
def test_login():
    """
            用例步骤：
            1.登录
            2.浏览商品
            3.添加商品
            4.购物车结算
    """
    with allure.step('浏览商品'):
        assert 1 == 2
