import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('time', ["95", "96", "97", "98", "99", "03", "04", "05"])
def test_guest_should_see_login_link(browser, time):
    link = f"https://stepik.org/lesson/236{time}/step/1"
    browser.get(link)

    answer = math.log(int(time.time()))
    quiz = browser.find_element_by_class_name("quiz-component")
    quiz.send_keys(answer)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()