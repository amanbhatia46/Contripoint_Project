# '''
# FUncitonal

# '''
# from lib2to3.pgen2 import driver
# from optparse import Option
# import unittest
# import time
# import HtmlTestRunner as x
# import pyautogui
# from multiprocessing import Event
# from traceback import print_exc
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from openpyxl import load_workbook
# from datetime import datetime, timedelta

# from datainputs import *

# class CAuth(unittest.TestCase):
    
#     def __init__(self): 

#         """ interact with the underlying operating system."""
#         import os
#         print(os.path.join(os.getcwd()+ "\\xyz.xlsx"),">>>>>>")
#         self.filename = os.path.join(os.getcwd()+ "\\xyz.xlsx")
#         self.wb = load_workbook(filename=self.filename)
#         self.index_sheet = 0
#         if 'certifications' not in self.wb.sheetnames:
#             self.wb.create_sheet('certifications')
#             self.wb.save(os.path.join(os.getcwd()+ "\\xyz.xlsx"))
#         self.wb = load_workbook(filename=self.filename)
#         self.ws = self.wb.active
#         for i, n in enumerate(self.wb.sheetnames):
#             if n == 'certifications':
#                 self.index_sheet = i
#                 break
#         self.wb.active = self.index_sheet
#         self.ws = self.wb.active  
#         self.wb.active = 1
#         self.ws['A1'] = 'Email'
#         self.ws['B1'] = 'Password'
#         self.ws['C1'] = 'Test Case Module'
#         self.ws['G1'] = 'Result'
#         self.ws['H1'] = 'Date and Time'
#         self.wb.save(os.path.join(os.getcwd()+ "\\xyz.xlsx"))

#         # datetime object containing current date and time
#         futuredate = str(datetime.now())
#         print(futuredate)
#         self.ws['H2'] = futuredate

#     def setUp(self):
#         try:
 

#             # Chrome_options =Options()
#             # ChromeDriverManager.chromedriver().setup()
#             # opt.setExperimentalOption("debuggerAddress", "localhost:9222")
#             # self.driver=webdriver.Chrome(Option)
#             # driver.manage().deleteAllCookies()
#             # driver.manage().timeouts().implicitlyWait(20)
#             # driver.manage().window().maximize()


#             Chrome_options =Options()
#             Option.setExperimentalOption("debuggerAddress", "localhost:9222");
#             driver=webdriver.Chrome(Option)
            
#             # import os
#             # s=Service( executable_path="chromedriver.exe")
#             # chrome_options = Options()
#             # chrome_driver = "chromedriver.exe"
#             # chrome_options.add_experimental_option("debuggerAddress","localhost:9515") 
#             # self.driver = webdriver.Chrome(chrome_driver, options=chrome_options)
#             # print("\n\n\n\n\n>>>>>>>>> CERTIFICATIONS >>>>>>>>>>>>")

#             # driver = self.driver
#             # # driver.session_id = "b2e961955fcd438678b05fe13cda342c"
#             # # print(driver.session_id,">>>>>>>>>>>>>>>>>>>")
#             driver.maximize_window()
#             driver.get(
#                 "https://dev-contripoint.geminisolutions.com/#/login")
#             driver.implicitly_wait(10)  # seconds
#             button = driver.find_element(
#                 By.XPATH, '//button[contains(., "Login with Gemini mail")]')
#             button.click()
#             time.sleep(6)

#             window_handles = driver.window_handles
#             driver.switch_to.window(window_handles[1])
#             driver.find_element(
#                 By.XPATH, '//*[@id="i0116"]').send_keys(login_Id)
#             self.ws['A2'] = 'aman.bhatia@geminisolutions.in'
#             driver.find_element(
#                 By.XPATH, '//*[@id="idSIButton9"]').click()
#             time.sleep(3)

#             driver.find_element(
#                 By.XPATH, '//*[@id="i0118"]').send_keys(login_Password)
#             self.ws['B2'] = 'RitaNandini96'
#             driver.find_element(
#                 By.XPATH, '//*[@id="idSIButton9"]').click()
#             time.sleep(6)

#             # Entering Multi-factor Authentication (MFA) Code Manually
#             driver.find_element(By.ID, "idTxtBx_SAOTCC_OTC")
#             time.sleep(6)
#             print("\n Entering and Verifying MFA Code \n")

#             driver.find_element(
#                 By.XPATH, '//*[@id="idSubmit_SAOTCC_Continue"]').click() 
#             time.sleep(5)

