import time

import pytest
from selenium.webdriver.common.by import By

from page_object.key_word_op.key_word_class_op import KeyWordWeb


@pytest.mark.skip
def test_login(get_browser):
    # 给类KeyWordWeb 传入conftest里面定义获取浏览器对象的方法
    key_class = KeyWordWeb(get_browser)
    key_class.open_browser("http://novel.hctestedu.com/")
    # get_browser.get("http://novel.hctestedu.com/") #线性写法
    key_class.find_el(By.XPATH, """//a[text()="登录"]""").click()
    time.sleep(3)
    # get_browser.find_element(By.XPATH, """//a[text()="登录"]""").click()
    key_class.find_el(By.XPATH, """//input[@placeholder="手机号码"]""").send_keys("15224880595")
    time.sleep(3)
    # get_browser.find_element(By.XPATH, """//input[@placeholder="手机号码"]""").send_keys("15224880595")
    key_class.find_el(By.XPATH, """//input[@placeholder="密码"]""").send_keys("huange521")
    time.sleep(3)
    # get_browser.find_element(By.XPATH, """//input[@placeholder="密码"]""").send_keys("huange521")
    key_class.find_el(By.XPATH, """//input[@value="登录"]""").click()
    # get_browser.find_element(By.XPATH, """//input[@value="登录"]""").click()
    time.sleep(5)
