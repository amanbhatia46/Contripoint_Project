from Functionals import *
from datainputs import *


class TBAuth(unittest.TestCase):
    

    def __init__(self):
        
            """ interact with the underlying operating system."""
            import os
            print(os.path.join(os.getcwd()+ "\\result.xlsx"),">>>>>>")
            self.filename = os.path.join(os.getcwd()+ "\\result.xlsx")
            self.wb = load_workbook(filename=self.filename)
            self.index_sheet = 0
            if 'TeamBuildingActivity' not in self.wb.sheetnames:
                self.wb.create_sheet('TeamBuildingActivity')
                self.wb.save(os.path.join(os.getcwd()+ "\\result.xlsx"))
            self.wb = load_workbook(filename=self.filename)
            self.ws = self.wb.active
            for i, n in enumerate(self.wb.sheetnames):
                if n == 'TeamBuildingActivity':
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
       
    def teambuildingactivity(self):
        '''

        '''
        try:
            #TeamBuildingActivity  
            TeamBuildingActivity = self.driver.find_element(
                By.XPATH, '//div[text()="Team Building Activity"]')
            TeamBuildingActivity.click()
            print("\n 2 - Selecting 'Team Building Activity'")
            self.ws['C3'] = 'Team Building Activity'
            self.ws['G3'] = 'Pass'
            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN TEAM BUILDING ACTIVITY >>>>>>>>>>>>>>>\n\n")
            print (e)
            print("\n 2 - Selecting 'Team Building Activity' got Failed")
            self.ws['C3'] = 'Team Building Activity'
            self.ws['G3'] = 'Fail'
            self.wb.save(self.filename)

        
    def AddNew(self):
        '''

        '''
        try:
            # ADD NEW
            ''' Scroll to the page top '''
            self.driver.execute_script("window.scroll(0, 0);")
            

            button = self.driver.find_element(
                By.XPATH, "//button[@id='add_btn']").click()
            print("\n 3 - 'Add New' button gets selected")
            

            self.ws['C4'] = 'Add New button'
            self.ws['G4'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN AddNew >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 3 - 'Add New' button got fail")
            self.ws['C4'] = 'Add New button'
            self.ws['G4'] = 'Fail'
            self.wb.save(self.filename)

    def NameofActivityConducted(self):
        '''

        '''
        try:
            # Name of Activity Conducted
            self.driver.find_element(By.XPATH,'//input[@ng-reflect-name="summary"]').send_keys("Project")
            print("\n 4 - Name of Activity Conducted")

            self.ws['C5'] = 'Name of Activity Conducted'
            self.ws['G5'] = 'Pass'
            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN NameOfActivityConducted >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 3 - Name of Activity Fail")
            self.ws['C5'] = 'Name of Activity Conducted'
            self.ws['G5'] = 'Fail'
            self.wb.save(self.filename)


    def NumberOfParticipants(self):
        '''

        '''
        try:
            #No. Of Participants in the Activity
            self.driver.find_element(By.XPATH,'//input[@ng-reflect-name="headCount"]').send_keys("2")
            print("\n 5 - No. Of Participants in the Activity - '2'")

            self.ws['C6'] = 'No. Of Participants in the Activity'
            self.ws['G6'] = 'Pass'
            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN NumberOfParticipants >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 5 - No. Of Participants in the Activity gets fail")
            self.ws['C6'] = 'No. Of Participants in the Activity'
            self.ws['G6'] = 'Fail'
            self.wb.save(self.filename)
            

    def EnterDescription(self):
        '''

        '''
        try:
            #Enter Description 
            self.driver.find_element(By.XPATH,'//textarea[@formcontrolname="description"]').send_keys("If you want to lift yourself up, lift up with the team")
            print("\n 6 - Entering Description Done")

            self.ws['C7'] = 'Description'
            self.ws['G7'] = 'Pass'
            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN EnterDescription >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 5 - Entering Description gets fail")
            self.ws['C7'] = 'Description'
            self.ws['G7'] = 'Fail'
            self.wb.save(self.filename)

    def Goal_Type(self):
        """

        """
        try:
            # Goal Type-
            self.driver.find_element(
                By.XPATH, '//span[text()="Engineering Council (EC) "]').click()
            

            print("\n 6 - Selecting Goal Type- Engineering Council (EC)")
            self.ws['C8'] = 'Engineering Council (EC)'
            self.ws['G8'] = 'Pass'

            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Goal Type >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 6 - Unable to select Goal_Type")
            self.ws['C8'] = 'Engineering Council (EC)'
            self.ws['G8'] = 'Fail'

            self.wb.save(self.filename)
        
    def DateoftheActivity(self):
        '''

        '''
        try:
            #Date of the Activity
            self.driver.find_element(
                By.CSS_SELECTOR, ".mat-datepicker-toggle-default-icon").click()
            print("\n 7 - Selecting 'Date of the Activity' . . . ")

            self.ws['C9'] = 'Date of the Activity'
            self.ws['G9'] = 'Pass'
            self.wb.save(self.filename)
            

            #Date from the Calander
            self.driver.find_element(
                By.CSS_SELECTOR, ".mat-calendar-body-today").click()
            print("\n 8 - Selecting the Date of the Activity from the calander")
            
        
        except Exception as e:
            print("\n\nERROR IN DateoftheActivity >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 7 - Fail to select the Date of the Activity from the calander")
            self.ws['C9'] = 'Date of the Activity'
            self.ws['G9'] = 'Fail'
            self.wb.save(self.filename)

    def SubmitButton(self):
        '''

        '''
        try:
            #SUBMIT Button
            self.driver.find_element(
                By.XPATH,'//button[@type="submit"]').click()
            print("\n 9 - All Details get SUBMIT successfully.")

            self.ws['C10'] = 'SUBMIT'
            self.ws['G10'] = 'Pass'
            self.wb.save(self.filename)
            
        
        except Exception as e:
            print("\n\nERROR IN SubmitButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 9 - All Details get fail while SUBMIT.")
            self.ws['C10'] = 'SUBMIT'
            self.ws['G10'] = 'Fail'
            self.wb.save(self.filename)

    def OKButton(self):
        '''

        '''
        try:
            #OK Button
            assert self.driver.find_element(
                By.CSS_SELECTOR, "#ok_btn > .mat-button-wrapper").text == "OK"
            

            element = self.driver.find_element(By.ID, "ok_btn")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            

            self.driver.find_element(By.ID, "ok_btn").click()
            print("\n 10 - Clicking OK Button")

            self.ws['C11'] = 'OK BUTTON'
            self.ws['G11'] = 'Pass'
            self.wb.save(self.filename)
            

            self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN OKButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 9 - Unable to click OK Button")
            self.ws['C10'] = 'OK BUTTON'
            self.ws['G10'] = 'Fail'
            self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()
    

if __name__ == '__main__':
    tb= TBAuth()
    tb.setUp()
    tb.teambuildingactivity()
    tb.AddNew()
    tb.NameofActivityConducted()
    tb.NumberOfParticipants()
    tb.EnterDescription()
    tb.Goal_Type()
    tb.DateoftheActivity()
    tb.SubmitButton()
    tb.OKButton()

    # unittest.main()
    # unittest.main(testRunner= x.HTMLTestRunner( '/home/am.bhatia/Desktop/ContriPoint/testsuits'))

