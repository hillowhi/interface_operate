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

'''
案例
'''


class A:
    def __init__(self, a):
        a += a


class B(A):
    def __init__(self, e, b):
        super().__init__(e)
        # super().__init__(a) 就是引用父类构造函数 定义自己类特有的参数
        # 并保留父类里定义好的变量
        self.c = b

    def fun_b(self, b):
        b += 1


class C(A):
    b = B(3, 4)
    f = b.fun_b(5)


c = C(1, 1)
