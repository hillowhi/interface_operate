import pytest

"""
pytest 可以声明类 也可以不声明直接声明函数
pytest将在当前目录及其子目录中运行所有格式为test_*.或者 *_test.py文件
## 请观察子文件夹test_child_package 文件夹 里面的两个用例在此文件运行时也会同时运行
测试方法(类里定义的函数叫方法，类外面定义叫函数)、测试函数必须以test开头
测试类必须以Test开头
测试类不能有构造方法 __init__
"""


def test01():
    print("login")
    # pytest中 打印内容并不会展示在打印台，需要在main 函数里设置参数
    assert 1 == 1


if __name__ == '__main__':
    pytest.main()
