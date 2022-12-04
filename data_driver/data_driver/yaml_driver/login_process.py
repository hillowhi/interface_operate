from time import sleep

from page_object.po_model3.KEY_VALUE.KEY_WORD_VALUE3 import *
from page_object.po_model3.key_word_class.key_operate_browser import KeyOperateBrowser

"""
封装一下登录流程
该流程只需要传入用户名+密码，
该流程是直接打开登录url 输入用户名+密码点击登录
"""


class Login(KeyOperateBrowser):
    def url_login(self, login_url, name, password):
        # 登录页面都是同样的,所以可以把元素定位这一步骤封装到流程类里，（登录页也可以写死🤔）
        # 但是这样就涉及到打开新页面的问题，所以引用的时候需要窗口切换
        # 其实最好就是把登录入口也封起来，只需要传入口元素定位+用户名密码就好
        self.open_browser(login_url)
        self.find_el(*LOCATOR_USERNAME).send_keys(name)
        self.find_el(*LOCATOR_PASSWORD).send_keys(password)
        self.find_el(*LOCATOR_LOGIN_BUTTON).click()
        sleep(2)

    # 再封装一个点击登录入口登录的流程，由于该网站都是原页面刷新的不涉及新页面切换
    def click_login(self, find_way, value, name, password):
        self.find_el(find_way, value).click()
        sleep(1)
        self.find_el(*LOCATOR_USERNAME).send_keys(name)
        self.find_el(*LOCATOR_USERNAME).send_keys(password)
        self.find_el(*LOCATOR_LOGIN_BUTTON).click()
        sleep(1)

    # 整合
    def url_login1(self, name, password, login_url, find_way=None, value=None):
        if find_way is None and name is None:
            self.open_browser(login_url)
            self.find_el(*LOCATOR_USERNAME).send_keys(name)
            self.find_el(*LOCATOR_PASSWORD).send_keys(password)
            self.find_el(*LOCATOR_LOGIN_BUTTON).click()
            sleep(2)
            self.find_el(find_way, value).click()
            sleep(1)
        self.find_el(*LOCATOR_USERNAME).send_keys(name)
        self.find_el(*LOCATOR_USERNAME).send_keys(password)
        self.find_el(*LOCATOR_LOGIN_BUTTON).click()
        sleep(1)
