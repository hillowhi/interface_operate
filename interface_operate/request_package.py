import jsonpath
import requests
import allure

"""
错误代码
"""


# def request_type(request_type):
#     if request_typue == "get":
#         def get(url, params=None, **kwargs):
#             return requests.get(url=url, params=params, **kwargs)
#     elif request_type == "post":
#         def post(self, url, params=None, json=None, **kwargs):
#             return requests.post(url=url, json=json, params=params, **kwargs)
#
#
# def assert_func(path, type_assert, message):
#     request_r = request_type(type_assert)
#     request_response = request_r.json()
#     assert_message = jsonpath.jsonpath(request_response, path)
#     assert message == assert_message


"""
依次创建post get请求函数
"""


class InterfaceOperate:
    @allure.step("开始get请求")
    def get(self, url, params, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    @allure.step("开始post请求")
    def post(self, url, params=None, json=None, **kwargs):
        return requests.post(url=url, json=json, params=params, **kwargs)

    @allure.step("开始获取请求结果")
    def res_request(self, request_r):
        response_request = request_r.json()
        return response_request

    @allure.step("开始断言")
    def assert_func(self, path, response_request1, expect_response):
        assert_message = jsonpath.jsonpath(response_request1, path)
        assert expect_response == assert_message[0]


def main():
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
    assert_request1 = key.assert_func("$..msg", response1, "登录成功")


if __name__ == "__main__":
    main()

