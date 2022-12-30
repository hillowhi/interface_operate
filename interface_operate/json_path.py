from time import sleep

import jsonpath as jsonpath
import requests

data = {
    "empNumber": "012682",
    "empPassword": "123456",
    "imgCode": ""
}
login_r = requests.post("https://broker-dev.mklij.com/broker-api/loginByEmpNoOrPwd", json=data)
dic_response = login_r.json()
# print(type(dic_response))

em = jsonpath.jsonpath(dic_response, "$.data.employeeDTO..levelName")
token = jsonpath.jsonpath(dic_response, "$..token")
print(token)
print(type(token))
print(token[0])
token1 = str(token)
print(token1)
# 有没有简单的办法
# str2 = token1.strip("['")
# str3 = str2.strip("']")
# print(str3)
# print(type(token1))
# print(em)
# print(type(em))

# str1 = token1.split("[", -1)
# print(str1[1])

headers = {
    "authorization": token1
}
property_list = {
    "privy": "公盘",
    "propertyQueryTypeEnum": "ALL",
    "sortFieldAppEnum": "last_follow_date",
    "sortTypeAppEnum": "ASC",
    "pageNo": 1,
    "pageSize": 10,
    "fangYuanJianLouFlag": "false"
}
property_r = requests.post("https://broker-dev.mklij.com/broker-api/fangyuan/property/queryPropertyList",
                           json=property_list, headers=headers)
property_response = property_r.json()
print(property_response)

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
