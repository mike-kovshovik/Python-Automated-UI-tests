from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# import time

# arrange
driver = webdriver.Chrome()
url = 'https://answers.squarespace.com/index.html'

# act
driver.get(url)
wait = WebDriverWait(driver, 10)
element = wait.until(ec.presence_of_element_located((By.LINK_TEXT, 'Main Website')))
# time.sleep(2)

documentation_link = driver.find_element_by_link_text('Documentation')
documentation_link.click()


# assert
def get_number_of_windows():
    windows = driver.window_handles
    win_count = len(windows)
    # print("There are {} windows opened in a browser".format(win_count))
    return win_count


def switch_to_window_number(win_index):
    try:
        win_index = int(win_index)
    except ValueError:
        raise Exception('The value passed in is not an integer')

    total_number_of_windows = get_number_of_windows()

    if win_index > total_number_of_windows:
        raise Exception('There is no such window with index {}'.format(win_index))

    all_windows = driver.window_handles
    requested_window = all_windows[win_index-1]
    driver.switch_to.window(requested_window)

    return


get_number_of_windows()
switch_to_window_number(2)
