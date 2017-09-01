from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

base_url = 'https://intelliflo99.mypfp.co.uk'
driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(30)

driver.find_element(By.XPATH, 'html/body/div[1]/div/header/div/div/div[2]/nav/div[1]/div[2]/a').click()

driver.find_element(By.ID, 'username').send_keys('*****')
driver.find_element(By.ID, 'password').send_keys('*****')

driver.find_element(By.XPATH, 'html/body/div/div[2]/div/div/div[1]/div/div[1]/form/fieldset/div[3]/button').click()

#driver.implicitly_wait(30)
driver.set_page_load_timeout(30)
driver.get(base_url + '/overview/planningandadvice')

terms_of_service_checkbox = driver.find_element_by_xpath(".//*[@id='planning-and-advice-form']/div/div/div[4]/label/span")
no_debts_checkbox = driver.find_element_by_xpath(".//*[@id='planning-and-advice-form']/div/div/div[5]/label/span")
start_planning_button = driver.find_element(By.ID, 'startPlanningBtn')
next_on_how_service_works = driver.find_element_by_xpath(".//*[@id='how-service-works']/main/div/div[2]/div[2]/a")


terms_of_service_checkbox.click()   # selects the first checkbox
no_debts_checkbox.click()
start_planning_button.click()
next_on_how_service_works.click()
