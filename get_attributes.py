from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_textarea'
driver = webdriver.Firefox()
driver.get(url)

my_frame = driver.find_element('id', 'iframeResult')
driver.switch_to.frame(my_frame)

box = driver.find_element_by_tag_name('textarea')

box_text = box.get_attribute('value')
print(box_text)

num_rows = box.get_attribute('rows')
num_columns = box.get_attribute('cols')

print(num_rows, num_columns)

'''


def assert_find_element(locator_type, locator_text):

    element = driver.find_element(locator_type, locator_text)

    if not element.is_displayed():
        raise AssertionError('The element could not be found')
    else:
        return True


assert_find_element('id', 'mySidenavx')
##

'''