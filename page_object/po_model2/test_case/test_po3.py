import pytest

from page_object.po_model.KEY_WORD_VALUE import *
# 导入变量文件 直接用*表示所有的变量导入
from page_object.po_model2.key_process.key_api_po_up import KeyApiOpTwo


@pytest.mark.skip
def test_login(get_browser):
    # 这里测试用例调用fixture函数
    key_login = KeyApiOpTwo(get_browser)
    key_login.op_login(URL, USERNAME, PASSWORD)
