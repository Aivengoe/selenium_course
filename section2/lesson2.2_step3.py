from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num1_value = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    num2_value = int(num2.text)

    summ = num1_value + num2_value

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("{}".format(summ))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

