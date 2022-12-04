from time import sleep

from data_driver.data_driver.key_word_class.key_operate_browser import KeyOperateBrowser
from data_driver.data_driver.yaml_data import KEY_WORD
from data_driver.data_driver.yaml_driver.login_process import Login


class Book_Pay_Process(KeyOperateBrowser):
    def book_pay_process(self):
        # 调用登录流程
        login_pay = Login(self.driver)
        login_pay.url_login(KEY_WORD.YAML_LOGIN, KEY_WORD.PAY_USERNAME, KEY_WORD.PAY_PASSWORD)
        self.wait_locat(*KEY_WORD.PAY_BUTTON).click()
        sleep(2)
        self.wait_locat(*KEY_WORD.PAY_MONEY).click()
        sleep(3)
