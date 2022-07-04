# from lib2to3.pgen2 import driver
# import unittest
# import time
# import HtmlTestRunner as x
# import pyautogui
# from multiprocessing import Event
# from traceback import print_exc
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from openpyxl import load_workbook
# from datetime import datetime, timedelta


# class Login(unittest.TestCase):

#     def __init__(self):
#         self.filename = '/home/am.bhatia/Desktop/contripoint/abc1.xlsx'
#         self.wb = load_workbook(filename=self.filename)
#         self.index_sheet = 0
#         if 'Login' not in self.wb.sheetnames:
#             self.wb.create_sheet('Login')
#             self.wb.save('/home/am.bhatia/Desktop/contripoint/abc1.xlsx')
#         self.wb = load_workbook(filename=self.filename)
#         self.ws = self.wb.active
#         for i, n in enumerate(self.wb.sheetnames):
#             if n == 'Login':
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
#         self.wb.save('/home/am.bhatia/Desktop/contripoint/abc1.xlsx')

#         # datetime object containing current date and time
#         futuredate = str(datetime.now())
#         print(futuredate)
#         self.ws['H2'] = futuredate

#     def setExternalDriver(self, driver):
#         s=Service(ChromeDriverManager().install())
#         self.driver = webdriver.Chrome(service=s)

        
#         self.driver =  driver
#         driver.maximize_window()
#         # y = self.driver.window_handles[0]
#         # time.sleep(6)
#         # self.driver.switch_to.window(y)

#     def loginMFA(self):
#         try:
#             # set implicit wait time
#             driver.implicitly_wait(10) # seconds

#             print("\n\n\n\n\n>>>>>>>>>> Login >>>>>>>>>>>>")

#             driver.maximize_window()

#             # get url
#             driver.get(
#                 "https://dev-contripoint.geminisolutions.com/#/login")
#             button = driver.find_element(
#                 By.XPATH, '/html/body/app-root/div/div/app-login-screen/div/div/div/mat-card/div[2]/div/button')
#             button.click()

#             print("\n\n Login With Gemini mail \n\n")
            
#             time.sleep(6)

#             window_handles = driver.window_handles
#             driver.switch_to.window(window_handles[1])
#             driver.find_element(
#                 By.XPATH, '//*[@id="i0116"]').send_keys('aman.bhatia@geminisolutions.com')
#             self.ws['A2'] = 'aman.bhatia@geminisolutions.com'

#             driver.find_element(
#                 By.XPATH, '//*[@id="idSIButton9"]/div/button/span').click()
#             time.sleep(3)

#             driver.find_element(
#                 By.XPATH, '//*[@id="i0118"]/div[1]/div/div[1]/input').send_keys('RitaNandini96')
#             self.ws['B2'] = 'RitaNandini96'
#             driver.find_element(
#                 By.XPATH, '//*[@id="idSIButton9"]/div/button/span').click()
#             time.sleep(6)

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

#     def tearDown(self):
#         self.driver.quit()


# if __name__ == '__main__':
#     tb = Login()
#     # login = Login()
#     # driver = login.LoginMFA()
#     tb.setExternalDriver(driver= driver)
#     tb.loginMFA()