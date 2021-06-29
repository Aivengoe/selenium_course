from selenium import webdriver
import unittest
import time

def request_site(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block input.first")
    input1.send_keys("Test")
    input2 = browser.find_element_by_css_selector(".first_block input.second")
    input2.send_keys("Test")
    input3 = browser.find_element_by_css_selector(".first_block input.third")
    input3.send_keys("Test")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    return(welcome_text)


class TestSite(unittest.TestCase):
    def test_site1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = "Congratulations! You have successfully registered!"
        self.assertEqual(request_site(link), welcome_text)
    
    def test_site2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = "Congratulations! You have successfully registered!"
        self.assertEqual(request_site(link), welcome_text)


if __name__ == "__main__":
    unittest.main()