'''
登录&点击充值
'''

from time import sleep
from data_driver.data_driver.key_word_class.key_operate_browser import KeyOperateBrowser
from data_driver.data_driver.yaml_data import KEY_WORD
from data_driver.data_driver.yaml_driver.login_process import Login


class BookPayProcess(KeyOperateBrowser):
    def book_pay_process(self):
        # 调用登录流程 普通版
        # login_pay = Login(self.driver)
        # login_pay.url_login(KEY_WORD.YAML_LOGIN, KEY_WORD.PAY_USERNAME, KEY_WORD.PAY_PASSWORD)
        # self.wait_locat(*KEY_WORD.PAY_BUTTON).click()
        # sleep(2)
        # self.wait_locat(*KEY_WORD.PAY_MONEY).click()
        # sleep(3)
        # 当请求遇到异常怎么办 走重试机制 下面重试机制是重试多少次

        # 登录
        login_pay = Login(self.driver)
        login_pay.url_login(KEY_WORD.YAML_LOGIN, KEY_WORD.PAY_USERNAME, KEY_WORD.PAY_PASSWORD)
        # 跳转到付款页 如果页面出现请求异常 就一直请求
        while True:
            try:
                self.wait_locat(*KEY_WORD.PAY_BUTTON).click()
                break
            except:
                pass
