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


def find_element_in_dropdown_by_visible_text(dropdown_element, option):

    all_options_from_dropdown = dropdown_element.find_elements_by_tag_name('option')
    for item in all_options_from_dropdown:
        item_text = item.text

        if item_text == option:
            item.click()
            return


def assert_find_dropdown_element_by_value(dropdown, value):

    all_options_from_dropdown = dropdown.find_elements_by_tag_name('option')
    for item in all_options_from_dropdown:
        item_value = item.get_attribute('value')
        if item_value == value:
            item.click()
            return
    raise AssertionError('The requested element "{value}" is not among the list of values'.format(value))


text = 'Electronics'
option_value = 'search-alias=mobile'

#assert_element_is_drop_down(main_dropdown)
#find_element_in_dropdown_by_visible_text(main_dropdown, text)
assert_find_dropdown_element_by_value(main_dropdown, option_value)



