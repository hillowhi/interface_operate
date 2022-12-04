"""
该类封装的是作家专区小说的操作流程
主要是新增小说章节
    编辑章节
"""
from time import sleep

from page_object.po_model3.KEY_VALUE import KEY_WORD_VALUE3
from page_object.po_model3.key_process_chapter.login_process import Login
from page_object.po_model3.key_word_class.key_operate_browser import KeyOperateBrowser
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver


class OperateChapter(KeyOperateBrowser):
    def chapter_add(self, title, content):
        login = Login(self.driver)
        # # 这里！！！！ 引用其他流程的类函数时，一定要继承一下装饰器里定义的driver ！！！     没用。
        login.url_login(
            KEY_WORD_VALUE3.URL_LOGIN,
            KEY_WORD_VALUE3.USERNAME_AUTHOR,
            KEY_WORD_VALUE3.PASSWORD_AUTHOR,
        )  # 咩呀？
        # 登陆后直接跳转到首页 点击作家专区
        self.find_el(*KEY_WORD_VALUE3.AUTHOR_AREA1).click()
        sleep(2)
        # 等到浏览器出现两个窗口时 该方法不好用
        self.wait.until(ec.number_of_windows_to_be(2))
        # 切换句柄到新页面
        self.switch_windows(-1)
        # 点击章节管理
        self.wait_locat(*KEY_WORD_VALUE3.CHAPTER_BUTTON).click()
        # 跳转新页面，切换句柄
        self.switch_windows(-1)
        sleep(2)
        # 点击新建章节 ,由于点击拿不到元素，这里直接打开添加章节页面 url写死
        # self.wait_locat(*KEY_WORD_VALUE3.CREATE_CHAPTER).click()
        # sleep(2)
        self.open_new_browser(KEY_WORD_VALUE3.ADD_URL, KEY_WORD_VALUE3.OPEN_TYPE)
        sleep(2)
        # 输入章节标题+内容点击提交
        self.wait_locat(*KEY_WORD_VALUE3.CREATE_CHAPTER_TITLE).send_keys(title)
        self.wait_locat(*KEY_WORD_VALUE3.CREATE_CHAPTER_CONTENT).send_keys(content)
        # 选择是否收费
        self.wait_locat(*KEY_WORD_VALUE3.CONTENT_IS_CHARGE).click()
        # 点击提交按钮
        self.wait_locat(*KEY_WORD_VALUE3.CHAPTER_ADD_SUBMIT_BUTTON).click()
