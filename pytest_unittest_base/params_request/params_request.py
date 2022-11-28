"""
首先 先来点简单的单参数化
@pytest.mark.parametrize("形参1,形参2",[(‘123’,'456'),(‘113’,'456'),(‘223’,'456')])
"""
# 错误代码  目的：将登录函数前置化 调用用例的时候直接code返回断言
import jsonpath
import pytest
import requests

#
#
# class Request:
#     def post_return_code(self, url, json=None, params=None, **kwargs):
#         request_res = requests.post(url, json=json, params=params, **kwargs)
#         response_data = request_res.json()
#         return_code = response_data.code[0]
#         return return_code
#
#
# @pytest.mark.parametrize('empNumber, empPassword',
#                          [('012682', '123456'), ('012686', '123456'), ('012682', '12345678')])
# class setup_and_teardown:
#     @classmethod
#     def setup_function(cls):
#         url = "https://broker-dev.mklij.com/broker-api/loginByEmpNoOrPwd"
#         request_setup = Request()
#         return request_setup.post_return_code()
#
#
# def test_login():
#     cla_code = setup_and_teardown()
#     assert cla_code() == 200
#
#
# if __name__ == '__main__':
#     pytest.main(['-s'])

# class Request:
#     def post_return_code(self, url, json=None, params=None, **kwargs):
#         requests.post(url, json=json, params=params, **kwargs)


# @pytest.mark.parametrize('url,json', [('https://broker-dev.mklij.com/broker-api/loginByEmpNoOrPwd',
#                                        {
#                                            "empNumber": "012682",
#                                            "empPassword": "123456"
#                                        }
#                                        ), ('https://broker-dev.mklij.com/broker-api/loginByEmpNoOrPwd',
#                                            {
#                                                "empNumber": "012682",
#                                                "empPassword": "12345678"
#                                            }
#                                            )])
# 为什么不能这么写
# def test_login():
#     request = Request()
#     request.post_return_code(url=None, json=None)
#     return

# @pytest.mark.parametrize('',''['','',])

# 参数函数化示例
# url = 'https://broker-dev.mklij.com/broker-api/loginByEmpNoOrPwd'


# def get_data():
#     login_data = [('012682', '12333'), ('012682', '123456'), ('012682', '78888')]
#     return login_data
"""
多参数传参模式
"""

# @pytest.mark.parametrize('url,json', [('https://broker-dev.mklij.com/broker-api/loginByEmpNoOrPwd',
#                                        {
#                                            "empNumber": "012682",
#                                            "empPassword": "123456"
#                                        }
#                                        ), ('https://broker-dev.mklij.com/broker-api/loginByEmpNoOrPwd',
#                                            {
#                                                "empNumber": "012682",
#                                                "empPassword": "12345678"
#                                            }
#                                            )])
#
# def test_login(url, json):
#     r = requests.post(url, json=json)
#     r_response = r.json()
#     code = jsonpath.jsonpath(r_response, "$..code")
#     assert 200 == code[0]
#
# if __name__ == '__main__':
#     pytest.main(['params_request.py', '--html=params_report.html'])

"""
参数函数化
"""


def get_data():
    login_data = [({"empPassword": "123456", "empNumber": "012682"}),
                  ({"empPassword": "123456", "empNumber": "012688"})]
    return login_data


@pytest.mark.parametrize('data', get_data())
def test_login(data):
    print(data)
    url = 'https://broker-dev.mklij.com/broker-api/loginByEmpNoOrPwd'
    r = requests.post(url, data)
    r_data = r.json()
    print(jsonpath.jsonpath(r_data, "$..code"))


if __name__ == '__main__':
    pytest.main(['-s', 'params_request.py'])
