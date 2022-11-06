import allure

from login_testcase.key_api.request_package import InterfaceOperate


@allure.title("登陆用例01-登录成功")
def test01():
    key = InterfaceOperate()
    params = {
        "application": "app",
        "application_client_type": "weixin"
    }
    url_login = "http://shop-xo.hctestedu.com/index.php?s=api/user/login"
    login_data = {
        "accounts": "lihuanhuan",
        "pwd": "huange521",
        "type": "username"
    }
    post_res = key.post(url_login, json=login_data, params=params)
    response1 = key.res_request(post_res)