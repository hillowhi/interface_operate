"""
关键字变量统一管理文件 变量一般都大写
"""

"""
最好标注一下 关键字所应用的业务场景 方便后续的搜索
比如以下关键字用于读书屋的登录
"""
# 读书屋首页登录
# 首页url
URL = "http://novel.hctestedu.com/"
# 账号密码
USERNAME = "15224880595"
PASSWORD = "huange521"

# 登录页面定位
LOCATOR_LOGIN = ['xpath', "//a[text()='登录']"]
LOCATOR_USERNAME = ['xpath', """//input[@placeholder="手机号码"]"""]
LOCATOR_PASSWORD = ['xpath', """//input[@placeholder="密码"]"""]
LOCATOR_LOGIN_BUTTON = ['xpath', """//input[@value="登录"]"""]

# 书籍详情
BOOK_DETAIL_URL = 'http://novel.hctestedu.com/book/199.html'
OPEN_TYPE = 'tab'
# 获取动态轮播图的定位和点击按钮定位
move_button_path = "//li/img[@alt ='史上最强大皇子']"
CLICK_BUTTON = ['xpath', "//dd[@class='on']"]

# 首页搜索框
SEARCH_BOX = ['xpath', "//input[@class='s_int']"]
TEXT_NOVEL = '宫之海'
# select框
SELECT_URL = 'https://sahitest.com/demo/selectTest.htm'
SELECT_ELEMENT = ['id', "s3Id"]
# SELECT_NAME = 'xpath'
# SELECT_VALUE = "//select[@id='s3Id']"
SELECT_TEXT = 'o3'
SELECT_WAY = 'text'
SELECT_OBJECT_VALUE = ['id', "s3Id", 'text', 'o3']
