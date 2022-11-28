# 导入变量文件 直接用*表示所有的变量导入
from page_object.po_model.KEY_WORD_VALUE import *
from page_object.po_model2.key_process.key_api_po_up import KeyApiOpTwo
from page_object.po_model2.key_process.select_process import SelectProcess


def test_select(get_browser):
    key_select = SelectProcess(get_browser)
    key_select.select_process()

