from lib2to3.pgen2 import driver
import unittest
import time
import HtmlTestRunner as x
import pyautogui
from multiprocessing import Event
from traceback import print_exc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from openpyxl import load_workbook
from datetime import datetime, timedelta

from datainputs import *


class Login(unittest.TestCase):

    def __init__(self):
        self.filename = '/home/am.bhatia/Desktop/contripoint/abc1.xlsx'
        self.wb = load_workbook(filename=self.filename)
        self.index_sheet = 0
        if 'Polling Event' not in self.wb.sheetnames:
            self.wb.create_sheet('Polling Event')
            self.wb.save('/home/am.bhatia/Desktop/contripoint/abc1.xlsx')
        self.wb = load_workbook(filename=self.filename)
        self.ws = self.wb.active
        for i, n in enumerate(self.wb.sheetnames):
            if n == 'Polling Event':
                self.index_sheet = i
                break
        self.wb.active = self.index_sheet
        self.ws = self.wb.active
        self.wb.active = 1
        self.ws['A1'] = 'Email'
        self.ws['B1'] = 'Password'
        self.ws['C1'] = 'Test Case Module'
        self.ws['G1'] = 'Result'
        self.ws['H1'] = 'Date and Time'
        self.wb.save('/home/am.bhatia/Desktop/contripoint/abc1.xlsx')

        # datetime object containing current date and time
        futuredate = str(datetime.now())
        print(futuredate)
        self.ws['H2'] = futuredate

    def setExternalDriver(self, driver):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)

        self.driver.maximize_window()

    def MFA(self):
        try:
            # set implicit wait time
            self.driver.implicitly_wait(10)  # seconds

            print("\n >>>>>>>>>> Login >>>>>>>>>>>> \n")

            # get url
            self.driver.get(
                "https://dev-contripoint.geminisolutions.com/#/dashboard")
            button = self.driver.find_element(
                By.XPATH, '/html/body/app-root/div/div/app-login-screen/div/div/div/mat-card/div[2]/div/button')
            button.click()

            print("\n 1- Login With Gemini mail \n")

            time.sleep(6)

            window_handles = self.driver.window_handles
            self.driver.switch_to.window(window_handles[1])

            # Entering Mail Id in input
            self.driver.find_element(
                By.XPATH, '//*[@id="i0116"]').send_keys(login_Id)
            self.ws['A2'] = 'aman.bhatia@geminisolutions.com'
            print("\n 2- Entering mail id \n")

            self.driver.find_element(
                By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input').click()
            time.sleep(3)

            # Entering Passowrd in Input
            self.driver.find_element(
                By.XPATH, '//*[@id="i0118"]').send_keys(login_Password)
            self.ws['B2'] = 'RitaNandini96'
            print("\n 3- Entering mail password \n")

            self.driver.find_element(
                By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input').click()
            time.sleep(6)

            # Entering Multi-factor Authentication (MFA) Code Manually
            self.driver.find_element(By.ID, "idTxtBx_SAOTCC_OTC")
            time.sleep(6)
            print("\n 4- Entering and Verifying MFA Code \n")

            self.driver.find_element(
                By.XPATH, '//*[@id="idSubmit_SAOTCC_Continue"]').click()
            time.sleep(5)

            self.driver.find_element(
                By.XPATH, '//*[@id="KmsiCheckboxField"]').click()
            time.sleep(5)

            self.driver.find_element(By.ID, "idSIButton9").click()

            print("\n 5- Login Successfull \n")
            time.sleep(6)

            print("\n 6 - Gemini Id and Password successfully login \n")
            self.ws['C2'] = 'Login'
            self.ws['G2'] = 'login Success'

            self.wb.save(self.filename)

        except Exception as e:

            print("\n 6 - Gemini Id and Password  login failed")
            print(e)

            self.ws['C2'] = 'Login'
            self.ws['G2'] = 'login failed'
            self.wb.save(self.filename)

    def Events(self):
        """

        """
        try:

            y = self.driver.window_handles[0]
            time.sleep(6)
            self.driver.switch_to.window(y)

            # Clicking on Events
            self.driver.find_element(
                By.XPATH, '/html/body/app-root/div/app-navbar/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
            time.sleep(6)
            print("\n 7 - Clicking on Events ")

            # Create New Event
            self.driver.find_element(By.ID, "add_btn").click()
            time.sleep(5)
            print("\n 8 - Creating New Event")

        except Exception as e:
            print("\n 7 - Clicking on Events ")
            print("\n 8 - Error in Creating New Event")
            print(e)

    def Add_Banner_Image(self):
        """

        """
        try:
            # Adding Banner Image
            self.driver.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-event-modal/mat-dialog-content/mat-horizontal-stepper/div[2]/div[1]/form/div[1]/div[1]/label/img').click()
            time.sleep(8)
            pyautogui.write(banner_image)
            pyautogui.press('enter')
            print("\n 9 - Banner Image Upload successfully")
            self.ws['C3'] = 'Uploading Banner Image'
            self.ws['G3'] = 'Pass'

            self.wb.save(self.filename)
            time.sleep(3)

        except Exception as e:
            print("\n ERROR IN Adding Banner Image >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 9 - Unable to Add Banner Image")
            self.ws['C3'] = 'Uploading Banner Image'
            self.ws['G3'] = 'Fail'

            self.wb.save(self.filename)

    def Add_Listing_Image(self):
        """

        """
        try:
            # Adding Listing Image
            self.driver.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-event-modal/mat-dialog-content/mat-horizontal-stepper/div[2]/div[1]/form/div[2]/div[1]/label/label/img').click()
            time.sleep(8)
            pyautogui.write(listing_image)
            pyautogui.press('enter')
            time.sleep(3)

            print("\n 10 - Listing Image Upload successfully")

            self.ws['C4'] = 'Upload Listing Image'
            self.ws['G4'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Adding Listing Image >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 10 - Unable to Add Listing Image")

            self.ws['C4'] = 'Upload Listing Image'
            self.ws['G4'] = 'Fail'
            self.wb.save(self.filename)

    def Event_Name(self):
        """

        """
        try:
            # Entering  Event Name
            self.driver.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-event-modal/mat-dialog-content/mat-horizontal-stepper/div[2]/div[1]/form/div[2]/div[2]/div[1]/mat-form-field/div/div[1]/div/input').send_keys("Polling Event")
            time.sleep(5)
            print("\n 11 - Entering Event Name ")

            self.ws['C5'] = 'Event Name'
            self.ws['G5'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Event Name >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Unable to Add Event Name")

            self.ws['C5'] = 'Event Name'
            self.ws['G5'] = 'Fail'
            self.wb.save(self.filename)

    def Description(self):
        """

        """
        try:
            # Entering Description
            self.driver.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-event-modal/mat-dialog-content/mat-horizontal-stepper/div[2]/div[1]/form/div[2]/div[2]/div[2]/mat-form-field/div/div[1]/div/textarea').send_keys("Please take participate in Polling Event and win Rewards")
            time.sleep(5)
            print("\n 12 - Entering Description  ")

            self.ws['C6'] = 'Description '
            self.ws['G6'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Description  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 12 - Unable to Add Description ")

            self.ws['C6'] = 'Description '
            self.ws['G6'] = 'Fail'
            self.wb.save(self.filename)

    def Next_Button(self):
        """

        """
        try:
            # Clicking on Next Button
            self.driver.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-event-modal/mat-dialog-content/mat-horizontal-stepper/div[2]/div[1]/form/div[3]/div/button').click()
            time.sleep(5)
            print("\n 13 - Clicking on Next Button  ")

            self.ws['C7'] = 'Next Button '
            self.ws['G7'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Next Button  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 13 - Unable to Add Next Button ")

            self.ws['C7'] = 'Next Button '
            self.ws['G7'] = 'Fail'
            self.wb.save(self.filename)

    def Event_Type(self):
        """

        """
        try:
            # Clicking on Event Type
            self.driver.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-event-modal/mat-dialog-content/mat-horizontal-stepper/div[2]/div[2]/form/div[1]/div/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span').click()
            time.sleep(5)
            print("\n 14 - Clicking on Event Type Dropdown ")

            self.driver.find_element(By.ID,"mat-option-2").click()
            time.sleep(5)

            print("\n 15 - Event Type - Polling Event")

            self.ws['C8'] = 'Event Type - Polling Event'
            self.ws['G8'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Event Type  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 15 - Unable to Select Event Type ")

            self.ws['C8'] = 'Event Type - Polling Event'
            self.ws['G8'] = 'Fail'
            self.wb.save(self.filename)

    def Start_Date(self):
        """

        """
        try:
            # Clicking on Start Date
            self.driver.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-event-modal/mat-dialog-content/mat-horizontal-stepper/div[2]/div[2]/form/div[2]/div[1]/mat-form-field/div/div[1]/div[1]/input').click()
            time.sleep(5)
            print("\n 16 - Clicking on Start Date Calander ")

            self.driver.find_element(By.XPATH,'//*[@id="mat-datepicker-0"]/div/mat-month-view/table/tbody/tr[2]/td[2]/div[1]').click()
            time.sleep(5)

            self.ws['C9'] = 'Start Date'
            self.ws['G9'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Start Date  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 16 - Unable to Add Start Date ")

            self.ws['C9'] = 'Start Date'
            self.ws['G9'] = 'Fail'
            self.wb.save(self.filename)

    def End_Date(self):
        """

        """
        try:
            # Clicking on End Date
            self.driver.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-event-modal/mat-dialog-content/mat-horizontal-stepper/div[2]/div[2]/form/div[2]/div[2]/mat-form-field/div/div[1]/div[1]/input').click()
            time.sleep(5)
            print("\n 17 - Clicking on End Date Calander ")

            self.driver.find_element(By.XPATH,'//*[@id="mat-datepicker-0"]/div/mat-month-view/table/tbody/tr[2]/td[2]/div[1]').click()
            time.sleep(5)

            self.ws['C10'] = 'End Date'
            self.ws['G10'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN End Date  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 17 - Unable to Add End Date ")

            self.ws['C10'] = 'End Date'
            self.ws['G10'] = 'Fail'
            self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = Login()
    tb.setExternalDriver(driver=driver)
    tb.MFA()
    tb.Events()
    tb.Add_Banner_Image()
    tb.Add_Listing_Image()
    tb.Event_Name()
    tb.Description()
    tb.Next_Button()
    tb.Event_Name()
    tb.Start_Date()
    tb.End_Date()
    
