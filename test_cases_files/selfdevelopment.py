from Functionals import *
from datainputs import *



class SDAuth(unittest.TestCase):

    def __init__(self):
        
        # """ interact with the underlying operating system."""
        # import os
        # print(os.path.join(os.getcwd()+ "\\result.xlsx"),">>>>>>")
        # self.filename = os.path.join(os.getcwd()+ "\\result.xlsx")
        # #self.wb = load_workbook(filename=self.filename)
        # self.index_sheet = 0
        # if 'SelfDevelopment' not in #self.wb.sheetnames:
        #     #self.wb.create_sheet('SelfDevelopment')
        #     #self.wb.save(os.path.join(os.getcwd()+ "\\result.xlsx"))
        # #self.wb = load_workbook(filename=self.filename)
        # #self.ws = #self.wb.active
        # for i, n in enumerate(#self.wb.sheetnames):
        #     if n == 'SelfDevelopment':
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
        # print(futuredate)
        # #self.ws['H2'] = futuredate
        pass

    def setUp(self):
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option('debuggerAddress', 'localhost:9222')
            
            self.driver = webdriver.Chrome(options=chrome_options,executable_path="C:\\Users\\Aman Bhatia\\OneDrive - Gemini Solutions\\Desktop\\Contripoint_Project\\ChromeDriver\\chromedriver.exe")
            print("Browser Connected")

            self.driver.implicitly_wait(20)

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

    def SelfDevelopment(self):
        '''

        '''
        try:
            
            # SelfDevelopment
            SelfDevelopment = self.driver.find_element(
                By.XPATH, '//div[text()="Self Development"]')
            SelfDevelopment.click()
            print("\n 2 - Selecting 'SelfDevelopment'")
            #self.ws['C3'] = 'SelfDevelopment'
            #self.ws['G3'] = 'Pass'
            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN SelfDevelopment >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 2 - Selecting SelfDevelopment gets fail")
            #self.ws['C3'] = 'SelfDevelopment'
            #self.ws['G3'] = 'Fail'

            #self.wb.save(self.filename)
            

    def Add_New(self):
        '''

        '''
        try:

            # ADD NEW
            ''' Scroll to the page top '''
            self.driver.execute_script("window.scroll(0, 0);")
            

            button = self.driver.find_element(
                By.XPATH, "//button[@id='add_btn']").click()
            print("\n 3 - Selecting 'Add New' button gets selected")
            
            #self.ws['C4'] = 'Add New Button'
            #self.ws['G4'] = 'Pass'

            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN Adding New Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 3 - Add New button gets fail")
            #self.ws['C4'] = 'Add New Button'
            #self.ws['G4'] = 'Fail'

            #self.wb.save(self.filename)


    def Skill_Name(self):
        '''

        '''
        try:
            self.driver.find_element(By.XPATH,'//input[@formcontrolname="summary"]').send_keys("Machine Learning")
            print("\n 4 - Name of Skill - 'Machine Learning'")
            
            #self.ws['C5'] = 'Skill_Name'
            #self.ws['G5'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Skill Name >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 4 - Adding Skill_Name gets fail")
            #self.ws['C5'] = 'Skill_Name'
            #self.ws['G5'] = 'Fail'

            #self.wb.save(self.filename)


    def Duration(self):
        ''' '''
        try:

            # Duration
            self.driver.find_element(By.XPATH,'//input[@formcontrolname="duration"]').send_keys("2")
            print("\n 5 - Duration in weeks- '2'")
            #self.ws['C6'] = 'Duration'
            #self.ws['G6'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Duration >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 5 - Adding Duration gets fail")
            #self.ws['C6'] = 'Duration'
            #self.ws['G6'] = 'Fail'

            #self.wb.save(self.filename)
            

    def StartDate(self):
        '''

        '''
        try:

            # Start Date
            self.driver.find_element(By.XPATH,'//input[@formcontrolname="date"]').click()
            print("\n 6 - Opening Calander . . .")
            

            self.driver.find_element(
                By.CSS_SELECTOR, ".mat-calendar-body-today").click()
            print("\n 7 - Date Done")
            
            #self.ws['C7'] = 'Start Date'
            #self.ws['G7'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Start Date >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 7 - Start Date gets fail")
            #self.ws['C7'] = 'Start Date'
            #self.ws['G7'] = 'Fail'

            #self.wb.save(self.filename)

    def Description(self):
        """

        """
        try:
            #Enter Description
            self.driver.find_element(By.XPATH,'//textarea[@formcontrolname="description"]').send_keys(
                "Machine learning is the study of computer algorithms that can improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence")
            print("\n 8 - Entering Description Done")
            
            #self.ws['C8'] = 'Description'
            #self.ws['G8'] = 'Pass'
            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN Entering Description >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 8 - Entering Description gets fail")
            #self.ws['C8'] = 'Description'
            #self.ws['G8'] = 'Fail'
            #self.wb.save(self.filename)

    def Goal_Type(self):
        """

        """
        try:
            # Goal Type-
            self.driver.find_element(
                By.XPATH, '//span[text()="Delivery Council (DC)"]').click()
            

            print("\n 9 - Selecting Goal Type- Engineering Council (EC)")
            #self.ws['C9'] = 'Engineering Council (EC)'
            #self.ws['G9'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Goal Type >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 9 - Unable to select Goal_Type")
            #self.ws['C9'] = 'Engineering Council (EC)'
            #self.ws['G9'] = 'Fail'

            #self.wb.save(self.filename)

    def Submit(self):
        """

        """
        try:
            #SUBMIT
            assert self.driver.find_element(
                By.CSS_SELECTOR, ".col-xs-3 > #add_btn").text == "SUBMIT"
            

            Submit_button = ActionChains(self.driver).move_to_element(self.driver.find_element(
                By.XPATH, '//button[text()="SUBMIT"]'))
            Submit_button.click().perform()
            

            self.driver.find_element(
                By.XPATH, '//button[text()="SUBMIT"]').click()

            
            
            print("\n 10 - All Details get SUBMIT successfully.")
            #self.ws['C10'] = 'Submit'
            #self.ws['G10'] = 'Pass'
            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN SUBMIT  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 10 - Unable to Click Submit Button")
            #self.ws['C10'] = 'Submit'
            #self.ws['G10'] = 'Fail'

            #self.wb.save(self.filename)

    def OK_Button(self):
        """

        """
        try:

            #OK Button
            assert self.driver.find_element(By.XPATH,'//span[text()="OK"]').text == "OK"
            

            element = self.driver.find_element(By.XPATH,'//span[text()="OK"]')
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            

            self.driver.find_element(By.XPATH,'//span[text()="OK"]').click()
            print("\n 11 - Clicking OK Button")
            #self.ws['C11'] = 'OK Button'
            #self.ws['G11'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN OK Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Unable to Click OK Button")
            #self.ws['C11'] = 'OK Button'
            #self.ws['G11'] = 'Fail'

            #self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = SDAuth()
    tb.setUp()
    tb.SelfDevelopment()
    tb.Add_New()
    tb.Skill_Name()
    tb.Duration()
    tb.StartDate()
    tb.Description()
    tb.Goal_Type()
    tb.Submit()
    tb.OK_Button()
    # unittest.main()
    # unittest.main(testRunner= x.HTMLTestRunner( '/home/am.bhatia/Desktop/ContriPoint/testsuits'))

