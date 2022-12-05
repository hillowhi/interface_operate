'''
类构造函数的继承
'''
# class Plant:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_age(self):
#         return self.age
#
#
# class Fruit(Plant):
#     def get_name_and_age(self, prefix):
#         login = Login(self.name)
#         text = login.get_text()
#         return f"{prefix}, {text}, {self.name}, {self.age}"
#
#
# apple = Fruit("apple", 100)
# temp = apple.get_name_and_age("===")
# print(temp)
import requests

'''
案例
'''


# class A:
#     def __init__(self, a):
#         a += a
#
#
# class B(A):
#     def __init__(self, e, b):
#         super().__init__(e)
#         # super().__init__(a) 就是引用父类构造函数 定义自己类特有的参数
#         # 并保留父类里定义好的变量
#         self.c = b
#
#     def fun_b(self, b):
#         b += 1
#
#
# class C(A):
#     b = B(3, 4)
#     f = b.fun_b(5)
#
#
# c = C(1, 1)

# 下载重试机制:设置重试次数
# def loading_retry(url, n):
#     for i in range(0, n):
#         try:
#             # print(1)
#             requests.get(url)  # 如果这一步报错，那么这部代码下面的都不会走
#             print('如果上一步报错，那么这步将不会运行')
#             break
#         except requests.exceptions.ConnectionError:
#             print(f"重试第{i + 1}次")
#
#
# loading_retry('https://baidu1.com/', 3)

# 下载重试机制:无次数限制，重试到成功为止
def loading_retry_success(url):
    while True:
        try:
            # print(1)
            requests.get(url)  # 如果这一步报错，那么这部代码下面的都不会走
            print('如果上一步报错，那么这步将不会运行')
            break
        except requests.exceptions.ConnectionError:
            print('路径异常')


loading_retry_success('https://baidu1.com/')
