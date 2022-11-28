"""
> 类似于setup前置函数 测试用例在调用时如果参数里引用了fixture函数
> 则自动调用该fixture函数，fixture函数不用导入 可以直接引用

"""
import jsonpath
import pytest
import requests


@pytest.fixture
def pytest_fixture():
    property_message_box = []
    url = "https://app-dev.mklij.com/fangyuan-api/property/queryPropertyList"
    data = {"client": "ios",
            "pageNo": "1",
            "pageSize": "8",
            "propertyQueryTypeEnum": "SALE",
            "querySourceType": "liebiaoye",
            "channel": "ershoufang",
            "cityId": "2",
            "cityName": "上海"}
    response_list = requests.post(url, json=data)
    response_data = response_list.json()
    print(response_list.status_code)
    property_no = jsonpath.jsonpath(response_data, "$.data..data..propertyNo")
    property_message_box.append(property_no)
    estate_name_response = jsonpath.jsonpath(response_data, "$.data..data..estateName")
    property_message_box.append(estate_name_response)
    return property_message_box


def test_fixture01(pytest_fixture):
    estate_name_list = []
    url = "https://app-dev.mklij.com/fangyuan-api/app/property/propertyDetailByNo"
    for i in pytest_fixture[0]:
        print(i)
        data_detail = {
            "cityId": "2",
            "cityName": "上海市",
            "propertyNo": i,
            "sourceType": "SALE"
        }
        detail_response = requests.post(url, data_detail)
        detail_data_response = detail_response.json()
        estate_name = jsonpath.jsonpath(detail_data_response, "$.data..estateName")
        estate_name_list.append(estate_name)
        detail_code = jsonpath.jsonpath(detail_data_response, "$..code")
        # assert 200 == int(detail_code)


if __name__ == '__main__':
    pytest.main(['-s'])
