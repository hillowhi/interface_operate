import os

import pytest


def run():
    pytest.main(['--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report/ --clean')


if __name__ == '__main__':
    run()
