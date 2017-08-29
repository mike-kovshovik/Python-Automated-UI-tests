from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

base_url = 'https://intelliflo99.mypfp.co.uk'
driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(30)

driver.find_element(By.XPATH, 'html/body/div[1]/div/header/div/div/div[2]/nav/div[1]/div[2]/a').click()

driver.find_element(By.ID, 'username').send_keys('forgotpasswordinprod@mailinator.com')
driver.find_element(By.ID, 'password').send_keys('qWaszx123')

driver.find_element(By.XPATH, 'html/body/div/div[2]/div/div/div[1]/div/div[1]/form/fieldset/div[3]/button').click()

driver.implicitly_wait(30)
driver.get(base_url + '/overview/planningandadvice')


def number_of_rows_in_table(my_table):
    all_rows = my_table.find_elements_by_tag_name('tr')
    number_of_rows = len(all_rows)
    return number_of_rows


def assert_number_of_rows_in_table(my_table, expected_number_of_rows):
    actual_number_of_rows = number_of_rows_in_table(my_table)
    if actual_number_of_rows != expected_number_of_rows:
        raise AssertionError('Actual number of rows is {} which is not equal to the expected number which is {}'.format(str(actual_number_of_rows), str(expected_number_of_rows)))
    else:
        print('Actual number of rows is {} which is equal to the expected number of rows'.format(str(actual_number_of_rows)))


def assert_row_contains_text(my_table, text_to_compare_with, row_number):
    all_rows = my_table.find_elements_by_tag_name('tr')
    my_row = all_rows[row_number]
    my_row_text = my_row.text
    print(my_row.text)

    if my_row_text not in text_to_compare_with:
        raise AssertionError('The text does not match with the expected text')
    return


def assert_row_column_contains_text(my_table, text_to_compare_with, row_number, column_number):
    all_rows = my_table.find_elements_by_tag_name('tr')
    my_row = all_rows[row_number]
    my_column = my_row.find_elements_by_tag_name('td')
    my_column_text = my_column[column_number].text

    if my_column_text != text_to_compare_with:
        raise AssertionError('The text in a cell is {} but should be {}'.format(my_column_text, text_to_compare_with))
    else:
        print('The text in a cell matches the expected text')



table_1 = driver.find_element(By.XPATH, ".//*[@id='planning-and-advice-form']/div/div/div[3]/div/div[2]")
text_in_cell = '0.94%'

assert_row_column_contains_text(table_1, text_in_cell, 2, 1)


print('***************')
print(number_of_rows_in_table(table_1))
print('***************')

assert_number_of_rows_in_table(table_1, 4)

print('***************')
test_text_to_compare = 'Nutmeg 0.94% close'
assert_row_contains_text(table_1, test_text_to_compare, 2)
print('***************')


def assert_verify_the_row_contains_text(my_table, text_to_compare_with, row_number):
    all_rows = my_table.find_elements(By.TAG_NAME, 'tr')
    my_row = all_rows[row_number - 1]
    if text_to_compare_with not in my_row:
        raise AssertionError('The text {} is not equal to the {}'.format(my_row, text_to_compare_with))
    else:
        print('The text {} matches with the text {} we were looking for'.format(text_to_compare_with), all_rows[row_number - 1])

print('--------------------------------')




