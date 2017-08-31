from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = 'https://www.amazon.com'

driver.get(url)

main_dropdown = driver.find_element(By.ID, 'searchDropdownBox')


def assert_element_is_drop_down(element):
    if element.get_attribute('class') not in ['nav-search-dropdown searchSelect']:
        raise AssertionError("The element is not a drop-down list")
    else:
        print("The element is a drop-down list")

    return

assert_element_is_drop_down(main_dropdown)

