'''
FUncitonal

'''
import requests
from json import load
import unittest
import time
import unittest
import time
import HtmlTestRunner as x
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from openpyxl import load_workbook
from xlutils.copy import copy as xl_copy
from datetime import datetime, timedelta


class Api(unittest.TestCase):

    def __init__(self):
        self.filename = '/home/am.bhatia/Desktop/contripoint/abc1.xlsx'
        self.wb = load_workbook(filename=self.filename)
        self.ws = self.wb.active
        print(self.wb)
        print(self.wb.sheetnames)

        # self.ws.append([self.filename])
        self.wb.create_sheet('Certifications')
        self.ws['A1'] = 'Email'
        self.ws['B1'] = 'Password'
        self.ws['C1'] = 'Test Case Module'
        self.ws['G1'] = 'Result'
        self.ws['H1'] = 'Date and Time'
        self.wb.save('/home/am.bhatia/Desktop/contripoint/abc1.xlsx')

        # datetime object containing current date and time
        futuredate = datetime.now()
        print(futuredate)
        self.ws['H2'] = futuredate

    def setUp(self):
        try:
            s = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=s)
            print("\n\n\n\n\n>>>>>>>>> CERTIFICATIONS >>>>>>>>>>>>")

            driver = self.driver
            driver.maximize_window()
            driver.get(
                "http://dev-contripoint.geminisolutions.com.s3-website.ap-south-1.amazonaws.com/#/dashboard")
            button = driver.find_element(
                By.XPATH, '/html/body/app-root/div/div/app-login-screen/div/div/div/mat-card/div[2]/div/button')
            button.click()
            time.sleep(6)

            window_handles = driver.window_handles
            driver.switch_to.window(window_handles[1])
            driver.find_element(
                By.XPATH, '//*[@id="identifierId"]').send_keys('test.user@geminisolutions.in')
            self.ws['A2'] = 'test.user@geminisolutions.in'
            driver.find_element(
                By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
            time.sleep(3)

            driver.find_element(
                By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Gemini@123#')
            self.ws['B2'] = 'Gemini@123#'
            driver.find_element(
                By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
            time.sleep(6)

            driver.switch_to.window(window_handles[0])
            time.sleep(6)
            print("\n 1 - Gemini Id and Password successfully login")
            self.ws['C2'] = 'Login'
            self.ws['G2'] = 'login Success'

            self.wb.save(self.filename)

        except Exception as e:
            print(e)
            print("\n 1 - Gemini Id and Password  login failed")
            self.ws['C2'] = 'Login'
            self.ws['G2'] = 'login failed'
            self.wb.save(self.filename)

     # As per unittest module, individual test should start with test_
    def Certifications(self):
        """

        """
        try:
            #Certifications
            a = self.driver.find_element(By.XPATH,'/html/body/app-root/div[3]/div/app-dash-board/div[3]/app-dash-cards/div/div[1]/div[1]/mat-card/mat-card-header/div[2]/mat-card-title')
            a.click()
            print("\n 2 - Selecting 'Certifications' successfully")
            self.ws['C3'] = 'Certifications'
            self.ws['G3'] = 'Pass'

            self.wb.save(self.filename)

            time.sleep(3)
        
        except Exception as e:
            print("\n\nERROR IN Certifications >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 2 - Selecting 'Certifications' get fail")
            self.ws['C3'] = 'Certifications'
            self.ws['G3'] = 'Fail'
            self.wb.save(self.filename)

    def Certifications_Api(self):

        try:
            self.url = "https://fonts.googleapis.com/css?family=Poppins"
            response = requests.get(self.url)
            print(response.content)
            print(response.headers)
        except Exception as e:
            print("Try again")

if __name__ == '__main__':
    tb = Api()
    tb.setUp()
    tb.Certifications()
    tb.Certifications_Api()