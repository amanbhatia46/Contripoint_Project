'''
FUncitonal

'''
from logging import log
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

from datainputs import *

class Authentication(unittest.TestCase):

    def setUp(self):
        '''
          The setUp() methods allows to define set of instructions.If this method it self raises an exception while executing tests, the test methods will not be executed.
        '''
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)

    def test_login(self):
        '''
        The test_login() method helps us in executing the flow to login the url and reaches to it's main page. 
        It contains Gemini ID and password for authentication while login.
        '''
        try:
            print("\n\n\n\n\n>>>>>>>>>>LOGIN >>>>>>>>>>>>")
            
            driver = self.driver
            driver.maximize_window()
            
            driver.get(
                "https://dev-contripoint.geminisolutions.com/#/login")
            print("\n 1 - The TITLE of the page is: ", self.driver.title)
            print("\n 2 - The URL of the page is: ", self.driver.current_url)
            print("\n 3 - Now logging to the " + self.driver.title +
                  " by using Gemini ID and Password . . .")

            button = driver.find_element(
                By.XPATH, '/html/body/app-root/div/div/app-login-screen/div/div/div/mat-card/div[2]/div/button')
            button.click()
            time.sleep(6)

            window_handles = driver.window_handles
            driver.switch_to.window(window_handles[1])
            driver.find_element(
                By.XPATH, '//*[@id="identifierId"]').send_keys(login_Id)
            driver.find_element(
                By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
            time.sleep(3)

            driver.find_element(
                By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(login_Password)
            driver.find_element(
                By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
            time.sleep(6)

            driver.switch_to.window(window_handles[0])
            time.sleep(6)
            print("\n 4 - Gemini Id and Password successfully login")
            print(
                "\n 5 - You have login successfully and welcome to the site: " + self.driver.title)
            print("\n 6 - The TITLE of the page is: ", self.driver.title)
            print("\n 7 - The URL of the page is: ", self.driver.current_url)
            print("\n 8 - Login to contripoint is successfully completed")

        except Exception as e:
            print("\n\nERROR While LOGIN >>>>>>>>>>>>>>>\n\n")
            print(e)

    # using tearDown to close the file for us when it notices that the file object is dead, but this only occurs after some unknown time has elapsed.
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    unittest.main(testRunner= x.HTMLTestRunner( 'C:\Users\Aman Bhatia\OneDrive - Gemini Solutions\Desktop\Contripoint_Project\test_suits'))