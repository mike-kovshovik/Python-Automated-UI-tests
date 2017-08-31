from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://www.w3schools.com/'
driver = webdriver.Firefox()
driver.get(url)


def assert_find_element(locator_type, locator_text):

    element = driver.find_element(locator_type, locator_text)

    if not element.is_displayed():
        raise AssertionError('The element could not be found')
    else:
        return True


assert_find_element('id', 'mySidenavx')


##