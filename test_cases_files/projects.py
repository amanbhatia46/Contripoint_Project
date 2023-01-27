from Functionals import *
from datainputs import *


class PAuth(unittest.TestCase):

    def __init__(self):
        
        """ interact with the underlying operating system."""
        # import os
        # print(os.path.join(os.getcwd()+ "\\result.xlsx"),">>>>>>")
        # self.filename = os.path.join(os.getcwd()+ "\\result.xlsx")
        # #self.wb = load_workbook(filename=self.filename)
        # self.index_sheet = 0
        # if 'Projects' not in #self.wb.sheetnames:
        #     #self.wb.create_sheet('Projects')
        #     #self.wb.save(os.path.join(os.getcwd()+ "\\result.xlsx"))
        # #self.wb = load_workbook(filename=self.filename)
        # #self.ws = #self.wb.active
        # for i, n in enumerate(#self.wb.sheetnames):
        #     if n == 'Projects':
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

    def Projects(self):
        """

        """
        try:
            # Projects -
            self.driver.find_element(
                By.XPATH, '//div[text()="Project"]').click()

            print("\n 2 - Clicking on module - 'Projects'")
            #self.ws['C3'] = 'Project'
            #self.ws['G3'] = 'Pass'
            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN PROJECTS >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 2 - Selecting Proejct gets fail")
            #self.ws['C3'] = 'Project'
            #self.ws['G3'] = 'Fail'

            #self.wb.save(self.filename)

            print("\n 3 - sample test case of entering 'PROJECTS' successfully open")

    def Add_New(self):
        """

        """
        try:
             # ADD NEW
            ''' Scroll to the page top '''
            self.driver.execute_script("window.scroll(0, 0);")
            

            button = self.driver.find_element(
                By.XPATH, "//button[@id='add_btn']").click()
            print("\n 4 - 'Add New' button gets selected")

            #self.ws['C4'] = 'Add New Button'
            #self.ws['G4'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Adding New Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 4 - Add New button gets fail")
            #self.ws['C4'] = 'Add New Button'
            #self.ws['G4'] = 'Fail'

            #self.wb.save(self.filename)

    def Project_Type(self):
        """

        """
        try:
            # Select Project Type *
            self.driver.find_element(By.XPATH,'//mat-radio-button[@ng-reflect-value="Inhouse"]').click()
            print("\n 5 - Project Type gets selected as 'Inhouse'")

            #self.ws['C5'] = 'Project type'
            #self.ws['G5'] = 'Pass'
            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Project Type >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 6 - Add New Project Type gets fail")
            #self.ws['C5'] = 'Project Type'
            #self.ws['G5'] = 'Fail'

            #self.wb.save(self.filename)

    def Project_Title(self):
        """
        """
        try:
            # Project Title -
            self.driver.find_element(
                By.XPATH,'//input[@formcontrolname="projectName"]').send_keys("contripoint")

            print("\n 7 - Project Title savesuccessfully")

            #self.ws['C6'] = 'Project Title'
            #self.ws['G6'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Project Title >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 7 - Project Title save unsuccessfully")
            #self.ws['C6'] = 'Project Title'
            #self.ws['G6'] = 'Fail'

            #self.wb.save(self.filename)

    def Start_Date(self):
        """

        """
        try:
            # calander

            self.driver.find_element(
                By.XPATH,'//input[@formcontrolname="date"]').send_keys("7/1/2022")

            
            print("\n 11 - Date Of Completion")
            #self.ws['C7'] = 'Date Of Completion'
            #self.ws['G7'] = 'Pass'

            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN Date Of Completion >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Selecting Date Of Completion gets fail")
            #self.ws['C7'] = 'Date Of Completion'
            #self.ws['G7'] = 'Fail'

            #self.wb.save(self.filename)

    def Project_Status(self):
        """
        """
        try:
            self.driver.find_element(
                By.XPATH,'//mat-radio-button[@value= "ongoing"]').click()

            print("\n 13 - Project Status Done")
            #self.ws['C8'] = 'Project Status'
            #self.ws['G8'] = 'Pass'
            

            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN Project Status >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 13 - Entering Project Status gets fail")
            #self.ws['C8'] = 'Project Status'
            #self.ws['G8'] = 'Fail'
            #self.wb.save(self.filename)

    def Description(self):
        """

        """
        try:
            self.driver.find_element(
                By.XPATH, '//textarea[@formcontrolname="description"]').send_keys("internal project")
            
            print("\n 14 - Entering Description Done")
            #self.ws['C8'] = 'Description'
            #self.ws['G8'] = 'Pass'
            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN Project Status >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 14 - Entering Description gets fail")
            #self.ws['C8'] = 'Description'
            #self.ws['G8'] = 'Fail'
            #self.wb.save(self.filename)

    def Goal_Type(self):
        """

        """
        try:
            # Goal Type-
            self.driver.find_element(
                By.XPATH,'//span[text()="Delivery Council (DC)"]').click()
            

            print("\n 15 - Selecting Goal Type- Engineering Council (EC)")
            #self.ws['C9'] = 'Engineering Council (EC)'
            #self.ws['G9'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Goal Type >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 15 - Unable to select Goal_Type")
            #self.ws['C9'] = 'Engineering Council (EC)'
            #self.ws['G9'] = 'Fail'

            #self.wb.save(self.filename)

    def Submit(self):
        """

        """
        try:
            self.driver.find_element(
                By.XPATH, '//button[@type="submit"]').click()
            
            print("\n 16 - All Details get submit successfully.")
            #self.ws['C10'] = 'Submit'
            #self.ws['G10'] = 'Pass'
            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN SUBMIT  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 116 - Unable to Click Submit Button")
            #self.ws['C10'] = 'Submit'
            #self.ws['G10'] = 'Fail'

            #self.wb.save(self.filename)
            

    def OK_Button(self):
        """

        """
        try:
            self.driver.find_element(By.ID, "ok_btn").click()
            print("\n 17 - Clicking OK Button")
            #self.ws['C11'] = 'OK Button'
            #self.ws['G11'] = 'Pass'

            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN OK Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 17 - Unable to Click OK Button")
            #self.ws['C11'] = 'OK Button'
            #self.ws['G11'] = 'Fail'

            #self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = PAuth()
    tb.setUp()
    tb.Projects()
    tb.Add_New()
    tb.Project_Type()
    tb.Project_Title()
    tb.Start_Date()
    tb.Project_Status()
    tb.Description()
    tb.Goal_Type()
    tb.Submit()
    tb.OK_Button()
    # unittest.main()
#    unittest.main(testRunner= x.HTMLTestRunner( '/home/am.bhatia/Desktop/ContriPoint/testsuits'))
