from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_image():
    chrome_options = Options()
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://search.jd.com/Search?keyword=iphone%20%2C14&enc=utf-8&wq=iphone%20%2C14&pvid'
               '=7e484fe7ea85403a8126f08e4b1fbf49')
    sleep(2)
    driver.execute_script("var q=document.documentElement.scrollTop=10000")
    img_list = driver.find_elements('xpath', "//img[@width='220' and @height = '220' and @data-img='1']")
    test_list = []
    for i in range(0, len(img_list)):
        goods_dict = {}
        goods_dict["platform"] = 'JD'
        goods_dict["good_img"] = img_list[i].get_attribute('src')
        test_list.append(goods_dict)
    print(test_list)


if __name__ == '__main__':
    test_image()
