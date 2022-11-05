import jsonpath
import requests

# 登录拿到token
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
login_r = requests.post(url_login, json=login_data, params=params)
login_response = login_r.json()
# hea = login_r.headers
# print(hea)
# print(type(hea))
# print(login_r.text)
token_list = jsonpath.jsonpath(login_response, "$.data..token")
token = token_list[0]
# 添加到购物车
params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}
shop_cart_data = {
    "goods_id": 2,
    "stock": 1,
    "spec": ""
}
url_add_shopcart = "http://shop-xo.hctestedu.com/index.php?s=api/cart/save"
r_shop_cart = requests.post(url_add_shopcart, params=params, json=shop_cart_data)
resopnse_add = r_shop_cart.text
# print(resopnse_add)
response = r_shop_cart.json()
code = jsonpath.jsonpath(response, "$.code")
add_cart_message = jsonpath.jsonpath(response, "$.msg")
# print(code)
# print(type(code[0]))
assert 0 == code[0]
assert "加入成功" == add_cart_message[0]

# 查询购物车 校验是否添加成功
url_cart_list = "http://shop-xo.hctestedu.com/index.php?s=api/cart/index"
login_cart_r = requests.post(url_cart_list, params=params)
# print(login_cart_r.text)
login_cart_response = login_cart_r.json()
goods_id = jsonpath.jsonpath(login_cart_response, "$.data.data..[goods_id]")
# print(goods_id)
# print(type(goods_id))
# stock = jsonpath.jsonpath(login_cart_response, "$.data.data..stock")
# print(goods_id)
for a in goods_id:
    print(type(a))
    # print(type(shop_cart_data))
    print(type(shop_cart_data["goods_id"]))
    if a == str(shop_cart_data["goods_id"]):
        print("添加成功")
    else:
        print("购物车添加失败")