#             driver.find_element(
#                 By.XPATH, '//*[@id="KmsiCheckboxField"]').click()
#             time.sleep(5)

#             driver.find_element(By.ID, "idSIButton9").click()

#             print("\n Login Successfull \n")


#             driver.switch_to.window(window_handles[0])
#             time.sleep(6)
#             print("\n 1 - Gemini Id and Password successfully login")
#             self.ws['C2'] = 'Login'
#             self.ws['G2'] = 'login Success'

#             self.wb.save(self.filename)

#         except Exception as e:
#             print(e)
#             print("\n 1 - Gemini Id and Password  login failed")
#             self.ws['C2'] = 'Login'
#             self.ws['G2'] = 'login failed'
#             self.wb.save(self.filename)



#      # As per unittest module, individual test should start with test_
#     def Certifications(self):
#         """

#         """
#         try:
#             #Certifications
#             a = self.driver.find_element(By.XPATH,'//div[text()="Certificate"]')
#             a.click()
#             print("\n 2 - Selecting 'Certifications' successfully")
#             self.ws['C3'] = 'Certifications'
#             self.ws['G3'] = 'Pass'

#             self.wb.save(self.filename)

#             time.sleep(3)
        
#         except Exception as e:
#             print("\n\nERROR IN Certifications >>>>>>>>>>>>>>>\n\n")
#             print(e)
#             print("\n 2 - Selecting 'Certifications' get fail")
#             self.ws['C3'] = 'Certifications'
#             self.ws['G3'] = 'Fail'
#             self.wb.save(self.filename)

#     def Add_New_Contribution(self):
#         """

#         """
#         try:
#             #Adding New Contribution
#             self.driver.execute_script("window.scrollTo(0,100)")

#             self.driver.find_element(By.XPATH,'//*[@id="add_btn"]').click()
#             time.sleep(6)
#             print("\n 3 - Add New Contribution button gets selected")
#             self.ws['C4'] = 'Add New Contribution'
#             self.ws['G4'] = 'Pass'

#             self.wb.save(self.filename)

#         except Exception as e:
#             print("\n\nERROR IN Adding New Contribution >>>>>>>>>>>>>>>\n\n")
#             print(e)
#             print("\n 3 - Add New Contribution button gets fail")
#             self.ws['C4'] = 'Add New Contribution'
#             self.ws['G4'] = 'Fail'

#             self.wb.save(self.filename)

#     def Name_Of_Certification(self):
#         """

#         """
#         try:
#             #NAME OF CERTIFICATION-
#             self.driver.find_element(By.XPATH,'//*[@id="mat-input-0"]') .send_keys('Python')           
#             print("\n 4 - Name Of Certification - 'Python'")
#             self.ws['C5'] = 'Name Of Certification'
#             self.ws['G5'] = 'Pass'

#             self.wb.save(self.filename)
#             time.sleep(3)

#         except Exception as e:
#             print("\n\nERROR IN Name Of Certificate >>>>>>>>>>>>>>>\n\n")
#             print(e)
#             print("\n 4 - Unable to select Name Of Certification from dropdown list ")
#             self.ws['C5'] = 'Name Of Certification'
#             self.ws['G5'] = 'Fail'

#             self.wb.save(self.filename)

            
#     def Date_Of_Completion(self):
#         """

#         """
#         try:
#             #Selecting Date of completion-
#             datefield = self.driver.find_element(By.XPATH,'//*[@id="mat-dialog-0"]/app-certificate-add-modal/div/mat-dialog-content/form/div/div[2]/div/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button').click()
#             datefield = self.driver.find_element(By.XPATH,"//div[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']").click()
#             print("\n 5 - Date of completion done")
#             self.ws['C6'] = 'Date of completion'
#             self.ws['G6'] = 'Pass'

#             self.wb.save(self.filename)
#             time.sleep(3)

#         except Exception as e:
#             print("\n\nERROR IN Date of Completion >>>>>>>>>>>>>>>\n\n")
#             print(e)
#             print("\n 5 - Date of completion gets fail")
#             self.ws['C6'] = 'Date of completion'
#             self.ws['G6'] = 'Fail'

#             self.wb.save(self.filename)

#     def Uploading_Attachment(self):
#         """

#         """
#         try:
#             #Uploading Attatchment-
#             self.driver.find_element(By.XPATH,'//*[@id="attachment_btn"]').click()
#             time.sleep(8)
#             pyautogui.write("C:\\Users\\Aman Bhatia\\OneDrive - Gemini Solutions\\Desktop\\wallpaper\\1.jpeg")
#             pyautogui.press('enter') 
#             print("\n 6 - Attachment Upload successfully")
#             self.ws['C7'] = 'Upload attatchment'
#             self.ws['G7'] = 'Pass'

