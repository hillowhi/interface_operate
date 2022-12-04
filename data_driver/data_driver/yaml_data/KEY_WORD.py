# yaml 文件需要的参数
YAML_LOGIN = 'http://novel.hctestedu.com/user/login.html'
PAY_MONEY_PAGE = 'http://novel.hctestedu.com/pay/index.html'

# 登录后跳转页面的用户名定位
LOGIN_USERNAME = ['xpath', "//span//a[1]"]
LOGIN_USERNAME1 = 'link_text'

# 登录账号密码
PAY_USERNAME = '15224880595'
PAY_PASSWORD = 'huange521'

# 充值按钮
PAY_BUTTON = ['xpath', "//li[4]//a"]
# 充值页面 充值金额按钮
PAY_MONEY = ['xpath', "//li[@vals][3]"]
