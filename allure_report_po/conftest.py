'''
钩子函数
'''
import allure
import pytest
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()


@pytest.fixture()
def get_browser():
    # global driver  # 将driver设定为全局变量
    # 用例前置定义一个driver对象
    # driver = webdriver.Chrome()
    # driver.maximize_window()

    # 用例执行返回driver
    yield driver
    # 用例后置关闭浏览器
    driver.quit()


'''
以下这一串都是设置allure的目前看不懂
'''


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    # 获取测试用例执行结果，yield,返回一个result对象
    out = yield
    """
    从result对象获取测试用例结果的测试报告，返回一个report对象
    report对象的属性包括when(setup,call,teardown三个值)，
    nodeid(测试用例的名字)，outcome(用例的执行结果passed,failed)
    """
    report = out.get_result()
    # 获取call(用例执行阶段)的执行结果
    if report.when == "call":
        # 获取call用例执行失败的情况
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 大概意思是报告里跳过的用例+call执行的时候报错的情况 加上报告里失败的用例并且不是运行中报错的用例
            with allure.step("添加失败截图........."):
                # 添加allure报告截图 attach方法三个参数，源文件，文件名，文件类型
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
