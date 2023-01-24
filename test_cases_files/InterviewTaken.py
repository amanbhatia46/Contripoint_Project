from Functionals import *
from datainputs import *


class ITAuth(unittest.TestCase):

    def __init__(self):
        """ interact with the underlying operating system."""
        import os
        print(os.path.join(os.getcwd() + "\\xyz.xlsx"), ">>>>>>")
        self.filename = os.path.join(os.getcwd() + "\\xyz.xlsx")
        self.wb = load_workbook(filename=self.filename)
        self.index_sheet = 0
        if 'Interview Taken' not in self.wb.sheetnames:
            self.wb.create_sheet('Interview Taken')
            self.wb.save(os.path.join(os.getcwd() + "\\xyz.xlsx"))
        self.wb = load_workbook(filename=self.filename)
        self.ws = self.wb.active
        for i, n in enumerate(self.wb.sheetnames):
            if n == 'Interview Taken':
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
        self.wb.save(os.path.join(os.getcwd() + "\\xyz.xlsx"))

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

            # driver = self.driver

            self.driver.get(
                "https://dev-contripoint.geminisolutions.com/#/dashboard")

            time.sleep(5)

            print("\n Login Successfull \n")

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

    def Interview_taken(self):
        """

        """
        try:
            """Selecting Interview Taken"""
            self.driver.find_element(
                By.XPATH, '//div[text()="Interviews Taken"]').click()
            print("\n 2 - Selecting 'Interview Taken' successfully")
            self.ws['C3'] = 'Interview Taken'
            self.ws['G3'] = 'Pass'
            time.sleep(4)

        except Exception as e:
            print("\n\nERROR IN Interview Taken >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 2 - Selecting Interview Taken gets fail")
            self.ws['C3'] = 'Interview Taken'
            self.ws['G3'] = 'Fail'

            self.wb.save(self.filename)

            print("\n 3 - sample test case of entering 'Interview Taken' successfully open")

    def Add_New_Button(self):
        """

        """
        try:
            ''' Scroll to the page top '''
            self.driver.execute_script("window.scroll(0, 0);")
            time.sleep(5)

            button = self.driver.find_element(
                By.XPATH, "//button[@id='add_btn']").click()
            time.sleep(6)
            print("\n 4 - 'Add New' button gets selected")
            self.ws['C4'] = 'Add New Button'
            self.ws['G4'] = 'Pass'

            self.wb.save(self.filename)
            time.sleep(4)

        except Exception as e:
            print("\n\nERROR IN Adding New Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 4 - Add New button gets fail")
            self.ws['C4'] = 'Add New Button'
            self.ws['G4'] = 'Fail'

            self.wb.save(self.filename)

    def Interview_position(self):
        """

        """
        try:
            # # position for which Interview was taken
            c = self.driver.find_element(
                By.XPATH, '//span[text()="Select Position"]').click()
            print("\n 5 - position done")

            print("\n 6 - Selecting Positions from the drop down list . . .")

            BussinessAnalystwithCRM = self.driver.find_element(
                By.XPATH, '//mat-option[@ng-reflect-value="Business Analyst with CRM"]').click()
            print("\n 7 - Bussiness Analyst with CRM")
            time.sleep(3)
            CloudEngineer = self.driver.find_element(
                By.XPATH, '//mat-option[@ng-reflect-value="Cloud Engineer"]').click()
            print("\n 8 - Cloud Engineer")
            time.sleep(3)
            CollaborationPlatform = self.driver.find_element(
                By.XPATH, '//mat-option[@ng-reflect-value="Collaboration Platform Adminis"]').click()
            print("\n 9 - Collaboration Platform")
            time.sleep(3)
            AdministratorDevOpsEngineer = self.driver.find_element(
                By.XPATH, '//mat-option[@ng-reflect-value="Data Warehouse Developer"]').click()
            print("\n 10 - Data Warehouse Developer")
            time.sleep(6)

            self.ws['C5'] = 'Interview Position'
            self.ws['G5'] = 'Pass'

            self.wb.save(self.filename)
            time.sleep(4)

        except Exception as e:
            print("\n\nERROR IN Interview Position >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 5 - Interview Position gets fail")
            self.ws['C5'] = 'Interview Position'
            self.ws['G5'] = 'Fail'

            self.wb.save(self.filename)

    def ExperienceLevel(self):
        """

        """
        try:
            ExpLevel = self.driver.find_element(
                By.CSS_SELECTOR, ".cdk-overlay-transparent-backdrop").click()
            time.sleep(5)
            
            self.driver.find_element(
                By.XPATH, '//span[text()="Select Interviewee Experience Level"]').click()
            print("\n 11 - Selecting 'Interviewee Exp Level'")
            time.sleep(6)

            self.driver.find_element(
                By.XPATH, '//mat-option[@ng-reflect-value="Junior (Less than 5 years)"]').click()
            print("\n 12 - Junior (Less than 5 years)")

            self.ws['C6'] = 'Experience Level'
            self.ws['G6'] = 'Pass'

            self.wb.save(self.filename)
            time.sleep(4)

        except Exception as e:
            print("\n\nERROR IN Experience Level >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Selecting Experience Level gets fail")
            self.ws['C6'] = 'Experience Level'
            self.ws['G6'] = 'Fail'

            self.wb.save(self.filename)

    def No_of_InterviewTaken(self):
        """

        """
        try:
            Interview_Number = self.driver.find_element(
                By.XPATH, '//input[@placeholder="No. Of Interview Taken In A Month "]').send_keys("2")
            print("\n 13 - Adding No. of Interview Taken")
            time.sleep(6)

            self.ws['C7'] = 'No. of Interview Taken'
            self.ws['G7'] = 'Pass'

            self.wb.save(self.filename)
            time.sleep(4)

        except Exception as e:
            print("\n\nERROR IN No. of Interview Taken >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 13 - No. of Interview Taken gets fail")
            self.ws['C7'] = 'No. of Interview Taken'
            self.ws['G7'] = 'Fail'

            self.wb.save(self.filename)

    def Interview_Month(self):
        """

        """
        try:
            Interview_Month = self.driver.find_element(
                By.XPATH, '//span[text()="Select Month"]').click()
            print("\n 14 -Selecting the Month . . . ")
            time.sleep(6)

            Month = ActionChains(self.driver).move_to_element(self.driver.find_element(
                By.XPATH, '//span[text()=" January "]')).click().perform()
            print("\n 15 - Selecting 'JANUARY' Month from the list")
            time.sleep(6)

            self.ws['C8'] = 'Interview Month'
            self.ws['G8'] = 'Pass'

            self.wb.save(self.filename)
            time.sleep(4)

        except Exception as e:
            print("\n\nERROR IN Interview Month >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 13 - Selecting Interview Month gets fail")
            self.ws['C8'] = 'Interview Month'
            self.ws['G8'] = 'Fail'

            self.wb.save(self.filename)

    def Goal_Type(self):
        """

        """
        try:
            # Goal Type-
            self.driver.find_element(
                By.XPATH, '//span[text()="Engineering Council (EC)"]').click()
            print("\n 14 - Selecting Goal Type- Engineering Council (EC)")
            self.ws['C9'] = 'Engineering Council (EC)'
            self.ws['G9'] = 'Pass'

            self.wb.save(self.filename)
            time.sleep(3)

        except Exception as e:
            print("\n\nERROR IN Goal Type >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 14 - Unable to select Goal_Type")
            self.ws['C9'] = 'Engineering Council (EC)'
            self.ws['G9'] = 'Fail'

            self.wb.save(self.filename)


    def Description(self):
        """

        """
        try:
            self.driver.find_element(
                By.XPATH,'//textarea[@formcontrolname="description"]').send_keys("Automation testing")
            time.sleep(4)
            print("\n 15 - Entering Description Done")
            self.ws['C10'] = 'Description'
            self.ws['G10'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN Project Status >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 15 - Entering Description gets fail")
            self.ws['C10'] = 'Description'
            self.ws['G10'] = 'Fail'
            self.wb.save(self.filename)

    def Submit(self):
        """

        """
        try:
            Submit = self.driver.find_element(
                By.XPATH, '//button[@id="add_btn"]')
            Submit.click()
            print("\n 16 - All Details get submit successfully.")
            time.sleep(6)

            self.ws['C11'] = 'Submit'
            self.ws['G11'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN SUBMIT  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 16 - Unable to Click Submit Button")
            self.ws['C11'] = 'Submit'
            self.ws['G11'] = 'Fail'

            self.wb.save(self.filename)
            time.sleep(3)

    def OK_Button(self):
        """

        """
        try:
            OK = self.driver.find_element(
                By.XPATH, '//span[text()="OK"]').click()
            print("\n 17 - Clicking OK Button")
            self.ws['C12'] = 'OK Button'
            self.ws['G12'] = 'Pass'
            time.sleep(4)
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN OK Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 17 - Unable to Click OK Button")
            self.ws['C12'] = 'OK Button'
            self.ws['G12'] = 'Fail'

            self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = ITAuth()
    tb.setUp()
    tb.Interview_taken()
    tb.Add_New_Button()
    tb.Interview_position()
    tb.ExperienceLevel()
    tb.No_of_InterviewTaken()
    tb.Interview_Month()
    tb.Goal_Type()
    tb.Description()
    tb.Submit()
    tb.OK_Button()

    # unittest.main()
#    unittest.main(testRunner= x.HTMLTestRunner( '/home/am.bhatia/Desktop/ContriPoint/testsuits'))
