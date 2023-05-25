from Functionals import *
from datainputs import *

class Login(unittest.TestCase):

    def __init__(self):
        
        # """ interact with the underlying operating system."""
        # import os
        # print(os.path.join(os.getcwd()+ "\\result.xlsx"),">>>>>>")
        # self.filename = os.path.join(os.getcwd()+ "\\result.xlsx")
        # #self.wb = load_workbook(filename=self.filename)
        # self.index_sheet = 0
        # if 'LoginMFA' not in #self.wb.sheetnames:
        #     #self.wb.create_sheet('LoginMFA')
        #     #self.wb.save(os.path.join(os.getcwd()+ "\\result.xlsx"))
        # #self.wb = load_workbook(filename=self.filename)
        # #self.ws = #self.wb.active
        # for i, n in enumerate(#self.wb.sheetnames):
        #     if n == 'LoginMFA':
        #         self.index_sheet = i
        #         break
        # #self.wb.active = self.index_sheet
        # #self.ws = #self.wb.active  
        # #self.wb.active = 1
        # #self.ws['A1'] = 'Email'
        # #self.ws['B1'] = 'Password'
        # #self.ws['C1'] = 'Test Case Module'
        # #self.ws['G1'] = 'Result'
        # #self.ws['H1'] = 'Date and Time'
        # #self.wb.save(os.path.join(os.getcwd()+ "\\result.xlsx"))

        # # datetime object containing current date and time
        # futuredate = str(datetime.now())
        # #self.ws['H2'] = futuredate
        pass
        
    def setExternalDriver(self):
        chrome_options = Options()
        chrome_options.add_experimental_option('debuggerAddress', 'localhost:9222')
            
        self.driver = webdriver.Chrome(options=chrome_options,executable_path="C:\\Users\\Aman Bhatia\\OneDrive - Gemini Solutions\\Desktop\\Contripoint_Project\\ChromeDriver\\chromedriver.exe")
        print("Browser Connected")

        self.driver.implicitly_wait(25)

        self.driver.get(
                "https://dev-contripoint.geminisolutions.com/#/dashboard")

            

        print("\n Login Successfull \n")

            
            
        print("\n 1 - Gemini Id and Password successfully login")
        #self.ws['C2'] = 'Login'
        #self.ws['G2'] = 'login Success'

        #self.wb.save(self.filename)

    def MFA(self):
            # set implicit wait time
            self.driver.implicitly_wait(10)  # seconds

            print("\n >>>>>>>>>> Login >>>>>>>>>>>> \n")

            # get url
            self.driver.get(
                "https://contripoint.geminisolutions.com/#/dashboard")
            button = self.driver.find_element(
                By.XPATH, '//button[contains(., "Login with Gemini mail")]')
            button.click()

            print("\n 1- Login With Gemini mail \n")

            

            window_handles = self.driver.window_handles
            self.driver.switch_to.window(window_handles[1])

            # Entering Mail Id in input
            self.driver.find_element(
                By.XPATH, '//*[@id="i0116"]').send_keys(login_Id)
            #self.ws['A2'] = '***@geminisolutions.com'
            print("\n 2- Entering mail id \n")

            self.driver.find_element(
                By.XPATH, '//*[@id="idSIButton9"]').click()
            

            # Entering Passowrd in Input
            self.driver.find_element(
                By.XPATH, '//*[@id="i0118"]').send_keys(login_Password)
            #self.ws['B2'] = 'RitaNandini96'
            print("\n 3- Entering mail password \n")

            time.sleep(4)
            self.driver.find_element(
                By.XPATH, '//*[@id="idSIButton9"]').click()
            
            # Entering Multi-factor Authentication (MFA) Code Manually
            time.sleep(10)
            self.driver.find_element(By.ID, "idTxtBx_SAOTCC_OTC")
            
            print("\n 4- Entering and Verifying MFA Code \n")

            self.driver.find_element(
                By.XPATH, '//*[@id="idSubmit_SAOTCC_Continue"]').click() 
            

            self.driver.find_element(
                By.XPATH, '//*[@id="KmsiCheckboxField"]').click()
            

            self.driver.find_element(By.ID, "idSIButton9").click()
            
            self.driver.switch_to.window(window_handles[0])
            print("\n 5- Gemini Id and Password successfully login \n")
            #self.ws['C2'] = 'Login'
            #self.ws['G2'] = 'login Success'

            #self.wb.save(self.filename)

            print(
                "\n 6 - You have login successfully and welcome to the site: " + self.driver.title)
            print("\n 7 - The URL of the page is: ", self.driver.current_url)
            print("\n 8 - All the details are successfully printed.")

            

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = Login()
    tb.setExternalDriver()
    tb.MFA()
    # unittest.main()
    # unittest.main(testRunner= x.HTMLTestRunner( 'C:\Users\Aman Bhatia\OneDrive - Gemini Solutions\Desktop\Contripoint_Project\test_suits'))
