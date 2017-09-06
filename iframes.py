from selenium import webdriver
from selenium.webdriver.common.by import By
import uuid

# random_first_name = random_last_name = uuid.uuid4().hex
random_first_name = 'auto_first_name_' + uuid.uuid4().hex
random_last_name = 'auto_last_name_' + uuid.uuid4().hex


url = 'https://tst-04.test.intelliflo.com/nio/dashboard/userdashboard'

driver = webdriver.Chrome()
driver.get(url)

login_button = driver.find_element(By.LINK_TEXT, 'Login')
login_button.click()
username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')

username.send_keys('vdamm04')
password.send_keys('qWaszx12')

login_confirm = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
login_confirm.click()

add_client = driver.find_element_by_link_text('Add Client').click()

add_client_iframe = driver.find_element(By.XPATH, '/html/body/div[11]/iframe')

driver.switch_to.frame(add_client_iframe)

first_name = driver.find_element_by_id('Life1FirstName').send_keys(random_first_name)
last_name = driver.find_element_by_id('Life1LastName').send_keys(random_last_name)
client_dob = driver.find_element_by_id('id_BasicDetailsStep_FirstLife_DateOfBirth').send_keys('14/09/1984')
finish_button = driver.find_element_by_css_selector('.complete.button.button-enabled').click()

driver.switch_to.default_content()


#bar_info = driver.find_element(By.XPATH, ".//*[@id='sidebar-container']/div[1]/div")
#bar_info_text = bar_info.text
#print(bar_info_text)



#url = 'https://www.intelligent-office.net/nio/dashboard/userdashboard'
#username.send_keys('mkau99')
#password.send_keys('P@ssw0rd12345')