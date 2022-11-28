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


class KeyApiOpTwo(KeyWordWebClass):
    # 类的继承KeyWordWeb是KeyApiOp的父类
    # 所以KeyApiOp不需要再声明一个浏览器对象
    def op_login(self, url, username, password):
        self.open_browser(url)
        # 写一段校验证明这个url确实打开了 用定位到指定元素去校验 用显示等待
        # wait = WebDriverWait(self.driver, 10)
        # 校验页面是否出现登录字样判断页面是否加载正确
        self.wait.until(ec.text_to_be_present_in_element((By.XPATH, "//a[text()='登录']"), "登录"))
        # 用不定长的参数*args 获取参数值の写法  奈斯！我真棒！
        self.find_el(*LOCATOR_LOGIN).click()
        self.find_el(*LOCATOR_USERNAME).send_keys(username)
        self.find_el(*LOCATOR_PASSWORD).send_keys(password)
        self.find_el(*LOCATOR_LOGIN_BUTTON).click()

        # 从key_word_list文件夹下的KEY_WORD_VALUE2文件里面读取变量 LOCATOR_LOGIN是一个list 所以需要分别读取字段
        # self.find_el(KEY_WORD_VALUE2.LOCATOR_LOGIN[0], KEY_WORD_VALUE2.LOCATOR_LOGIN[1]).click()
        # self.find_el(KEY_WORD_VALUE2.LOCATOR_USERNAME[0], KEY_WORD_VALUE2.LOCATOR_USERNAME[1]).send_keys(username)
        # self.find_el(KEY_WORD_VALUE2.LOCATOR_PASSWORD[0], KEY_WORD_VALUE2.LOCATOR_PASSWORD[1]).send_keys(password)
        # self.find_el(KEY_WORD_VALUE2.LOCATOR_LOGIN_BUTTON[0], KEY_WORD_VALUE2.LOCATOR_LOGIN_BUTTON[1]).click()

        # 线性获取定位元素の写法
        # self.find_el(By.XPATH, """//input[@placeholder="手机号码"]""").send_keys(username)
        # self.find_el(By.XPATH, """//input[@placeholder="密码"]""").send_keys(password)
        # self.find_el(By.XPATH, """//input[@value="登录"]""").click()
        sleep(2)
        # 确保登陆完成 找一个成功登录后出现的元素作为条件
        wait_login = WebDriverWait(self.driver, 6)
        wait_login.until(ec.text_to_be_present_in_element((By.XPATH, """//a[@class="mr15"]"""), username))
        # /(ㄒoㄒ)/~~ 这个括号！！！好烦 找了好久的问题

        # 再封一个流程 打开新页面
        self.open_new_browser(BOOK_DETAIL_URL, OPEN_TYPE)
        # 切换窗口 0 ，-1，1
        self.switch_windows(0)
        sleep(2)
        self.mouse_hold_click(move_button_path, CLICK_BUTTON)
        self.switch_windows(1)

        # 从首页搜索框搜索宫之海小说
        self.clear_send_search(*SEARCH_BOX, TEXT_NOVEL)
        sleep(2)
