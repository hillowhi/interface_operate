import time

import pytest
from selenium.webdriver.common.by import By

"""
线性代码登录流程
基类封装请看 key_word_op文件夹
"""


@pytest.mark.skip
def test_login(get_browser):
    get_browser.get("http://novel.hctestedu.com/")
    time.sleep(2)
    get_browser.find_element(By.XPATH, """//a[text()="登录"]""").click()
    get_browser.find_element(By.XPATH, """//input[@placeholder="手机号码"]""").send_keys("15224880595")
    get_browser.find_element(By.XPATH, """//input[@placeholder="密码"]""").send_keys("huange521")
    get_browser.find_element(By.XPATH, """//input[@value="登录"]""").click()
    time.sleep(5)
