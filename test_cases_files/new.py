'''
FUncitonal

'''
from lib2to3.pgen2 import driver
from typing import KeysView
import unittest
import time
import HtmlTestRunner as x
import pyautogui
from traceback import print_exc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from openpyxl import load_workbook
from datetime import datetime, timedelta


class CAuth(unittest.TestCase):
    
    def __init__(self): 
        chrome_options = Options()
        chrome_options.add_experimental_option('debuggerAddress', 'localhost:9222')
            
        self.driver = webdriver.Chrome(options=chrome_options,executable_path="C:\\Users\\Aman Bhatia\\OneDrive - Gemini Solutions\\Desktop\\Contripoint_Project\\ChromeDriver\\chromedriver.exe")
        print("Browser Connected")

        # driver= self.driver
        # driver.implicitly_wait(5)
        self.driver.get(
                'https://dev-contripoint.geminisolutions.com/#/dashboard')

        time.sleep(5)


        #Certifications
        self.driver.find_element(By.XPATH,'//div[text()="Certificate"]').click()            
        print("\n 2 - Selecting 'Certifications' successfully")

        self.driver.execute_script("window.scrollTo(0,100)")

        self.driver.find_element(By.XPATH,'//*[@id="add_btn"]').click()
        time.sleep(6)


    def tearDown(self):
        self.driver.quit()

           

if __name__ == '__main__':
    tb = CAuth()