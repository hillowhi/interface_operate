import jsonpath as jsonpath
import requests

data = {
    "empNumber": "012682",
    "empPassword": "123456",
    "imgCode": ""
}
r = requests.post("https://broker-dev.mklij.com/broker-api/loginByEmpNoOrPwd", json=data)
dic_response = r.json()
# print(type(dic_response))

em = jsonpath.jsonpath(dic_response, "$.data.employeeDTO..levelName")
print(em)
print(type(em))

"""
> $表示从根节点开始

> .表示获取子节点

> ..表示获取所有符合条件的内容

> *表示所有元素节点

> []表示迭代器的标示

>[,]表示多个结果的选择

>?()表示过滤操作

>@表示当前节点
"""
