from selenium import webdriver
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Test firstname")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Test lastname")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test@email.net")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "lesson2.2_step8.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
