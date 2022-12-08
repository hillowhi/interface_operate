"""
登录&点击充值
"""

from time import sleep
from data_driver.data_driver.key_word_class.key_operate_browser import KeyOperateBrowser
from data_driver.data_driver.yaml_data import KEY_WORD
from data_driver.data_driver.yaml_driver.login_process import Login
from selenium.webdriver.support import expected_conditions as ec


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
        login_pay.url_login(
            KEY_WORD.YAML_LOGIN, KEY_WORD.PAY_USERNAME, KEY_WORD.PAY_PASSWORD
        )
        # 跳转到付款页 如果页面出现请求异常502 就一直请求直到页面正常展示
        # 流程函数不能去做异常处理，放在test函数里这里只封业务流程
        while True:
            try:
                # 点击充值金额按钮
                self.wait_locat(*KEY_WORD.PAY_BUTTON).click()
                # 502错误页面
                self.wait_locat(*KEY_WORD.PAY_MONEY).click()
                sleep(2)
                # 捕获 页面502则返回上一个页面重试
                self.wait.until(
                    ec.text_to_be_present_in_element(
                        KEY_WORD.PAY_PAGE_BAD_GATEWAY, "502 Bad GateWay"
                    )
                )
                # 测试循环是否正确 (๑•̀ㅂ•́)و✧
                # self.wait.until(
                #     ec.text_to_be_present_in_element(
                #         KEY_WORD.PAY_PAGE_LOGIN, "登录支付宝账户付款"
                #     )
                # )
                self.driver.back()
            except:
                wait = self.wait.until(
                    ec.text_to_be_present_in_element(
                        KEY_WORD.PAY_PAGE_LOGIN, "登录支付宝账户付款"
                    )
                )
                return wait  # wait返回是true or false
