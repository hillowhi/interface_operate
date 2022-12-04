from data_driver.data_driver.yaml_driver.book_pay_process import Book_Pay_Process


def test_pay_money(get_browser):
    book_pay_process = Book_Pay_Process(get_browser)
    book_pay_process.book_pay_process()
