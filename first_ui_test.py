from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()

driver.get('https://tst-04-pfp.test.intelliflo.com')

driver.find_element(By.XPATH, 'html/body/div[1]/div/header/div/div/div[2]/nav/div[1]/div[2]/a').click()

driver.find_element(By.ID, 'username').send_keys('checkforalexei@mailinator.com')
driver.find_element(By.ID, 'password').send_keys('qWaszx12')

driver.find_element(By.XPATH, 'html/body/div/div[2]/div/div/div[1]/div/div[1]/form/fieldset/div[3]/button').click()

element = WebDriverWait(driver, 10)

driver.find_element(By.LINK_TEXT, 'Planning & Advice').click()

element = WebDriverWait(driver, 10)


driver.find_element(By.ID, 'isDisclosureRead').click()
driver.find_element(By.ID, 'hasNoDebts').click()


###  driver.find_element(By.XPATH, ".//*[@id='planning-and-advice-form']/div/div/div[5]/label/span'").click()





