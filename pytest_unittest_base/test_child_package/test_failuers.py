import pytest


# import pytest_rerunfailures


def test_fail1():
    print("运行assert断言用例")
    assert 1 == 2


def test_fail2():
    print("运行assert断言用例")
    assert 1 == 1


def test_fail3():
    print("运行assert断言用例")
    assert 1 == 2


if __name__ == '__main__':
    pytest.main(['--reruns', '3', 'test_failures.py'])  # 指定失败的用例重跑次数3，每次有用例失败就重跑3次
    pytest.main(['--reruns', '3', '--reruns-delay', '2', 'test_failures.py'])  # 失败延迟 重跑失败用例之前延迟2S
