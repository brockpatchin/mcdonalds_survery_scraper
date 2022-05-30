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
driver.find_element(By.ID, 'textR000455.3').click() # McDonald's App
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
# End of How did you place your order?

# Start of Please select your visit type
driver.find_element(By.ID, 'textR004000.2').click() # Drive Thru
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
# End of Please select your visit type

# Start of Please rate your overall satisfaction
driver.find_element(By.XPATH, "//label[@for='R001000.5']").click()
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
# End of Please rate your overall experience

# Start of Did the employee ask if you were using the mobile app
driver.find_element(By.XPATH, "//label[@for='R000473.1']").click()
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
# End of Did the employee ask if you were using the mobile app

# Start of Did the employee greet you by name or thank you
driver.find_element(By.XPATH, "//label[@for='R000474.1']").click()
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
# End of Did the employee greet you by name or thank you

# Start of Please rate your satisfaction with
# R005000.5
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[1]/td[1]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[2]/td[1]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[3]/td[1]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[4]/td[1]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[5]/td[1]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[6]/td[1]/label").click()
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
# End of Please rate your satisfaction with

# Continuation of Please rate your satisfaction with
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[1]/td[1]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[2]/td[1]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[3]/td[1]/label").click()
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
# End of Continuation

# Start of What items did you order?
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
# End of What items did you order?

# Start of Did you experience a problem
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[2]/label").click()
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
# End of Did you experience a problem

# Start of What is the likelihood that you will ...
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[1]/td[1]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[2]/td[1]/label").click()
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
# End of What is the likelihood that you will ...



time.sleep(8)

driver.close()