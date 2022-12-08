

'''
充值
'''
from data_driver.data_driver.yaml_driver.book_pay_process import BookPayProcess


def test_pay_money(get_browser):
    book_pay_process = BookPayProcess(get_browser)
    pay_answer = book_pay_process.book_pay_process()
    assert pay_answer is True
