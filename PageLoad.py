import time  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import os

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome(executable_path='/home/am.bhatia/Desktop/chromedriver')
driver.maximize_window()
driver.get("http://dev-contripoint.geminisolutions.com.s3-website.ap-south-1.amazonaws.com/#/dashboard")

button = driver.find_element(By.XPATH,'/html/body/app-root/div/div/app-login-screen/div/div/div/mat-card/div[2]/div/button')
time.sleep(3)
button.click()

window_handles =driver.window_handles
driver.switch_to.window(window_handles[1])
Login = driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys('aman.bhatia@geminisolutions.in')
Login = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click()
time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input').send_keys('AmanBhatia96')
driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span').click()
time.sleep(6)
print("\n 1 - Gmail Id and Password successfully login")

driver.switch_to.window(window_handles[0])
time.sleep(10)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart
 
print("\n Back End: %s backendPerformance" % backendPerformance_calc)
print("\n Front End: %s frontendPerformance" % frontendPerformance_calc)
 
driver.quit()