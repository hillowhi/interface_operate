# 导入变量文件 直接用*表示所有的变量导入
from page_object.po_model.KEY_WORD_VALUE import *
from page_object.po_model2.key_process.key_api_po_up import KeyApiOpTwo
from page_object.po_model2.key_process.select_process import SelectProcess
from page_object.po_model2.key_word_list.KEY_WORD_VALUE2 import ENTER_KEY


def test_select(get_browser):
    key_select = SelectProcess(get_browser)
    key_select.select_process()
    key_send = SelectProcess(get_browser)
    key_send.key_send(ENTER_KEY)

# def test_pull_down_key(get_browser):


