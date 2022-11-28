from page_object.po_model.KEY_WORD_VALUE import *
# 导入变量文件 直接用*表示所有的变量导入
from page_object.po_model.key_api_po import KeyApiOp


def test_login(get_browser):
    # 这里测试用例调用fixture函数
    key_login = KeyApiOp(get_browser)
    key_login.op_login(URL, USERNAME, PASSWORD)
