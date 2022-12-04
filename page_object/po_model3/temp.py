# class A:
#     def __init__(self, attr):
#         self.abc = attr
#
#     def __call__(self, a, b):
#         return a + b
#
#     def f(self):
#         print("f function")
#
#
# class B(A):
#     def __init__(self, attr2, attr3):
#         # super().__init__(attr2)
#         self.efg = attr3
#
#     def f2(self):
#         print("f2 function")
#
#
# b = B(2, 3)
package_list = [1, 2]


def unpack():
    print(tuple(*package_list))


a = unpack()
