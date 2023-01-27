from Functionals import *
from datainputs import *


class MAuth(unittest.TestCase):

    def __init__(self):
        """ interact with the underlying operating system."""
        # import os
        # print(os.path.join(os.getcwd() + "\\result.xlsx"), ">>>>>>")
        # self.filename = os.path.join(os.getcwd() + "\\result.xlsx")
        # #self.wb = load_workbook(filename=self.filename)
        # self.index_sheet = 0
        # if 'Mentorship' not in #self.wb.sheetnames:
        #     #self.wb.create_sheet('Mentorship')
        #     #self.wb.save(os.path.join(os.getcwd() + "\\result.xlsx"))
        # #self.wb = load_workbook(filename=self.filename)
        # #self.ws = #self.wb.active
        # for i, n in enumerate(#self.wb.sheetnames):
        #     if n == 'Mentorship':
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

            self.driver.implicitly_wait(25)

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

    def Mentorship(self):
        '''

        '''
        try:

            # Mentorship
            self.driver.find_element(
                By.XPATH, '//div[text()="Mentorship"]').click()
            print("\n 2 - Selecting 'Mentorship'")
            #self.ws['C3'] = 'Mentorship'
            #self.ws['G3'] = 'Pass'
            #self.wb.save(self.filename)
            

        except Exception as e:
            print(e)
            print("\n 2 - Mentorship failed")
            #self.ws['C3'] = 'Mentorship'
            #self.ws['G3'] = 'Fail'
            #self.wb.save(self.filename)

    def Add_New(self):
        """

        """
        try:
            ''' Scroll to the page top '''
            self.driver.execute_script("window.scroll(0, 0);")
            

            button = self.driver.find_element(
                By.XPATH, "//button[@id='add_btn']").click()
            
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

    def Eligible_Employees(self):
        """
        """
        try:
            
            # Colleagues Mentored
            self.driver.find_element(
                By.XPATH, '//input[@name= "searchText" and @type="text"]').click()
            print("\n 4 - Selecting Mentors From The List . . .")
            
            

            self.driver.find_element(
                By.XPATH, '//input[@name= "searchText" and @type="text"]').send_keys("Alpana Upadhyay")
            
            

            self.driver.find_element(
                By.XPATH, '//div[text()= " GSI G 1181 Alpana Upadhyay "]').click()
            print("\n 5 - 'GSI G 1181 Alpana Upadhyay'")
            
            

            self.driver.find_element(
                By.XPATH, '//input[@name= "searchText" and @type="text"]').clear()
            
            

            self.driver.find_element(
                By.XPATH, '//input[@name= "searchText" and @type="text"]').send_keys("Neha Goel")
            
            

            self.driver.find_element(
                By.XPATH, '//div[text()= " GSI G 1160 Neha Goel "]').click()
            print("\n 6 - 'GSI G 1160 Neha Goel'")
            
            

            self.driver.find_element(
                By.XPATH, '//input[@name= "searchText" and @type="text"]').clear()
            
            

            self.driver.find_element(
                By.XPATH, '//input[@name= "searchText" and @type="text"]').send_keys("Ekansh Kothiyal")
            
            

            self.driver.find_element(
                By.XPATH, '//div[text()= " GSI G 1286 Ekansh Kothiyal "]').click()
            print("\n 7 - 'GSI G 1286 Ekansh Kothiyal'")
            

            print("\n 8 - Mentors got selected")
            #self.ws['C5'] = 'Mentorship'
            #self.ws['G5'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN MENTORSHIP >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 8 - Selecting Mentors from dropdown list gets fail")
            #self.ws['C5'] = 'Mentorship'
            #self.ws['G5'] = 'Fail'

            #self.wb.save(self.filename)

    def Mentorship_Duration(self):
        """

        """
        try:
            # Mentorship Duration
            self.driver.find_element(
                By.XPATH, '//input[@formcontrolname= "duration"]').send_keys("2")
            print("\n 9 - Duration in weeks - '2'")
            #self.ws['C6'] = 'Mentorship'
            #self.ws['G6'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Mentorship Duration >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 9 - Selecting Mentors from dropdown list gets fail")
            #self.ws['C6'] = 'Mentorship'
            #self.ws['G6'] = 'Fail'

            #self.wb.save(self.filename)

    def Enter_Description(self):
        """
        """
        try:

            # Enter Description
            self.driver.find_element(
                By.XPATH, '//textarea[@formcontrolname= "description"]').send_keys("Adding Mentorship")
            print("\n 10 - Entering Description")
            #self.ws['C7'] = 'Enter Description'
            #self.ws['G7'] = 'Pass'
            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Enter Description >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 10 - Entering Description gets fail")
            #self.ws['C7'] = 'Enter Description'
            #self.ws['G7'] = 'Fail'
            #self.wb.save(self.filename)

    def Goal_Type(self):
        """

        """
        try:
            # Goal Type-
            self.driver.find_element(
                By.XPATH,'//span[text()="Delivery Council (DC)"]').click()
            print("\n 11 - Selecting Goal Type- Engineering Council (EC)")
            #self.ws['C8'] = 'Engineering Council (EC)'
            #self.ws['G8'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Goal Type >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Unable to select Goal_Type")
            #self.ws['C8'] = 'Engineering Council (EC)'
            #self.ws['G8'] = 'Fail'

            #self.wb.save(self.filename)

    def Technology(self):
        """

        """
        try:
            # Technology-
            self.driver.find_element(
                By.XPATH, '//span[text()= "Select Technology"]').click()
            

            self.driver.find_element(
                By.XPATH, '//mat-option[@ng-reflect-value= "Automation Testing"]').click()
            print("\n 12 - Selecting Technology- Automation Testing")

            #self.ws['C9'] = 'Technology- Automation Testing'
            #self.ws['G9'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Goal Type >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 12 - Selecting Technology- Automation Testing")
            #self.ws['C9'] = 'Technology- Automation Testing'
            #self.ws['G9'] = 'Fail'

            #self.wb.save(self.filename)

    def Submit(self):
        """

        """
        try:
            # SUBMIT
            assert self.driver.find_element(
                By.CSS_SELECTOR, ".col-xs-3 > #add_btn").text == "SUBMIT"
            

            Submit_button = ActionChains(self.driver).move_to_element(self.driver.find_element(
                By.XPATH, '//span[text()="SUBMIT"]'))
            Submit_button.click().perform()
            

            self.driver.find_element(
                By.XPATH, '//span[text()="SUBMIT"]').click()

            
            print("\n 13 - All Details get submit successfully.")

            #self.ws['C10'] = 'Submit'
            #self.ws['G10'] = 'Pass'
            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN SUBMIT  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 13 - Unable to Click OK Button")
            #self.ws['C10'] = 'Submit'
            #self.ws['G10'] = 'Fail'

            #self.wb.save(self.filename)
            

    def OK_Button(self):
        """

        """
        try:
            self.driver.find_element(By.XPATH,'//span[text()="OK"]').click()

            print("\n 14 - Clicking OK Button")
            #self.ws['C11'] = 'OK Button'
            #self.ws['G11'] = 'Pass'
            
            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN OK Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 14 - Unable to Click OK Button")
            #self.ws['C11'] = 'OK Button'
            #self.ws['G11'] = 'Fail'

            #self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = MAuth()
    tb.setUp()
    tb.Mentorship()
    tb.Add_New()
    tb.Eligible_Employees()
    tb.Mentorship_Duration()
    tb.Goal_Type()
    tb.Technology()
    tb.Enter_Description()
    tb.Submit()
    tb.OK_Button()

    # unittest.main()
    # unittest.main(testRunner= x.HTMLTestRunner( '/home/am.bhatia/Desktop/ContriPoint/testsuits'))
