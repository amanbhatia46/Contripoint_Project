'''
FUncitonal

'''
import unittest
import time
import HtmlTestRunner as x
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from json import load
from openpyxl import load_workbook
from datetime import datetime, timedelta


class CFAuth(unittest.TestCase):
    

    def __init__(self):
        
        """ interact with the underlying operating system."""
        import os
        print(os.path.join(os.getcwd()+ "\\xyz.xlsx"),">>>>>>")
        self.filename = os.path.join(os.getcwd()+ "\\xyz.xlsx")
        self.wb = load_workbook(filename=self.filename)
        self.index_sheet = 0
        if 'ClientFeedback' not in self.wb.sheetnames:
            self.wb.create_sheet('ClientFeedback')
            self.wb.save('/home/am.bhatia/Desktop/contripoint/xyz.xlsx')
        self.wb = load_workbook(filename=self.filename)
        self.ws = self.wb.active
        for i, n in enumerate(self.wb.sheetnames):
            if n == 'ClientFeedback':
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
        self.wb.save(os.path.join(os.getcwd()+ "\\xyz.xlsx"))


        # datetime object containing current date and time
        futuredate = str(datetime.now())
        print(futuredate)
        self.ws['H2'] = futuredate

    def setUp(self):
        try:
            s=Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=s)
            print("\n\n\n\n\n>>>>>>>>>> CLIENT FEEDBACK >>>>>>>>>>>>")

            driver = self.driver
            driver.maximize_window()
            driver.get(
                "https://dev-contripoint.geminisolutions.com/#/login")
            button = driver.find_element(
                By.XPATH, '/html/body/app-root/div/div/app-login-screen/div/div/div/mat-card/div[2]/div/button')
            button.click()
            time.sleep(6)

            window_handles = driver.window_handles
            driver.switch_to.window(window_handles[1])
            driver.find_element(
                By.XPATH, '//*[@id="identifierId"]').send_keys('aman.bhatia@geminisolutions.in')
            self.ws['A2'] = 'aman.bhatia@geminisolutions.in'
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
                   
    def Clientfeedback(self):
        '''

        '''
        try:
            
            #ClientFeedback
            clientfeedback = self.driver.find_element(
                By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[3]/app-dash-cards/div/div[3]/div[1]/mat-card/mat-card-header')
            clientfeedback.click()
            print("\n 2 - Selecting 'ClientFeedback'")
            self.ws['C3'] = 'Selecting ClientFeedback'
            self.ws['G3'] = 'Pass'
            self.wb.save(self.filename)
            time.sleep(6)

        except Exception as e:
            print("\n\nERROR IN CLIENT FEEDBACK >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 2 - Selecting 'ClientFeedback' gets failed")
            self.ws['C3'] = 'Selecting ClientFeedback'
            self.ws['G3'] = 'Fail'
            self.wb.save(self.filename)


    def AddNew(self):
        '''

        '''
        try:
            #ADD NEW
            element = self.driver.find_element(
                By.XPATH, '/html/body/app-root/div[3]/div/app-feedback-table/div/div/div/div[2]/div/div/div/div[2]/ul/div/button')
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            print("\n 3 - Selecting 'Add New' button gets selected")
            self.ws['C4'] = 'Add New'
            self.ws['G4'] = 'Pass'
            self.wb.save(self.filename)
            time.sleep(6)

        except Exception as e:
            print("\n\nERROR IN ADD NEW  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 3 - Selecting 'Add New' button gets fail")
            self.ws['C4'] = 'Add New'
            self.ws['G4'] = 'Fail'
            self.wb.save(self.filename)


    def ProjectName(self):
        '''

        '''
        try:
            #ProjectName
            self.driver.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-feedback-modal/div/mat-dialog-content/form/div/div[1]/div/mat-form-field/div/div[1]/div/input').send_keys('Skedular')
            print("\n 4 - Project Name Done")
            self.ws['C5'] = 'Project Name'
            self.ws['G5'] = 'Pass'
            self.wb.save(self.filename)
            time.sleep(5)

        except Exception as e:
            print("\n\nERROR IN PROJECT NAME >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 4 - Unable to fill Project name")
            self.ws['C5'] = 'Project Name'
            self.ws['G5'] = 'Fail'
            self.wb.save(self.filename)


    def ClientName(self):
        '''

        '''
        try:
            #ClientName
            self.driver.find_element(
                By.ID, "mat-input-1").send_keys("auto-skedular")
            print("\n 5 - Client Name Done")
            self.ws['C6'] = 'Client Name'
            self.ws['G6'] = 'Pass'
            self.wb.save(self.filename)
            time.sleep(5)

        except Exception as e:
            print("\n\nERROR IN CLIENT NAME >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 5 - Unable to fill Client name")
            self.ws['C6'] = 'Client Name'
            self.ws['G6'] = 'Fail'
            self.wb.save(self.filename)

    def Enter_ClientFeedback(self):
        '''

        '''
        try:
            #Enter Client Feedback
            self.driver.find_element(
                By.ID, "mat-input-2").send_keys("US client")
            print("\n 6 - Client Feedback Done")
            self.ws['C7'] = 'Enter Client Feedback'
            self.ws['G7'] = 'Pass'
            self.wb.save(self.filename)
            time.sleep(5)

        except Exception as e:
            print("\n\nERROR IN CLIENT FEEDBACK >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 6 - Unable to fill Client Feedback")
            self.ws['C7'] = 'Enter Client Feedback'
            self.ws['G7'] = 'Fail'
            self.wb.save(self.filename)


    def Upload_attatchment(self):
        '''

        '''
        try:
            #Upload Attachment
            assert self.driver.find_element(
                By.ID, "attachment_btn").text == "Upload attachment"

            print("\n 7 - Uploading Attatchment . . . ")
            self.wb.save(self.filename)
            time.sleep(5)

            self.driver.find_element(By.ID, "attachment_btn").click()
            print("\n 8 - Selecting Attachment from Drive . . .")
            time.sleep(5)

            self.driver.find_element(By.ID, "firsting").send_keys(
                '/home/am.bhatia/Desktop/image.jpeg')
            print("\n 9 - Attatchment Successfully upload")
            self.ws['C8'] = 'Upload attatchment'
            self.ws['G8'] = 'Pass'
            self.wb.save(self.filename)
            time.sleep(5)

        except Exception as e:
            print("\n\nERROR IN UPLOAD ATTACHMENT >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 9 - Unable to upload attatchment")
            self.ws['C8'] = 'Upload attatchment'
            self.ws['G8'] = 'Fail'
            self.wb.save(self.filename)


    def Submit(self):
        '''

        '''
        try:
            #SUBMIT
            assert self.driver.find_element(
                By.CSS_SELECTOR, ".col-xs-3 > #add_btn > .mat-button-wrapper").text == "SUBMIT"

            self.driver.find_element(
                By.CSS_SELECTOR, ".col-xs-3 > #add_btn").click()

            print("\n 10 - All Details get SUBMIT successfully.")
            self.ws['C9'] = 'Submit'
            self.ws['G9'] = 'Pass'
            self.wb.save(self.filename)
            time.sleep(5)

        except Exception as e:
            print("\n\nERROR IN SUBMIT >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 10 - Unable to submit all details")
            self.ws['C9'] = 'Submit'
            self.ws['G9'] = 'Fail'
            self.wb.save(self.filename)



    def OK_Button(self):
        '''

        '''
        try:
            #OK Button
            assert self.driver.find_element(
                By.CSS_SELECTOR, "#ok_btn > .mat-button-wrapper").text == "OK"
            time.sleep(5)

            element = self.driver.find_element(By.ID, "ok_btn")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            time.sleep(5)

            self.driver.find_element(By.ID, "ok_btn").click()
            print("\n 11 - Clicking OK Button")
            self.ws['C10'] = 'OK Button'
            self.ws['G10'] = 'Fail'
            self.wb.save(self.filename)
            time.sleep(5)

        except Exception as e:
            print("\n\nERROR IN OKButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Unable to Click OK Button")
            self.ws['C10'] = 'OK Button'
            self.ws['G10'] = 'Fail'
            self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = CFAuth()
    tb.setUp()
    tb.Clientfeedback()
    tb.AddNew()
    tb.ProjectName()
    tb.ClientName()
    tb.Enter_ClientFeedback()
    tb.Upload_attatchment()
    tb.Submit()
    tb.OK_Button()
    
    # unittest.main()
    # unittest.main(testRunner= x.HTMLTestRunner( '/home/am.bhatia/Desktop/ContriPoint/testsuits'))

