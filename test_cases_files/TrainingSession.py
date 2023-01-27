from Functionals import *
from datainputs import *


class TSAuth(unittest.TestCase):

    def __init__(self):
        
        """ interact with the underlying operating system."""
        import os
        print(os.path.join(os.getcwd()+ "\\result.xlsx"),">>>>>>")
        self.filename = os.path.join(os.getcwd()+ "\\result.xlsx")
        self.wb = load_workbook(filename=self.filename)
        self.index_sheet = 0
        if 'TrainingSessions' not in self.wb.sheetnames:
            self.wb.create_sheet('TrainingSessions')
            self.wb.save(os.path.join(os.getcwd()+ "\\result.xlsx"))
        self.wb = load_workbook(filename=self.filename)
        self.ws = self.wb.active
        for i, n in enumerate(self.wb.sheetnames):
            if n == 'TrainingSessions':
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
        self.wb.save(os.path.join(os.getcwd()+ "\\result.xlsx"))


        # datetime object containing current date and time
        futuredate = str(datetime.now())
        print(futuredate)
        self.ws['H2'] = futuredate

    def setUp(self):
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option('debuggerAddress', 'localhost:9222')
            
            self.driver = webdriver.Chrome(options=chrome_options,executable_path="C:\\Users\\Aman Bhatia\\OneDrive - Gemini Solutions\\Desktop\\Contripoint_Project\\ChromeDriver\\chromedriver.exe")
            print("Browser Connected")

            self.driver.implicitly_wait(15)

            self.driver.get(
                "https://dev-contripoint.geminisolutions.com/#/dashboard")

            

            print("\n Login Successfull \n")
            
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


    def Training_Session(self):
        """

        """
        try:
            # Training&Session
            trainingsession = self.driver.find_element(
                By.XPATH, '//div[text()="Training & Sessions"]')
            trainingsession.click()
            print("\n 2 - Selecting 'TRAINING & SESSION'")
            
            self.ws['C3'] = 'TRAINING & SESSION'
            self.ws['G3'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN TRAINING & SESSION >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 2 - Selecting TRAINING & SESSION gets fail")
            self.ws['C3'] = 'TRAINING & SESSION'
            self.ws['G3'] = 'Fail'

            self.wb.save(self.filename)

    def Add_New(self):
        """

        """
        try:
            # ADD NEW
            ''' Scroll to the page top '''
            self.driver.execute_script("window.scroll(0, 0);")
            

            button = self.driver.find_element(
                By.XPATH, "//button[@id='add_btn']").click()

            print("\n 3 - 'Add New' button gets selected")
            
            self.ws['C4'] = 'Add New Button'
            self.ws['G4'] = 'Pass'

            self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN Adding New Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 3 - Add New button gets fail")
            self.ws['C4'] = 'Add New Button'
            self.ws['G4'] = 'Fail'

            self.wb.save(self.filename)

    def SessionName(self):
        """

        """
        try:
            time.sleep(5)
            # sessionName
            self.driver.find_element(
                By.XPATH,'//input[@type="text" and @formcontrolname="summary"]').send_keys("Selenium with Python")

            print("\n 4 - Name of Training & Session Conducted - 'Selenium with Python'")
            self.ws['C5'] = 'SessionName'
            self.ws['G5'] = 'Pass'
            self.wb.save(self.filename)
            

            # SessionsHeadcount
            self.driver.find_element(
                By.XPATH, '//input[@formcontrolname="activityCount"]').send_keys("2")
            print("\n 5 - Sessions Done ")
            

        except Exception as e:
            print("\n\nERROR IN SESSION NAME >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 4 - Adding SessionName gets fail")
            self.ws['C5'] = 'SessionName'
            self.ws['G5'] = 'Fail'

            self.wb.save(self.filename)

    def Description(self):
        """

        """
        try:
            # Enter Description
            Description = ActionChains(self.driver).move_to_element(self.driver.find_element(
                By.XPATH, '//textarea[@formcontrolname="description"]'))
            Description.click().perform()

            self.driver.find_element(
                By.XPATH,'//textarea[@formcontrolname="description"]').send_keys("Covered all the concepts of Selenium Pyhton")
            print("\n 6 - Description")
            self.ws['C6'] = 'Description'
            self.ws['G6'] = 'Pass'
            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Project Status >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 6 - Entering Description gets fail")
            self.ws['C6'] = 'Description'
            self.ws['G6'] = 'Fail'
            self.wb.save(self.filename)

    def NumberOfSessionProvided(self):
        """

        """
        try:
            # No. Of Training&Session Provided
            self.driver.find_element(By.XPATH,'//input[@formcontrolname="count"]').send_keys("5")
            print("\n 7 - No. Of Training & Session Provided")
            

            self.ws['C7'] = 'Number Of Session Provided'
            self.ws['G7'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN Number Of Session Provided >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 7 - Number Of Session Provided gets fail")
            self.ws['C7'] = 'Number Of Session Provided'
            self.ws['G7'] = 'Fail'
            self.wb.save(self.filename)

    def DateOfSession(self):
        '''
        '''
        try:
            #Start Date
            self.driver.find_element(By.XPATH,'//input[@formcontrolname="startDate"]').click()
            
            # actions = self.driver.find_element(
            #     By.XPATH, '//*[@id="mat-dialog-0"]/app-training-modal/div/mat-dialog-content/form/div[4]/div[2]/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button')
            # actions.click()
            

            self.driver.find_element(
                By.CSS_SELECTOR, ".mat-calendar-body-today").click()
            
            print("\n 8 - Start date done.")

            self.ws['C8'] = 'Start Date'
            self.ws['G8'] = 'Pass'
            self.wb.save(self.filename)

            #End Date
            self.driver.find_element(By.XPATH,'//input[@formcontrolname="endDate"]').click()
            

            self.driver.find_element(
                By.CSS_SELECTOR, ".mat-calendar-body-today").click()
            
            print("\n 9 - Start and End date done.")

            self.ws['C9'] = 'Session Date'
            self.ws['G9'] = 'Pass'
            self.wb.save(self.filename)


            print("\n 9 - Date Of Session Done")
            

        except Exception as e:
            print("\n\nERROR IN Date OF Session >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 9 - Date of Session gets fail")
            self.ws['C9'] = 'Date of Session'
            self.ws['G9'] = 'Fail'
            self.wb.save(self.filename)

    def Goal_Type(self):
        """

        """
        try:
            #Goal Type-
            self.driver.find_element(By.XPATH,'//*[text()="Engineering Council (EC)"]').click()
            print("\n 10 - Selecting Goal Type- Engineering Council (EC)")
            self.ws['C10'] = 'Engineering Council (EC)'
            self.ws['G10'] = 'Pass'

            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Goal Type >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 10 - Unable to select Goal_Type")
            self.ws['C10'] = 'Engineering Council (EC)'
            self.ws['G10'] = 'Fail'

    def Technology(self):
        """
        """
        try:
            # Technology Discussed
            self.driver.find_element(
                By.XPATH,'//span[text()="Select Technology *"]').click()
            print("\n 11 - Opening Technology List . . .")

            self.ws['C11'] = 'Technology Dropdown'
            self.ws['G11'] = 'Pass'
            self.wb.save(self.filename)
            

            self.driver.find_element(
                By.XPATH, '//mat-option[@ng-reflect-value="Automation Testing"]').click()
            print("\n 12 - 'Automation Testing' gets select from the list")
            

        except Exception as e:
            print("\n\nERROR IN Technology >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 -'Technology' gets fail")
            self.ws['C11'] = 'Technology'
            self.ws['G11'] = 'Fail'
            self.wb.save(self.filename)

    def Submit(self):
        """

        """
        try:
            # Submit
            submit= self.driver.find_element(
                By.XPATH, '//button[@type="submit"]')
            submit.click()
            

            print("\n 12 - All Details get submit successfully.")
            self.ws['C12'] = 'Submit'
            self.ws['G12'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN SUBMIT  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 12 - Unable to Click Submit Button")
            self.ws['C12'] = 'Submit'
            self.ws['G12'] = 'Fail'

            self.wb.save(self.filename)
            

    def OK_Button(self):
        """

        """
        try:
            # OK Button
            assert self.driver.find_element(
                By.CSS_SELECTOR, "#ok_btn > .mat-button-wrapper").text == "OK"
            

            element = self.driver.find_element(By.ID, "ok_btn")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            

            self.driver.find_element(By.ID, "ok_btn").click()
            print("\n 13 - Clicking OK Button")
            self.ws['C13'] = 'OK Button'
            self.ws['G13'] = 'Pass'

            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN OK Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 13 - Unable to Click OK Button")
            self.ws['C13'] = 'OK Button'
            self.ws['G13'] = 'Fail'

            self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = TSAuth()
    tb.setUp()
    tb.Training_Session()
    tb.Add_New()
    tb.SessionName()
    tb.NumberOfSessionProvided()
    tb.DateOfSession()
    tb.Technology()
    tb.Description()
    tb.Goal_Type()
    tb.Submit()
    tb.OK_Button()

    # unittest.main()
#    unittest.main(testRunner= x.HTMLTestRunner( '/home/am.bhatia/Desktop/ContriPoint/testsuits'))
