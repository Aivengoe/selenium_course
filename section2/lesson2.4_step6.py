from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    # browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element_by_id("button")


finally:
    time.sleep(2)
    browser.quit()