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


@pytest.mark.smoke
# 此处就是标记 smoke
def test_key():
    print("运行assert断言用例")
    assert 1 == 2


if __name__ == '__main__':
    # pytest.main(['2', '-auto', 'test_assert.py']) #跟运行电脑内核一样跑用例
    # pytest.main(['2', '-n', 'test_assert.py']) #多线程跑用例 pytest版本太会高跑不起来
    # pytest.main(['-m', 'smoke'])  # 只运行被smoke标记的用例
    # pytest.main(['-s', '--junit-xml=./report/junit_report01.xml --clean', '--maxfail==2'])
    # -s 输出打印信息到控制台 -v输出更详细的用例信息
    # 更多关键词配置 可以到dos系统里 pytest --help
    # 运行包含某个关键字的用例 -k,'关键字'
    # -q 简化输出信息
    # -x 一条用例失败 则退出运行 pytest.main(['-x'])
    # 运行指定目录下的用例 pytest.main(['-s','相对于当前目录文件的地址'])
    # 相对于当前目录文件的路径表达：'/test_child_package::TestCase1::test_class_case'  类/方法都要用::双冒号隔开
    # 允许最大用例失败数 pytest.main(['--maxfail==2']) 当出现2个失败用例时 则退出用例执行
    # 运行指定装饰器标记的用例 pytest.main(['-m', 'smoke']) smoke 是装饰器，-m 意思是mark
    '''
    装饰器 标记的 标记必须在pytest.init 文件中自定义 在当前文件根目录下创建init文件
    '''
