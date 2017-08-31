from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
url = 'https://www.w3schools.com'

driver.get(url)
my_left_nav = driver.find_element_by_class_name('w3-sidebar')
left_nav_text = my_left_nav.text

print(left_nav_text)




from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)

# save the url to navigate to in a variable
url = 'http://www.w3schools.com/html/html_tables.asp'

# Navigate to the url
driver.get(url)


def get_number_of_table_rows(my_table):
    """
    Description:
            Function to count the number of rows in a table. The table must be passed in as an element.
            Does not distinguish a table header tag <th> and will not count it.

    Parameters:
            my_table - The table element which the rows to be counted.

    Returns:
        number_of rows
    """

    all_rows = my_table.find_elements_by_tag_name('tr')
    number_of_rows = len(all_rows)

    return number_of_rows


def assert_number_of_rows_in_table(my_table, expected_num_of_rows):
    """
    Description:
        Function to assert a table has the expected number of rows. The table has to be passed as an element.
        The number of expected rows must be passed in as integer.
        The function raises and assertion error if the number of rows is not as expected.

    Parameters:
        my_table - the table element
        expected_num_of_rows - the number of rows

    Returns:
        None
    """

    actual_num_rows = get_number_of_table_rows(my_table)

    if expected_num_of_rows != actual_num_rows:
        raise AssertionError('The number of row did not match. The actual number is: %s and the expected\
        number is %s' % (str(actual_num_rows), str(expected_num_of_rows)))

    return


def assert_row_contains_text(my_table, text_to_check, row_number):
    """
    Description:
        Function that will assert if the expected text is not within the row specified. User must pass thet able as
        a web element, the text to look for and the row number.
        Raises and assertion error if the text is not found

    Parameters:
        my_table - the table as an element
        text_to_check - the expected text in the row (can be partial text)
        row_number - the row to search the text for

    Returns:
        None
    """

    all_rows = my_table.find_elements_by_tag_name('tr')
    my_row = all_rows[row_number]
    row_text = my_row.text

    if text_to_check not in row_text:
        raise AssertionError('The text %s is not in row %s' % (text_to_check, row_number))
    else:
        print 'The text %s is found in row %s' % (text_to_check, row_number)

    return


def assert_col_in_row_contains_text(my_table, text_to_check, row_number=0, col_number=0):
    """
    Description:
        Function to check the specified text is in the given cell. User must pass the table as element, the text to
        look for, the row number and the column number.
        Raises an assertion error if the text is not found.

    Description:
        my_table - The table as an element
        text_to_check - The text to search (can be partial text)
        row_number - the row number to search
        col_number - the column to search

    Returns:
        None
    """

    all_rows = my_table.find_elements_by_tag_name('tr')

    if row_number > len(all_rows):
        raise BaseException('The row number requested is more than the available rows')

    my_row = all_rows[row_number]
    all_cols = my_row.find_elements_by_tag_name('td')
    my_col = all_cols[col_number]
    col_text = my_col.text

    if text_to_check not in col_text:
        raise AssertionError('The text %s is not in row %s column %s' % (text_to_check, str(row_number), str(col_number)))
    else:
        print 'The text %s is in row %s and column %s' % (text_to_check, str(row_number), str(col_number))

    return


# Function calls start here
table = driver.find_element_by_class_name('reference')

rows = get_number_of_table_rows(table)

print rows

assert_number_of_rows_in_table(table, 5)
assert_col_in_row_contains_text(table, 'Jill', row_number=4, col_number=1)


##



