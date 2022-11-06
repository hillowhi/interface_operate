"""
pytest 的断言机制就是python运算符 + - * / 加上assert实现

!=
==
<=
>=
is true
is not true
"""
import pytest


def test_assert():
    print("运行assert断言用例")
    assert 1 == 2


def test_key():
    print("运行assert断言用例")
    assert 1 == 2


if __name__ == '__main__':
    pytest.main(['-s', '-v', '-k', 'key'])
    # -s 输出打印信息到控制台 -v输出更详细的用例信息
    # 更多关键词配置 可以到dos系统里 pytest --help
    # 运行包含某个关键字的用例 -k,'关键字'
    # -q 简化输出信息
    # -x 一条用例失败 则退出运行 pytest.main(['-x'])
    # 运行指定目录下的用例 pytest.main(['-s','相对于当前目录文件的地址'])
    # 相对于当前目录文件的路径表达：'/test_child_package::TestCase1::test_class_case'  类/方法都要用::双冒号隔开
