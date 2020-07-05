from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading
import time

content_list = ['djjdd ','Chrome','selenium ','webdriver ','Key ','import ','rang ',' 问问',' 的角度讲',' 嗯咯',]

def search(i):
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    time.sleep(10-i)
    while True:
        elem = driver.find_element_by_xpath('//*[@id="kw"]')
        elem.send_keys(content_list[i])
        elem.send_keys(Keys.RETURN)  # 这里需要引入库，否则报错
        time.sleep(5)

if __name__ == "__main__":

    for i in range(1,10):
        th1 = threading.Thread(target=search,
                               args=(i,))
        th1.start()



