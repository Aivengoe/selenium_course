import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('num', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_guest_should_see_login_link(browser, num):
    link = f"https://stepik.org/lesson/236{num}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    quiz = browser.find_element_by_class_name("ember-text-area")
    quiz.click()
    quiz.send_keys('%.14f' % answer)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    
    message = browser.find_element_by_class_name("smart-hints__hint")
    assert "Correct!" in message.text, message.text