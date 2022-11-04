import requests

# data = {
#     "empNumber": "012682",
#     "empPassword": "123456",
#     "imgCode": ""
# }

# r = requests.post("https://broker-dev.mklij.com/broker-api/loginByEmpNoOrPwd", json=data)
# print(type(r))
# print(r)
# print(r.status_code)
# print("--------------------------------------------------------------------------")
# print(r.content)

# print(r.text)
# print(r.url)
# token = r["data"]
# print(token)
# print(r.encoding)
# 只有字典格式的返回值才可以通过关键字取值 即使返回值是json格式 返回的数据类型依旧可能是string 所以必须确定返回值类型
# response = r.json()
# print(response)
# print(type(r.json()))
# print(r.text)
# print(type(r.text))
# print(r.content.decode(encoding="UTF-8"))
# print(type(r.content.decode(encoding="UTF-8")))

# print(r.raw)
# print(r.raw.read(10))
# print(r.iter_content)

# with open(r.iter_content, "wb") as fd:
#     for chunk in r.iter_content(chunk_size=128):
#         fd.write(chunk)

# login_data = {
#     "username": "lihh",
#     "password": "huange521"
# }
# url = ("http://shop-xo.hctestedu.com/index,php?s=api/user/login")
# print(r.status_code)
# print(r.text)
# print(r.content.decode(encoding="UTF-8"))
# print(response)
# print(type(response))
# print(r.request.url)
# token = response["data"]["employeeDTO"]["token"]
# print(token)
# assert 200 == response["code"]

try:
    data = {
        "empNumber": "01268",
        "empPassword": "123456",
        "imgCode": ""
    }

    r = requests.post("https://broker-dev1.mklij.com/broker-api/loginByEmpNoOrPwd", json=data)
    print(r)
    print(type(r))
    response = r.json()
    # print(type(response))
    # token = response["data"]["employeeDTO"]["token"]
    # print(token)
    assert 200 == response["code"]
except:
    # pass
    r.raise_for_status()

data = {
    "empNumber": "012682",
    "empPassword": "123456",
    "imgCode": ""
}

r = requests.post("https://broker-dev.mklij.com/broker-api/loginByEmpNoOrPwd", json=data, timeout=2)
response = r.json()
# token = response["data"]["employeeDTO"]["token"]
# print(token)
assert 200 == response["code"]
print(response["code"])
