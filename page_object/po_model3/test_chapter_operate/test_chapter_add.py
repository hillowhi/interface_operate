from page_object.po_model3.KEY_VALUE import KEY_WORD_VALUE3
from page_object.po_model3.key_process_chapter.login_process import Login
from page_object.po_model3.key_process_chapter.add_chapter import OperateChapter


def test_chapter_add(get_browser):
    # 登录流程
    # login_test = Login(get_browser)
    # login_test.url_login(URL_LOGIN, USERNAME_AUTHOR, PASSWORD_AUTHOR)
    # 新建章节
    operate = OperateChapter(get_browser)
    operate.chapter_add(KEY_WORD_VALUE3.TEST_TITLE, KEY_WORD_VALUE3.TEST_CONTENT)
