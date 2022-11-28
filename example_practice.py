# ec模块小测验

# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
#
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# result = ec.url_contains('https://www.baidu.com/')
# result1 = ec.title_is('百度一下，你就知道')
# print(result1(driver))
# print(result(driver))
# print(result1)
#
#
# # 闭包の写法
# def title_is(title: str):
#     def _predicate(driver):
#         return driver.title == title
#
#     return _predicate
#
#
# # 装饰器
# def title_is2(func):
#     print('开始咯')
#
#     def fun2(*arg):
#         return func(*arg)
#
#     return fun2
#
#
# @title_is2
# def fun1(title):
#     return (driver.title == title)
#
#
# if __name__ == "__main__":
#     a = fun1('百度一下，你就知道')
#     if a:
#         print('标题相等')

# 装饰器
# def do_twice(func):
#     print("Something is happening before the function is called.")
#
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#
#     return wrapper_do_twice
#
#
# @do_twice
# def greet(name):
#     print(f"Hello {name}")
#
#
# if __name__ == "__main__":
#     print("---")
#     greet("World")
# 错误代码：
# def dataF(num):
#     sum = 1
#     # n = 0
#     if num <= 1:
#         return 1
#     else:
#         for j in range(1, num):  # 0，1，2，3，。，num-1
#             if j == 1:
#                 continue
#             elif j < num:  # sum=1
#                 n = sum
#                 sum = sum + n
#     return sum


# 斐波那契数列
# def dataF(num):
#     n = 1
#     i = 1
#     sum1 = 1
#     if num <= 2:
#         return sum1
#     else:
#         for j in range(1, num - 1):
#             if j < num:
#                 n = i
#                 i = sum1
#                 sum1 = i + n
#
#         return sum1
#
#
# if __name__ == "__main__":
#     a = dataF(8)
#     print(a)

'''
冒泡排序
错误代码1 因为i+1 会下标越界，
所以我可以用两层嵌套去取值 一个从0开始遍历 一个从1开始遍历 (๑•̀ㅂ•́)و✧
'''
# def bubble(*args):
#     unlist = list(args)
#     emp_list = []
#     revers_list = []
#     for i in range(len(unlist)):
#         for j in range(len(unlist)-1):
#             if unlist[j] < unlist[j-1]:
#                 emp_list.append(unlist[j])
#                 unlist[j] = unlist[j-1]
#                 emp_list[j] = unlist[j-1]
#         revers_list.append(unlist[-1])
#         unlist.pop()
#     return revers_list
'''
错误代码2 根本不能两个循环同时走，达咩！
可以找个容器，没有必要更改原list,只要把每次比较的出来的最大值塞到空list里就好了
再试一次！！
'''


# def bubble1(*args):
#     unlist = list(args)
#     emp_list = []
#     revers_list = []
#     for j in range(len(unlist)):
#             for n in range(1, len(unlist)):
#                 if j < len(unlist):
#                     if unlist[j] > unlist[n]:
#                         emp_list.append(unlist[j])
#                         unlist[j] = unlist[n]
#                         unlist[n] = emp_list[0]
#                         emp_list.clear()
#                         j+=1
#         revers_list.append(unlist[-1])
#         unlist.pop()
#     return revers_list

def bubble3(args):
    # args = list(args)
    # emp_box = []
    emp_list = []
    for i in range(len(args)):
        # print(i)
        # emp_box = args[i]
        # print(emp_box)
        for j in range(i, len(args)):
            print(j)
            # if emp_box >= args[j]:
            #     continue
            # print(args[j])
            # emp_box = args[i]
            # print(args[i])
            if args[i] > args[j]:
                emp_box = args[j]
                args[j] = args[i]
                args[i] = emp_box
        # emp_list.append(emp_box)
        continue
    return args


'''
countinue!!! 用这个！！！
哽咽 竟然换个参数就对了 wtf?
'''

if __name__ == "__main__":
    list1 = [2, 9, 8, 0, 1, 2]
    # print(bubble(list1))
    a = bubble3(list1)
    print(a)

# list2 = [2,3,6,2,1,23,56]
# print(list2[3])
