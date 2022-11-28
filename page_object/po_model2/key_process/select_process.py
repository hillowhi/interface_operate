from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_object.po_model2.key_word_class_po3 import KeyWordWebClass
# 导入*就是所有参数
from page_object.po_model2.key_word_list.KEY_WORD_VALUE2 import *

"""
该类主要封装业务流程里的方法
"""


class SelectProcess(KeyWordWebClass):  # 类的继承
    def select_process(self):  # 这里不用参数 参数值调用全放流程函数里可以吗
        self.open_browser(SELECT_URL)
        sleep(2)
        # self.select_by_any(*SELECT_OBJECT_VALUE)  # 神奇 这样就行了
        self.select_by_any(*SELECT_ELEMENT, SELECT_WAY,  SELECT_TEXT, )
        sleep(3)
