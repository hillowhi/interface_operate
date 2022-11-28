from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

from page_object.key_word_op.key_word_class_op import KeyWordWeb

"""
该类主要封装业务流程里的方法
"""


class KeyApiOp(KeyWordWeb):
    # 类的继承KeyWordWeb是KeyApiOp的父类
    # 所以KeyApiOp不需要再声明一个浏览器对象
    def op_login(self, url, username, password):
        self.open_browser(url)
        # 写一段校验证明这个url确实打开了 用显示等待
        wait = WebDriverWait(self.driver, 10)
        # # 校验页面是否出现登录字样判断页面是否加载正确
        wait.until(ec.text_to_be_present_in_element((By.XPATH, "//a[text()='登录']"), "登录"))
        self.find_el(By.XPATH, """//a[text()="登录"]""").click()
        self.find_el(By.XPATH, """//input[@placeholder="手机号码"]""").send_keys(username)
        self.find_el(By.XPATH, """//input[@placeholder="密码"]""").send_keys(password)
        self.find_el(By.XPATH, """//input[@value="登录"]""").click()
        sleep(2)
        # 确保登陆完成 找一个成功登录后出现的元素作为条件
        wait_login = WebDriverWait(self.driver, 6)
        wait_login.until(ec.text_to_be_present_in_element((By.XPATH, """//a[@class="mr15"]"""), username))
        # /(ㄒoㄒ)/~~ 这个括号！！！好烦 找了好久的问题
