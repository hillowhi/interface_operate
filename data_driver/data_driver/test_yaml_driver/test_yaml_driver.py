from time import sleep

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from data_driver.data_driver.yaml_data import KEY_WORD
from data_driver.data_driver.yaml_driver.login_process import Login
from data_driver.data_driver.yaml_driver.yaml_driver import load_yaml
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.skip
def test_yaml_driver():
    yaml_data = load_yaml('../data_driver/yaml_data/login_yaml_data.yaml')
    print(yaml_data)


# 参数化登录参数
@pytest.mark.parametrize('data', load_yaml('./yaml_data/login_yaml_data.yaml'))
def test_login_yaml_data(get_browser, data):
    # 下面校验用到wait 所以要初始化一个wait
    wait = WebDriverWait(get_browser, 5)
    yaml_login = Login(get_browser)
    print(data['username'])
    yaml_login.url_login(KEY_WORD.YAML_LOGIN, str(data['username']), str(data['password']))
    sleep(4)
    # str(data['username']) 因为数据取出来 是元组格式 要转化成字符串
    # 用例校验 当登录名出现在页面上则校验登陆成功 用ec模块校验
    name = str(data['username'])
    # wait.until(ec.text_to_be_present_in_element((By.LINK_TEXT, name), name))
    wait.until(ec.text_to_be_present_in_element((KEY_WORD.LOGIN_USERNAME), name))
