"""
关键字变量统一管理文件 变量一般都大写
"""
from selenium.webdriver.common.by import By

"""
最好标注一下 关键字所应用的业务场景 方便后续的搜索
比如以下关键字用于读书屋的登录
"""
# 读书屋首页登录
# 首页url
URL = "http://novel.hctestedu.com/"
# 登录页url
URL_LOGIN = "http://novel.hctestedu.com/user/login.html"
# 作家专区url
URL_AUTHOR = "http://novel.hctestedu.com/author/index.html"

# 账号密码
USERNAME = "15224880595"
PASSWORD = "huange521"

# 作家专区账号密码
USERNAME_AUTHOR = "18894687777"
PASSWORD_AUTHOR = "123456"

# 登录页面定位
LOCATOR_LOGIN = ["xpath", "//a[text()='登录']"]
LOCATOR_USERNAME = ["xpath", "//input[@placeholder='手机号码']"]
LOCATOR_PASSWORD = ["xpath", """//input[@placeholder="密码"]"""]
LOCATOR_LOGIN_BUTTON = ["xpath", """//input[@value="登录"]"""]

# 书籍详情
BOOK_DETAIL_URL = "http://novel.hctestedu.com/book/199.html"
OPEN_TYPE = "tab"
# 获取动态轮播图的定位和点击按钮定位
move_button_path = "//li/img[@alt ='史上最强大皇子']"
CLICK_BUTTON = ["xpath", "//dd[@class='on']"]

# 首页搜索框
SEARCH_BOX = ["xpath", "//input[@class='s_int']"]
TEXT_NOVEL = "宫之海"
# select框
SELECT_URL = "https://sahitest.com/demo/selectTest.htm"
SELECT_ELEMENT = ["id", "s3Id"]
# SELECT_NAME = 'xpath'
# SELECT_VALUE = "//select[@id='s3Id']"
SELECT_TEXT = "o3"
SELECT_WAY = "text"
SELECT_OBJECT_VALUE = ["id", "s3Id", "text", "o3"]
# 回车键发起搜索
ENTER_KEY = "ENTER"
# 作家专区
# CHAPTER_BUTTON = ['xpath', "//a[text()='章节管理  ']"] 这个写法有点奇怪
CHAPTER_BUTTON = ["xpath", "//a[@class='redBtn']"]
CHAPTER_BUTTON_NAME = "xpath"
CHAPTER_BUTTON_VALUE = "//a[@class='redBtn']"
# AUTHOR_AREA里该路径可以定位到两个元素 所以需要用find_elements[0]
AUTHOR_AREA1 = ["xpath", "//li//a[text()='作家专区']"]
AUTHOR_AREA = ["link_text", "作家专区"]

# 新建章节xpath路径
CREATE_CHAPTER = ["xpath", "//div[@class='tc']//a[text()='新建章节']"]
CREATE_CHAPTER_NAME = "xpath"
CREATE_CHAPTER_VALUE = "//div[@class='tc']//a[text()='新建章节']"

# 这里引用了一个方法self.wait_locat(*CREATE_CHAPTER).click()
# 里面的locat参数把定位方式和路径做了一个打包，所以不能写成一个list 要分开写

# 新增章节url
ADD_URL = 'http://novel.hctestedu.com/author/content_add.html?indexCount=5&bookId=424'
# 新增章节标题
CREATE_CHAPTER_TITLE = ["xpath", "//input[@id='bookIndex']"]
# 测试标题(希望后面可以学会直接读取表格)
TEST_TITLE = "执着"
TEST_CONTENT = "每个夜晚来临的时候孤独总在我左右每个黄昏心跳的等候是我无限的温柔每次面对你的时候不敢看你的双眸在我温柔的笑容背后有多少泪水哀愁不管时空怎么转变"

# 新增章节内容
CREATE_CHAPTER_CONTENT = ["xpath", "//textarea[@name ='bookContent']"]
# 是否收费单选按钮
CONTENT_IS_CHARGE = ["xpath", "//input[@value='1']"]
# 新增章节提交按钮
CHAPTER_ADD_SUBMIT_BUTTON = ["xpath", "//input[@value='提交']"]
# 章节列表的第一个章节 校验新增用
FIRST_CHAPTER = ["xpath", "//tr[@class='book_list'][1]//td[1]"]

# 章节列表
# 章节名称
# CHAPTER_NAME =""
# CHAPTER_NAME ="""f"//tr[@class='book_list']//td[contains(text(),{value})]""""
# 章节列表里第一个章节的删除按钮
CHAPTER_DELETE = ['xpath', "//tr[@class='book_list']//td//a[2]"]
# 删除确认弹框按钮
ALTER_DELETE_BUTTON = ['xpath', "//a[text()='确定']"]
ENSURE_BUTTON = ['xpath', "//a[@class='layui-layer-btn0']"]
# 获取章节列表第一个章节的章节名称 title
CHAPTER_LIST_FIREST = ['xpath', "//tr[@class='book_list'][1]//td"]
