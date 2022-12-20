'''
类构造函数的继承
'''
# class Plant:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_age(self):
#         return self.age
#
#
# class Fruit(Plant):
#     def get_name_and_age(self, prefix):
#         login = Login(self.name)
#         text = login.get_text()
#         return f"{prefix}, {text}, {self.name}, {self.age}"
#
#
# apple = Fruit("apple", 100)
# temp = apple.get_name_and_age("===")
# print(temp)
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

'''
案例
'''

# class A:
#     def __init__(self, a):
#         a += a
#
#
# class B(A):
#     def __init__(self, e, b):
#         super().__init__(e)
#         # super().__init__(a) 就是引用父类构造函数 定义自己类特有的参数
#         # 并保留父类里定义好的变量
#         self.c = b
#
#     def fun_b(self, b):
#         b += 1
#
#
# class C(A):
#     b = B(3, 4)
#     f = b.fun_b(5)
#
#
# c = C(1, 1)

'''
异常处理重试机制
'''


# 下载重试机制:设置重试次数
# def loading_retry(url, n):
#     for i in range(0, n):
#         try:
#             # print(1)
#             requests.get(url)  # 如果这一步报错，那么这部代码下面的都不会走
#             print('如果上一步报错，那么这步将不会运行')
#             break
#         except requests.exceptions.ConnectionError:
#             print(f"重试第{i + 1}次")
#
#
# loading_retry('https://baidu1.com/', 3)

# 下载重试机制:无次数限制，重试到成功为止
# def loading_retry_success(url):
#     while True:
#         try:
#             # print(1)
#             requests.get(url)  # 如果这一步报错，那么这部代码下面的都不会走
#             print('如果上一步报错，那么这步将不会运行')
#             break
#         except requests.exceptions.ConnectionError:
#             print('路径异常')
#
#
# loading_retry_success('https://baidu1.com/')

def get_price_jd(keyword):
    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    wait = WebDriverWait(driver, 3)
    driver.get("https://jd.com")
    # driver.find_element(By.ID, "key").send_keys(keyword)
    driver.find_element(By.ID, "key").send_keys(keyword + Keys.ENTER)
    # 当点击按钮处于可被点击状态时再去运行点击操作
    # wait.until(ec.element_to_be_clickable(('xpath', "//button[@class='button']")))
    # driver.find_element('xpath', "//button[@class='button']").click()
    # 定位到底部的 //p//a[text()='关于我们'] 用Actionchains 需要定位到底部的关于我们保证页面全部加载完成才能拿到页面所有值
    # #这个方法找不到，这个方法只能用于页面元素处于当前可见窗口范围时
    # action = ActionChains(driver)
    # action.move_to_element(['xpath', "//p//a[text()='关于我们']"])

    # 试一下这个方法 ok的
    # driver.execute_script("var q=document.documentElement.scrollTop=10000")
    # sleep(2)

    # 批量获取商品信息 这里获取到的是元素本身 需要.text获取元素的文本信息，可以用关键字+商品信息拼接
    '''
    <em>【京东之家】Apple 苹果<font class="skcolor_ljg">14pro</font>（A2892）<font class="skcolor_ljg">iphone14pro</font> 
    A16芯片 5G手机 暗紫色 256G 套装一：搭配90天碎屏保障</em>
    '''
    # 这里需要拿到商品名,presence_of_element_located如果元素已经被加载了就去取数据 用这个方法保证页面加载完成
    wait.until(ec.presence_of_element_located(('xpath', "//div[@class='p-name p-name-type-2']//em")))
    goods_name_list = driver.find_elements('xpath', "//div[@class='p-name p-name-type-2']//em")
    # 批量获取产品图片，这里需要拿元素里面src里面包的图片路径
    '''
    元素示例：
    <img width="220" height="220" data-img="1" data-lazy-img="done" source-data-lazy-img="" 
    src="//img14.360buyimg.com/n7/jfs/t1/83908/12/22096/71048/6324a434Ebc7e529e/19f19b2b02984471.jpg">
    '''
    # sleep(2)

    # href
    # wait.until(ec.presence_of_element_located(('xpath', "//img[@width='220' and @height = '220' and @data-img='1']")))
    img_list = driver.find_elements('xpath', "//img[@width='220' and @height = '220' and @data-img='1']")
    goods_link = driver.find_elements('xpath', "//img[@width='220' and @height = '220' and @data-img='1']/..")
    # 批量获取商品价格
    '''
    元素代码示例：
    <i data-price="10060059831744">9599.00</i>
    '''
    sleep(1)
    price_list = driver.find_elements('xpath', "//strong//i")
    test_list = []

    for i in range(0, len(goods_name_list)):
        goods_dict = {}
        goods_dict["platform"] = 'JD'
        goods_dict["good_name"] = goods_name_list[i].text
        goods_dict["good_price"] = float(price_list[i].text)
        goods_dict["good_img"] = img_list[i].get_attribute('src')
        goods_dict["good_link"] = goods_link[i].get_attribute('href')
        test_list.append(goods_dict)
    print(test_list)
    return test_list


'''
结果
[{goodsname:14pro,good_pricer:1234,good_img:"https://ueuuefhh"},
{goodsname:14pro,good_pricer:1234,good_img:"https://ueuuefhh"}]
'''

if __name__ == '__main__':
    keyword = 'iphone14pro'
    get_price_jd(keyword)
