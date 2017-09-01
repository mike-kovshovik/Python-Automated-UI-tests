from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = 'http://www.echoecho.com/htmlforms09.htm'

driver.get(url)
table_with_checkboxes = driver.find_element_by_class_name('table8')


def assert_verify_presence_of_table(element):
    if element.get_attribute('class') != 'table8':
        raise AssertionError('There is no such element present of the page')
    else:
        print('the element is in a place')


def assert_element_is_a_checkbox(element):
    if element.get_attribute('type') not in ['checkbox', 'Checkbox']:
        raise AssertionError('The element is not a checkbox')
    return


def assert_checkbox_is_checked(element):
    assert_element_is_a_checkbox(element)   # This is to verify the element is actually a checkbox
    print('Checkbox status is: ' + str(element.get_attribute('checked')).upper())
    if element.get_attribute('checked'):  # If the attribute is checked='' it means that it will be checked
        print('The checkbox with the name {} is selected'.format(element.get_attribute('name')))
    else:
        return False


second_checkbox = driver.find_element_by_xpath('html/body/div[2]/table[9]/tbody/tr/td[4]/table/tbody/tr/td/div/span/form/table[1]/tbody/tr/td/table/tbody/tr[2]/td[3]/input[2]')
assert_checkbox_is_checked(second_checkbox)
