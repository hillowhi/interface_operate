"""
unittest 是python自带的测试框架 基于类的引用

"""
import unittest


class UnitDemo(unittest.TestCase):
    def test_login(self):
        print("login")
        self.assertEqual("123", "123", msg="登陆报错信息")


if __name__ == '__main__':
    unittest.main()
