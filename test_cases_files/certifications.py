from Functionals import *
from datainputs import *


class CAuth(unittest.TestCase):
    
    def __init__(self): 

        """ interact with the underlying operating system."""
        import os
        print(os.path.join(os.getcwd()+ "\\xyz.xlsx"),">>>>>>")
        self.filename = os.path.join(os.getcwd()+ "\\xyz.xlsx")
        self.wb = load_workbook(filename=self.filename)
        self.index_sheet = 0
        if 'certifications' not in self.wb.sheetnames:
            self.wb.create_sheet('certifications')
            self.wb.save(os.path.join(os.getcwd()+ "\\xyz.xlsx"))
        self.wb = load_workbook(filename=self.filename)
        self.ws = self.wb.active
        for i, n in enumerate(self.wb.sheetnames):
            if n == 'certifications':
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
        self.wb.save(os.path.join(os.getcwd()+ "\\xyz.xlsx"))

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

            self.driver.implicitly_wait(10)
            self.driver.get(
                "https://dev-contripoint.geminisolutions.com/#/dashboard")

            

            print("\n Login Successfull \n")

            
            print("\n 1 - Gemini Id and Password successfully login")
            self.ws['C2'] = 'Login'
            self.ws['G2'] = 'login Success'

        except Exception as e:
            import traceback
            print(traceback.print_exc())
            print(e)
            print("\n 1 - Gemini Id and Password  login failed")
            self.ws['C2'] = 'Login'
            self.ws['G2'] = 'login failed'
            self.wb.save(self.filename)



     # As per unittest module, individual test should start with test_
    def Certifications(self):
        """

        """
        try:
            ''' Scroll to the page top '''
            self.driver.execute_script("window.scroll(0, 0);")
            

            #Certifications
            a = self.driver.find_element(By.XPATH,'//div[text()="Certificate"]')
            a.click()
            print("\n 2 - Selecting 'Certifications' successfully")
            self.ws['C3'] = 'Certifications'
            self.ws['G3'] = 'Pass'

            self.wb.save(self.filename)

            
        
        except Exception as e:
            print("\n\nERROR IN Certifications >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 2 - Selecting 'Certifications' get fail")
            self.ws['C3'] = 'Certifications'
            self.ws['G3'] = 'Fail'
            self.wb.save(self.filename)

    def Add_New_Contribution(self):
        """

        """
        try:
            #Adding New Contribution
            self.driver.execute_script("window.scrollTo(0,100)")

            self.driver.find_element(By.XPATH,'//*[@id="add_btn"]').click()
            
            print("\n 3 - Add New Contribution button gets selected")
            self.ws['C4'] = 'Add New Contribution'
            self.ws['G4'] = 'Pass'

            self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN Adding New Contribution >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 3 - Add New Contribution button gets fail")
            self.ws['C4'] = 'Add New Contribution'
            self.ws['G4'] = 'Fail'

            self.wb.save(self.filename)

    def Name_Of_Certification(self):
        """

        """
        try:
            #NAME OF CERTIFICATION-
            self.driver.find_element(By.XPATH,'//*[@id="mat-input-0"]') .send_keys('Python')           
            print("\n 4 - Name Of Certification - 'Python'")
            self.ws['C5'] = 'Name Of Certification'
            self.ws['G5'] = 'Pass'

            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Name Of Certificate >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 4 - Unable to select Name Of Certification from dropdown list ")
            self.ws['C5'] = 'Name Of Certification'
            self.ws['G5'] = 'Fail'

            self.wb.save(self.filename)

            
    def Date_Of_Completion(self):
        """

        """
        try:
            #Selecting Date of completion-
            datefield = self.driver.find_element(By.XPATH,'//*[@id="mat-dialog-0"]/app-certificate-add-modal/div/mat-dialog-content/form/div/div[2]/div/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button').click()
            datefield = self.driver.find_element(By.XPATH,"//div[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']").click()
            print("\n 5 - Date of completion done")
            self.ws['C6'] = 'Date of completion'
            self.ws['G6'] = 'Pass'

            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Date of Completion >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 5 - Date of completion gets fail")
            self.ws['C6'] = 'Date of completion'
            self.ws['G6'] = 'Fail'

            self.wb.save(self.filename)

    def Uploading_Attachment(self):
        """

        """
        try:
            #Uploading Attatchment-
            self.driver.find_element(By.XPATH,'//*[@id="attachment_btn"]').click()
            time.sleep(8)
            pyautogui.write(Attachment)
            pyautogui.press('enter') 
            print("\n 6 - Attachment Upload successfully")
            self.ws['C7'] = 'Upload attatchment'
            self.ws['G7'] = 'Pass'

            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Uploading Attatchment >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 6 - Unable to upload the attatchment")
            self.ws['C7'] = 'Upload attatchment'
            self.ws['G7'] = 'Fail'

            self.wb.save(self.filename)

    def Technology(self):
        """

        """
        try:
            #Technology-
            self.driver.find_element(By.XPATH,'//*[text()="Select Technology"]').click()
            print("\n 7 - Selecting Technology. . .")
            self.ws['C8'] = 'Date of completion'
            self.ws['G8'] = 'Pass'

            self.wb.save(self.filename)
            

            self.driver.find_element(By.XPATH,'//*[text()="Android"]').click()
            print("\n 8 - 'ANDROID' got selected from Technology")
            
            

        except Exception as e:
            print("\n\nERROR IN TECHNOLOGY >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 7 - Unable to select Technology from dropdown list")
            self.ws['C8'] = 'Technology'
            self.ws['G8'] = 'Fail'

            self.wb.save(self.filename)


    def Goal_Type(self):
        """

        """
        try:
            #Goal Type-
            self.driver.find_element(By.XPATH,'//*[text()="Engineering Council (EC)"]').click()
            print("\n 8 - Selecting Goal Type- Engineering Council (EC)")
            self.ws['C9'] = 'Engineering Council (EC)'
            self.ws['G9'] = 'Pass'

            self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN Goal Type >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 8 - Unable to select Goal_Type")
            self.ws['C9'] = 'Engineering Council (EC)'
            self.ws['G9'] = 'Fail'

            self.wb.save(self.filename)


    def Submit(self):
        """

        """
        try:
            #SUBMIT
            element = self.driver.find_element(By.XPATH, '//*[contains(text(),"SUBMIT")]')
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()

            self.driver.find_element(
                By.CSS_SELECTOR, ".col-xs-3 > #add_btn").click()
            print("\n 9 - All Details get SUBMIT successfully.")
            self.ws['C10'] = 'Submit'
            self.ws['G10'] = 'Pass'
            self.wb.save(self.filename)
            

            #OK Button
            assert self.driver.find_element(
                By.CSS_SELECTOR, "#ok_btn > .mat-button-wrapper").text == "OK"
            

            element = self.driver.find_element(By.ID, "ok_btn")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            

            self.driver.find_element(By.ID, "ok_btn").click()
            print("\n 10 - Clicking OK Button")
            

        except Exception as e:
            print("\n\nERROR IN SUBMIT  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 9 - Unable to Click Submit Button")
            self.ws['C10'] = 'Submit'
            self.ws['G10'] = 'Fail'

            self.wb.save(self.filename)
            



    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = CAuth()
    tb.setUp()
    tb.Certifications()
    tb.Add_New_Contribution()
    tb.Name_Of_Certification()
    tb.Date_Of_Completion()
    tb.Uploading_Attachment()
    tb.Goal_Type()
    tb.Technology()
    tb.Submit()
    #unittest.main()
    #unittest.main(testRunner= x.HTMLTestRunner( 'C:Users/Aman Bhatia/OneDrive - Gemini Solutions/Desktop/Contripoint_Project/testsuits'))