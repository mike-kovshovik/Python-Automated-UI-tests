from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid

# random_first_name = random_last_name = uuid.uuid4().hex
random_first_name = 'auto_first_name_' + uuid.uuid4().hex
random_last_name = 'auto_last_name_' + uuid.uuid4().hex

# arrange
url = 'https://tst-04.test.intelliflo.com/nio/dashboard/userdashboard'

driver = webdriver.Chrome()
driver.get(url)

login_button = driver.find_element(By.LINK_TEXT, 'Login')
login_button.click()

username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')

username.send_keys('vdamm04')
password.send_keys('qWaszx12')

# act
login_confirm = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
login_confirm.click()
add_client = driver.find_element_by_link_text('Add Client').click()
add_client_iframe = driver.find_element(By.XPATH, '/html/body/div[11]/iframe')
driver.switch_to.frame(add_client_iframe)
first_name_control = driver.find_element_by_id('Life1FirstName')
first_name_control.send_keys(random_first_name)
last_name_control = driver.find_element_by_id('Life1LastName')
last_name_control.send_keys(random_last_name)
client_dob_control = driver.find_element_by_id('id_BasicDetailsStep_FirstLife_DateOfBirth')
client_dob_control.send_keys('14/09/1984')
finish_button = driver.find_element_by_css_selector('.complete.button.button-enabled')
finish_button.click()
driver.switch_to.default_content()


# assert
def assert_client_was_created():
    text_to_look_for = random_first_name + ' ' + random_last_name
    if text_to_look_for not in driver.page_source:
        raise AssertionError("The client with the name {} was not created".format(text_to_look_for))
    else:
        print("The client was created - Test Passed")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@id='sidebar-container']/div/div")))

assert_client_was_created()

#bar_info = driver.find_element(By.XPATH, ".//*[@id='sidebar-container']/div[1]/div")
#bar_info_text = bar_info.text
#print(bar_info_text)

'''







You can use driver.page_source and a simple regular expression to check if the text exists:

import re    
src = driver.page_source
text_found = re.search(r'text_to_search', src)
self.assertNotEqual(text_found, None)

url = 'https://www.intelligent-office.net/nio/dashboard/userdashboard'
username.send_keys('mkau99')
password.send_keys('P@ssw0rd12345')

'''