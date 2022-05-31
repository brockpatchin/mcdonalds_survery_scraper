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

s = input("Please enter your 26 digit code with the dashes include (56562-21231....)!\n")
code_split = s.split('-')


# 26 Digit Section
driver.find_element(By.ID, 'CN1').send_keys(code_split[0])
driver.find_element(By.ID, 'CN2').send_keys(code_split[1])
driver.find_element(By.ID, 'CN3').send_keys(code_split[2])
driver.find_element(By.ID, 'CN4').send_keys(code_split[3])
driver.find_element(By.ID, 'CN5').send_keys(code_split[4])
driver.find_element(By.ID, 'CN6').send_keys(code_split[5])
driver.find_element(By.ID, 'NextButton').click()
# End of 26 Digit Section
time.sleep(0.5)

# How did you place your order?
driver.find_element(By.ID, 'textR000455.3').click() # McDonald's App
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of How did you place your order?

# Start of Please select your visit type
driver.find_element(By.ID, 'textR004000.2').click() # Drive Thru
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of Please select your visit type

# Start of Please rate your overall satisfaction
driver.find_element(By.XPATH, "//label[@for='R001000.5']").click()
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of Please rate your overall experience

# Start of Did the employee ask if you were using the mobile app
driver.find_element(By.XPATH, "//label[@for='R000473.1']").click()
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of Did the employee ask if you were using the mobile app

# Start of Did the employee greet you by name or thank you
driver.find_element(By.XPATH, "//label[@for='R000474.1']").click()
time.sleep(0.5)
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
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of Please rate your satisfaction with

# Continuation of Please rate your satisfaction with
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[1]/td[1]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[2]/td[1]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[3]/td[1]/label").click()
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of Continuation

# Start of What items did you order?
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of What items did you order?

# Start of Did you experience a problem
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[2]/label").click()
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of Did you experience a problem

# Start of What is the likelihood that you will ...
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[1]/td[1]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[2]/td[1]/label").click()
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of What is the likelihood that you will ...

# Start of Paragraph thing 
para = "I really enjoy McDonald's. McDonald's is the best and it makes me happy. I am very glad that McDonald's always serves high quality food and drink :)"
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/div[2]/div[2]/div/div/div[2]/textarea").send_keys(para)
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of Paragraph thing

# Start of pull forward
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[2]/label").click()
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of pull forward

# Start of How many times have you been to McDonald's
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/fieldset/div/div/div[4]/span/label").click()
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of How many times have you been to McDonald's

# Start of What is your fav fast food place
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/fieldset/div/div/div[3]/span/label").click()
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of What is your fav fast food place

# Start of Trustworthy
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[1]/label").click()
time.sleep(0.5)
driver.find_element(By.ID, 'NextButton').click()
# End of Trustworthy

time.sleep(8)

# Start of Validation Code
full = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/div/div/div[1]/div/p[2]").text
x = int(full.split(" ")[-1])
print()
print()
print()
print("Your validation code is " + str(x))
print()
print()
print()

# End of Validation Code

time.sleep(8)

driver.close()