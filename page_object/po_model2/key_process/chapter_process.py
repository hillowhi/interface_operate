from time import sleep

from selenium import webdriver

from page_object.po_model2.key_word_class_po3 import KeyWordWebClass
from page_object.po_model2.key_word_list.KEY_WORD_VALUE2 import *


class ChapterProcess(KeyWordWebClass):
    # 封装登录流程
    def login(self):
        # self.driver = webdriver.Chrome()
        self.open_browser(URL_LOGIN)
        self.find_el(*LOCATOR_USERNAME).send_keys(USERNAME_AUTHOR)
        self.find_el(*LOCATOR_PASSWORD).send_keys(PASSWORD_AUTHOR)
        self.find_el(*LOCATOR_LOGIN_BUTTON).click()

    # 新增章节流程
    def chapter_add_process(self):
        # 基于已经登陆的状态 打开作家专区页面
        self.open_new_browser(URL_AUTHOR, OPEN_TYPE)
        # 定位到章节管理
        self.wait_locat(CHAPTER_BUTTON_NAME, CHAPTER_BUTTON_VALUE).click()
        sleep(2)
        # 打开了新页面 跳到新页面 句柄切换(这里能不能用一个方法 如果有新页面就跳新页面，click里面封一个sitch_windows方法)
        self.switch_windows(-1)
        print(self.driver.current_url)
        # 跳到章节列表页，点击新增按钮
        self.wait_locat(CREATE_CHAPTER_NAME, CREATE_CHAPTER_VALUE).click()
        # 这里跑不通 查不出原因 换一个方式
        # self.find_el(*CREATE_CHAPTER).click()
        sleep(2)
        # 跳转到新增章节页面
        self.switch_windows(-1)
        # 输入标题&内容
        self.find_el(*CREATE_CHAPTER_TITLE).send_keys(TEST_TITLE)
        self.find_el(*CREATE_CHAPTER_CONTENT).send_keys(TEST_CONTENT)
        # 选择是否收费 这里选择 是
        self.find_el(*CONTENT_IS_CHARGE).click()
        # 点击提交
        self.find_el(*CHAPTER_ADD_SUBMIT_BUTTON).click()
        sleep(2)