#             self.wb.save(self.filename)
#             time.sleep(3)

#         except Exception as e:
#             print("\n\nERROR IN Uploading Attatchment >>>>>>>>>>>>>>>\n\n")
#             print(e)
#             print("\n 6 - Unable to upload the attatchment")
#             self.ws['C7'] = 'Upload attatchment'
#             self.ws['G7'] = 'Fail'

#             self.wb.save(self.filename)

#     def Technology(self):
#         """

#         """
#         try:
#             #Technology-
#             self.driver.find_element(By.XPATH,'//*[text()="Select Technology"]').click()
#             print("\n 7 - Selecting Technology. . .")
#             self.ws['C8'] = 'Date of completion'
#             self.ws['G8'] = 'Pass'

#             self.wb.save(self.filename)
#             time.sleep(3)

#             self.driver.find_element(By.XPATH,'//*[text()="Android"]').click()
#             print("\n 8 - 'ANDROID' got selected from Technology")
            
#             time.sleep(3)

#         except Exception as e:
#             print("\n\nERROR IN TECHNOLOGY >>>>>>>>>>>>>>>\n\n")
#             print(e)
#             print("\n 7 - Unable to select Technology from dropdown list")
#             self.ws['C8'] = 'Technology'
#             self.ws['G8'] = 'Fail'

#             self.wb.save(self.filename)


#     def Goal_Type(self):
#         """

#         """
#         try:
#             #Goal Type-
#             self.driver.find_element(By.XPATH,'//*[text()="Engineering Council (EC)"]').click()
#             print("\n 8 - Selecting Goal Type- Engineering Council (EC)")
#             self.ws['C9'] = 'Engineering Council (EC)'
#             self.ws['G9'] = 'Pass'

#             self.wb.save(self.filename)
#             time.sleep(3)

#         except Exception as e:
#             print("\n\nERROR IN Goal Type >>>>>>>>>>>>>>>\n\n")
#             print(e)
#             print("\n 8 - Unable to select Goal_Type")
#             self.ws['C9'] = 'Engineering Council (EC)'
#             self.ws['G9'] = 'Fail'

#             self.wb.save(self.filename)


#     def Submit(self):
#         """

#         """
#         try:
#             #SUBMIT
#             element = self.driver.find_element(By.XPATH, '//*[contains(text(),"SUBMIT")]')
#             actions = ActionChains(self.driver)
#             actions.move_to_element(element).click().perform()

#             self.driver.find_element(
#                 By.CSS_SELECTOR, ".col-xs-3 > #add_btn").click()
#             print("\n 9 - All Details get SUBMIT successfully.")
#             self.ws['C10'] = 'Submit'
#             self.ws['G10'] = 'Pass'
#             self.wb.save(self.filename)
#             time.sleep(5)

#             #OK Button
#             assert self.driver.find_element(
#                 By.CSS_SELECTOR, "#ok_btn > .mat-button-wrapper").text == "OK"
#             time.sleep(5)

#             element = self.driver.find_element(By.ID, "ok_btn")
#             actions = ActionChains(self.driver)
#             actions.move_to_element(element).perform()
#             time.sleep(5)

#             self.driver.find_element(By.ID, "ok_btn").click()
#             print("\n 10 - Clicking OK Button")
#             time.sleep(3)

#         except Exception as e:
#             print("\n\nERROR IN SUBMIT  >>>>>>>>>>>>>>>\n\n")
#             print(e)
#             print("\n 9 - Unable to Click Submit Button")
#             self.ws['C10'] = 'Submit'
#             self.ws['G10'] = 'Fail'

#             self.wb.save(self.filename)
#             time.sleep(3)



#     # Anything declared in tearDown will be executed for all test cases
#     def tearDown(self):
#         self.driver.quit()


# if __name__ == '__main__':
#     tb = CAuth()
#     tb.setUp()
#     tb.Certifications()
#     tb.Add_New_Contribution()
#     tb.Name_Of_Certification()
#     tb.Date_Of_Completion()
#     tb.Uploading_Attachment()
#     tb.Goal_Type()
#     tb.Technology()
#     tb.Submit()
#     #unittest.main()
#     #unittest.main(testRunner= x.HTMLTestRunner( 'C:Users/Aman Bhatia/OneDrive - Gemini Solutions/Desktop/Contripoint_Project/testsuits'))
