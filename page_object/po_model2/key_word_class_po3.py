"""
封装工具类示例

"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_object.po_model2.key_word_list.KEY_WORD_VALUE2 import *


class KeyWordWebClass():
    # 因为conftest里面定义了一个浏览器 所以这里不需要定义浏览器driver对象，
    # 只需要接收driver 然后运用就好 所以需要在构造函数里接收一下这个driver对象
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        # 这里初始化一个wait 对象，用于后面打开浏览器校验当前的url是否正确打开确保后续操作页面准确
        # 如果觉得打出来自带方法太麻烦可以先初始化一个driver对象，写完再删掉
        # self.driver = webdriver.Chrome()

    # 打开浏览器
    def open_browser(self, url):
        self.driver.get(url)
        # 判断当前页面url是否正确
        self.wait.until(ec.url_contains(url))

    # 用新页面打开地址路径
    def open_new_browser(self, open_url, open_type):
        if open_type == 'tab' or open_type == '':
            self.driver.switch_to.new_window('tab')
        else:
            self.driver.switch_to.new_window('window')
        # self.driver.get(open_url)
        # 嘿 我真聪明( •̀ ω •́ )✧
        self.open_browser(open_url)

    # 查找元素定位
    def find_el(self, name, value):
        el = self.driver.find_element(name, value)
        # 调用locator_station 方法 将定位元素展示出来
        # 这里调用下面封装好的高亮方法 就不需要在key_page_object_test里面调用
        # self.locator_station(el)
        return el

    # 对定位元素高亮展示 ele指被定位元素
    def locator_station(self, ele):
        # argument[0]指的是第一个参数，即ele,然后arguments[1] 指的是第二个参数 "broder:2px solid green"
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                   ele, "border:6px solid green")

    """
    不知道为什么这段定位方法没有生效，代码可以运行起来
    妈的 单词拼错了 可恶(〃＞目＜)！！！！！！！！！！！
    execute 少了个e!!!!!!!!!!!(ˉ▽ˉ；)...
    """

    # 窗口切换函数的封装
    def switch_windows(self, n):
        # 切换到原始页面，即第一个页面 n=0
        # 切换到最新的一个窗口 n=-1
        # 切换到第二个页面 n=1
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[n])
        # print(self.driver.title)
        # 打印一下当前页面的title
        return self.driver

    # 鼠标点击并悬停操作封装，用于处理会变化的动态元素 轮播图等
    def mouse_hold_click(self, move_button_path, click_button):
        button_on = self.driver.find_element(By.XPATH, move_button_path)  # 不明白为什么用findelements 为了兼容性更好吗,我来改一下
        action = ActionChains(self.driver)  # 初始化一个action对象
        action.click_and_hold(button_on).perform()  # .perform()等于提交前面的鼠标操作
        self.find_el(*CLICK_BUTTON).click()

    # 先清空默认文本，再输入，enter键搜索 适用于搜索框
    def clear_send_search(self, name, value, txt):
        # self.driver.find_element(By.XPATH, search_box_value).clear()
        self.find_el(name, value).clear()
        self.find_el(name, value).send_keys(txt + Keys.ENTER)

    # select 选择器三种选中定位 by_value by_text, by_index(索引)
    '''
    https://sahitest.com/demo/selectTest.htm  select选择器测试连接
    '''

    def select_by_any(self, name, value, by_way, text):
        select_element = self.find_el(name, value)
        select_object = Select(select_element)
        if by_way == 'value':  # 值选择
            select_object.select_by_value(text)
        elif by_way == 'index':  # 索引选择
            select_object.select_by_index(text)
        elif by_way == 'text':  # 文本选择text
            select_object.select_by_visible_text(text)
        else:
            print('请输入value，index，text任意一种选择方式')
