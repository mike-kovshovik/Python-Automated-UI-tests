from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'http://www.echoecho.com/htmlforms10.htm'

driver.get(url)


def assert_element_is_radiobutton(element):
    if element.get_attribute('type') != 'radio':
        raise AssertionError('The element you passed is not a radio-button')
    else:
        print('The element is a radio-button')


def select_radio_by_value(elements, value):

    for element in elements:
        assert_element_is_radiobutton(element)
        current_value = element.get_attribute('value')

        if current_value == value:
            element.click()
            break


# element_to_check = driver.find_element(By.XPATH, 'html/body/div[2]/table[9]/tbody/tr/td[4]/table/tbody/tr/td/div/span/form/a/span')
# assert_element_is_radiobutton(element_to_check)

table1 = driver.find_element(By.XPATH, 'html/body/div[2]/table[9]/tbody/tr/td[4]/table/tbody/tr/td/div/span/form/table[3]/tbody/tr/td/table/tbody/tr/td')
my_radio = table1.find_elements_by_name('group2')

select_radio_by_value(my_radio, 'Water')

