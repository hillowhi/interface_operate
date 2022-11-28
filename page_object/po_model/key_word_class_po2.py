"""
封装工具类示例

"""
import time

from selenium.webdriver.common.by import By


class KeyWordWeb():
    # 因为conftest里面定义了一个浏览器 所以这里不需要定义浏览器driver对象，
    # 只需要接收driver 然后运用就好 所以需要在构造函数里接收一下这个driver对象
    def __init__(self, driver):
        self.driver = driver

    # 打开浏览器
    def open_browser(self, url):
        self.driver.get(url)

    def find_el(self, name, value):
        el = self.driver.find_element(name, value)
        # 调用locator_station 方法 将定位元素展示出来
        # 这里调用下面封装好的高亮方法 就不需要在key_page_object_test里面调用
        self.locator_station(el)
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
