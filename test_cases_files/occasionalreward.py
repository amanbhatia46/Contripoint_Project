from Functionals import *
from datainputs import *


class  AllotOccasionalReward (unittest.TestCase):

    def __init__(self):
        # """ interact with the underlying operating system."""
        # import os
        # print(os.path.join(os.getcwd() + "\\result.xlsx"), ">>>>>>")
        # self.filename = os.path.join(os.getcwd() + "\\result.xlsx")
        # #self.wb = load_workbook(filename=self.filename)
        # self.index_sheet = 0
        # if ' Allot Occasional Reward ' not in #self.wb.sheetnames:
        #     #self.wb.create_sheet(' Allot Occasional Reward ')
        #     #self.wb.save(os.path.join(os.getcwd() + "\\result.xlsx"))
        # #self.wb = load_workbook(filename=self.filename)
        # #self.ws = #self.wb.active
        # for i, n in enumerate(#self.wb.sheetnames):
        #     if n == ' Allot Occasional Reward ':
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
        # #self.wb.save(os.path.join(os.getcwd() + "\\result.xlsx"))

        # # datetime object containing current date and time
        # futuredate = str(datetime.now())
        # print(futuredate)
        # #self.ws['H2'] = futuredate
        pass

    def setUp(self):
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option(
                'debuggerAddress', 'localhost:9222')

            self.driver = webdriver.Chrome(
                options=chrome_options, executable_path="C:\\Users\\Aman Bhatia\\OneDrive - Gemini Solutions\\Desktop\\Contripoint_Project\\ChromeDriver\\chromedriver.exe")
            print("Browser Connected")

            self.driver.implicitly_wait(15)

            self.driver

            self.driver.get(
                "https://dev-contripoint.geminisolutions.com/#/dashboard")

            

            print("\n Login Successfull \n")

            print("\n 1 - Gemini Id and Password successfully login")
            #self.ws['C2'] = 'Login'
            #self.ws['G2'] = 'login Success'

            #self.wb.save(self.filename)

        except Exception as e:
            print(e)
            print("\n 1 - Gemini Id and Password  login failed")
            #self.ws['C2'] = 'Login'
            #self.ws['G2'] = 'login failed'
            #self.wb.save(self.filename)

    def Admin_Portal(self):
        """

        """
        try:

            # Clicking on Admin Portal
            self.driver.find_element(
                By.XPATH, '//a//img[@src="../../assets/images/Admin Portal icon.svg"]').click()
            
            print("\n 2 - Clicking on Admin Portal ")

            # Clicking Add New button
            self.driver.find_element(
                By.XPATH, '//button[text()=" ADD NEW "]').click()
            
            print("\n 3 - Add New button")

            print("\n 4 - Selecting Admin portal--Add New button button")
            #self.ws['C3'] = 'Admin Portal--Add New button'
            #self.ws['G3'] = 'Pass'

            #self.wb.save(self.filename)

        except Exception as e:
            print("\n 2 - Clicking on Admin Portal gets fail.")
            print("\n 3 - Selecting Add New button gets fail.")
            print(e)
            print("\n 4 - Error in selecting Admin portal--Add New button button")
            #self.ws['C3'] = 'Admin Portal--Add New button'
            #self.ws['G3'] = 'Fail'

            #self.wb.save(self.filename)

    def Allotment_Type(self):
        """
        """
        try:
            #selecting Dropdown
            self.driver.find_element(By.XPATH,'//mat-select[@formcontrolname="allotmentData"]').click()
            

            # Allot Occasional Reward 
            self.driver.find_element(By.XPATH,'//span[text()=" Allot Occasional Reward "]').click()
            
            
            print("\n 5 - Selecting ' Allot Occasional Reward '")
            #self.ws['C4'] = 'Dropdown-- Allot Occasional Reward '
            #self.ws['G4'] = 'Pass'

            #self.wb.save(self.filename)

        except Exception as e:
            print("\n 5 - Selecting ' Allot Occasional Reward ' gets fail")
            print(e)
            #self.ws['C4'] = 'Dropdown-- Allot Occasional Reward '
            #self.ws['G4'] = 'Pass'

            #self.wb.save(self.filename)

    def Title(self):
        """
        """
        try:
            #Occasional Reward Title
            self.driver.find_element(By.XPATH,'//input[@formcontrolname="title"]').send_keys("Employee budgets")            

            print("\n 6 - Enter Reward Title")
            #self.ws['C5'] = 'Reward Title'
            #self.ws['G5'] = 'Pass'

            #self.wb.save(self.filename)

        except Exception as e:
            print("\n 6 - Enter Reward Title gets fail")
            print(e)

            #self.ws['C5'] = 'Reward Title'
            #self.ws['G5'] = 'Fail'

            #self.wb.save(self.filename)

    def Import_excel(self):
        """
        """
        try:
            #Import Data from Excel Button
            self.driver.find_element(By.XPATH,'//button[text()=" IMPORT DATA FROM EXCEL "]').click()
            

            #Import Data Screen
            self.driver.find_element(By.XPATH,'//label[@id="attachment_btn"]').click()
            time.sleep(5)
            
            pyautogui.write(occasionalreward)
            
            pyautogui.press('enter')
            print("\n 7 - Budget Excel sheet Upload successfully")
            #self.ws['C5'] = ' Allot Occasional Reward  Excel sheet'
            #self.ws['G5'] = 'Pass'

            #self.wb.save(self.filename)

        except Exception as e:
            print("\n 7 - Budget Excel sheet Uploading gets fail")
            #self.ws['C5'] = ' Allot Occasional Reward  Excel sheet'
            #self.ws['G5'] = 'Fail'

            #self.wb.save(self.filename)

    def Submit(self):
        """
        """
        try:
            self.driver.find_element(By.XPATH,'//button[@id="add_btn" and text()=" SUBMIT "]').click()
            

            print("\n 8 - All Details get SUBMIT successfully.")

            #self.ws['C6'] = 'SUBMIT'
            #self.ws['G6'] = 'Pass'
            #self.wb.save(self.filename)
            
        
        except Exception as e:
            print("\n\nERROR IN SubmitButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 8 - All Details get fail while SUBMIT.")
            #self.ws['C6'] = 'SUBMIT'
            #self.ws['G6'] = 'Fail'
            #self.wb.save(self.filename)

    def OKButton(self):
        '''

        '''
        try:
            #OK Button
            self.driver.find_element(By.XPATH,'//span[text()="OK"]').click()
            print("\n 9 - Clicking OK Button")

            #self.ws['C7'] = 'OK BUTTON'
            #self.ws['G7'] = 'Pass'
            #self.wb.save(self.filename)
            

            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN OKButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 9 - Unable to click OK Button")
            #self.ws['C7'] = 'OK BUTTON'
            #self.ws['G7'] = 'Fail'
            #self.wb.save(self.filename)

    def Allot(self):
        """
        """
        try:
            time.sleep(4)
            #AllotButton
            Allot_btn = ActionChains(self.driver).move_to_element(self.driver.find_element(
                By.XPATH,'//button[@id="allot" and text()=" ALLOT "]'))
            Allot_btn.click().perform()           

            print("\n 10 - Alloting Budget(₹) to selected employees")

            #self.ws['C8'] = 'Allot Occasional Reward (₹)'
            #self.ws['G8'] = 'Pass'
            #self.wb.save(self.filename)
            

            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN OKButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 10 - Unable to Allot the Budget(₹)")
            #self.ws['C8'] = 'Alloting Budget(₹)'
            #self.ws['G8'] = 'Fail'
            #self.wb.save(self.filename)

    def OK(self):
        '''

        '''
        try:
            #OK Button
            self.driver.find_element(By.XPATH,'//button[@type="submit" and @id="ok_btn"]').click()
            print("\n 11 - Clicking OK Button")

            #self.ws['C9'] = 'OK BUTTON'
            #self.ws['G9'] = 'Pass'
            #self.wb.save(self.filename)
            

            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN OKButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Unable to click OK Button")
            #self.ws['C9'] = 'OK BUTTON'
            #self.ws['G9'] = 'Fail'
            #self.wb.save(self.filename) 


    def Table(self):
        '''

        '''
        try:

            #Occasional Reward Table
            self.driver.find_element(By.XPATH,'//div[text()="Occasional Rewards"]').click()
            print("\n 11 - Clicking Occasional Reward Button")

            #self.ws['C9'] = 'Occasional Reward BUTTON'
            #self.ws['G9'] = 'Pass'
            #self.wb.save(self.filename)

            ''' Scroll to the page down '''
            self.driver.execute_script("window.scroll(0, 300);")

        except Exception as e:
            print("\n\nERROR IN View Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Unable to click Occasional Reward Button")
            #self.ws['C9'] = 'Occasional Reward  BUTTON'
            #self.ws['G9'] = 'Fail'
            #self.wb.save(self.filename)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = AllotOccasionalReward()
    tb.setUp()
    tb.Admin_Portal()
    tb.Allotment_Type()
    tb.Title()
    tb.Import_excel()
    tb.Submit()
    tb.OKButton()
    tb.Allot()
    tb.OK()
    tb.Table()