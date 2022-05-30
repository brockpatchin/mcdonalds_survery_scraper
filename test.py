from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)




driver.get('https://www.mcdvoice.com')
driver.maximize_window()

time.sleep(5)


# 26 Digit Section
driver.find_element(By.ID, 'CN1').send_keys('12353')
driver.find_element(By.ID, 'CN2').send_keys('13950')
driver.find_element(By.ID, 'CN3').send_keys('52522')
driver.find_element(By.ID, 'CN4').send_keys('06504')
driver.find_element(By.ID, 'CN5').send_keys('00052')
driver.find_element(By.ID, 'CN6').send_keys('9')
driver.find_element(By.ID, 'NextButton').click()
# End of 26 Digit Section

# How did you place your order?
driver.find_element(By.ID, 'textR000455.3').click()
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
# End of How did you place your order?

# Start of Please select your visit type
driver.find_element(By.ID, 'textR004000.2').click()
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()


time.sleep(8)

driver.close()