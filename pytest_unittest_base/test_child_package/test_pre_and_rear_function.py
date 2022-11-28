import pytest


def multiply(a, b):
    return a * b


def init_test(self):
    assert multiply(2, 2) == 8


class Test_pre_rear_fun():
    @classmethod
    def setup_class(cls):
        print("调用该函数类之前运行")

    @classmethod
    def teardown_class(cls):
        print("调用该类之后运行")

    def setup(self):
        print("开始前置函数运行------------")

    def teardown(self):
        print("后置函数运行结束啦------------")

    def test_01(self):
        assert multiply(2, 3) == 1

    def test_02(self):
        assert multiply(4, 5) == 20

    if __name__ == '__main__':
        pytest.main(['--html=.html_report.html'])
