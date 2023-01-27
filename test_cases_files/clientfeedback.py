from Functionals import *
from datainputs import *


class CFAuth(unittest.TestCase):
    

    def __init__(self):
        
        """ interact with the underlying operating system."""
        # import os
        # print(os.path.join(os.getcwd()+ "\\result.xlsx"),">>>>>>")
        # self.filename = os.path.join(os.getcwd()+ "\\result.xlsx")
        # #self.wb = load_workbook(filename=self.filename)
        # self.index_sheet = 0
        # if 'ClientFeedback' not in #self.wb.sheetnames:
        #     #self.wb.create_sheet('ClientFeedback')
        #     #self.wb.save(os.path.join(os.getcwd()+ "\\result.xlsx"))
        # #self.wb = load_workbook(filename=self.filename)
        # #self.ws = #self.wb.active
        # for i, n in enumerate(#self.wb.sheetnames):
        #     if n == 'ClientFeedback':
        #         self.index_sheet = i
        #         break
        # #self.wb.active = self.index_sheet
        # #self.ws = #self.wb.active
        # #self.wb.active = 1
        # #self.ws['A1'] = 'Email'
        # #self.ws['B1'] = 'Password'
        # #self.ws['C1'] = 'Test Case Module'
        # #self.ws['G1'] = 'Result'
        # #self.ws['H1'] = 'Date and #time'
        # #self.wb.save(os.path.join(os.getcwd()+ "\\result.xlsx"))


        # # date#time object containing current date and #time
        # futuredate = str(date#time.now())
        # print(futuredate)
        # #self.ws['H2'] = futuredate
        pass

    def setUp(self):
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option('debuggerAddress', 'localhost:9222')
            
            self.driver = webdriver.Chrome(options=chrome_options,executable_path="C:\\Users\\Aman Bhatia\\OneDrive - Gemini Solutions\\Desktop\\Contripoint_Project\\ChromeDriver\\chromedriver.exe")
            print("Browser Connected")

            self.driver.implicitly_wait(12)
            self.driver.get(
                "https://dev-contripoint.geminisolutions.com/#/dashboard")

            #

            print("\n Login Successfull \n")

            #
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

                   
    def Clientfeedback(self):
        '''

        '''
        try:
            ''' Scroll to the page down '''
            self.driver.execute_script("window.scroll(300, 0);")

            #ClientFeedback Button
            clientfeedback = self.driver.find_element(
                By.XPATH, '//div[text()="Client Feedback"]')
            clientfeedback.click()
            print("\n 2 - Selecting 'ClientFeedback'")
            #self.ws['C3'] = 'Selecting ClientFeedback'
            #self.ws['G3'] = 'Pass'
            #self.wb.save(self.filename)
            #

        except Exception as e:
            print("\n\nERROR IN CLIENT FEEDBACK >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 2 - Selecting 'ClientFeedback' gets failed")
            #self.ws['C3'] = 'Selecting ClientFeedback'
            #self.ws['G3'] = 'Fail'
            #self.wb.save(self.filename)


    def AddNew(self):
        '''

        '''
        try:
            ''' Scroll to the page top '''
            self.driver.execute_script("window.scroll(0, 0);")
            #
            
            #ADD NEW
            element = self.driver.find_element(
                By.XPATH, '//button[@id="add_btn"]')
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            #
            
            print("\n 3 - Selecting 'Add New' button gets selected")
            #self.ws['C4'] = 'Add New'
            #self.ws['G4'] = 'Pass'
            #self.wb.save(self.filename)
            

        except Exception as e:
            print("\n\nERROR IN ADD NEW  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 3 - Selecting 'Add New' button gets fail")
            #self.ws['C4'] = 'Add New'
            #self.ws['G4'] = 'Fail'
            #self.wb.save(self.filename)


    def ProjectName(self):
        '''

        '''
        try:
            time.sleep(5)
            #ProjectName
            self.driver.find_element(
                By.XPATH, '//input[@formcontrolname="projectName"]').send_keys('Skedular')
            
            print("\n 4 - Project Name Done")
            #self.ws['C5'] = 'Project Name'
            #self.ws['G5'] = 'Pass'
            #self.wb.save(self.filename)
            #

        except Exception as e:
            print("\n\nERROR IN PROJECT NAME >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 4 - Unable to fill Project name")
            #self.ws['C5'] = 'Project Name'
            #self.ws['G5'] = 'Fail'
            #self.wb.save(self.filename)


    def ClientName(self):
        '''

        '''
        try:
            #ClientName
            self.driver.find_element(
                By.XPATH,'//input[@formcontrolname="clientName"]').send_keys("auto-skedular")
            print("\n 5 - Client Name Done")
            #self.ws['C6'] = 'Client Name'
            #self.ws['G6'] = 'Pass'
            #self.wb.save(self.filename)
            #

        except Exception as e:
            print("\n\nERROR IN CLIENT NAME >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 5 - Unable to fill Client name")
            #self.ws['C6'] = 'Client Name'
            #self.ws['G6'] = 'Fail'
            #self.wb.save(self.filename)

    def Enter_ClientFeedback(self):
        '''

        '''
        try:
            #Enter Client Feedback's description
            self.driver.find_element(
                By.XPATH,'//textarea[@formcontrolname="description"]').send_keys("US client")
            print("\n 6 - Client Feedback Done")
            #self.ws['C7'] = 'Enter Client Feedback'
            #self.ws['G7'] = 'Pass'
            #self.wb.save(self.filename)
            #

        except Exception as e:
            print("\n\nERROR IN CLIENT FEEDBACK >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 6 - Unable to fill Client Feedback")
            #self.ws['C7'] = 'Enter Client Feedback'
            #self.ws['G7'] = 'Fail'
            #self.wb.save(self.filename)


    def Upload_attatchment(self):
        '''

        '''
        try:
            #Upload Attachment
            assert self.driver.find_element(
                By.ID, "attachment_btn").text == "Upload attachment"

            #self.wb.save(self.filename)
            #

            self.driver.find_element(By.ID, "attachment_btn").click()
            print("\n 7 - Selecting Attachment from Drive . . .")
            time.sleep(5)

            pyautogui.write(Attachment)
            pyautogui.press('enter') 
            print("\n 8 - Attachment Upload successfully")
            #self.ws['C8'] = 'Upload attatchment'
            #self.ws['G8'] = 'Pass'

            #self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN UPLOAD ATTACHMENT >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 8 - Unable to upload attatchment")
            #self.ws['C8'] = 'Upload attatchment'
            #self.ws['G8'] = 'Fail'
            #self.wb.save(self.filename)

    def Goal_Type(self):
        """

        """
        try:
            #Goal Type-
            self.driver.find_element(By.XPATH,'//span[text()="Delivery Council (DC)"]').click()
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
        '''

        '''
        try:
            #SUBMIT
            assert self.driver.find_element(
                By.CSS_SELECTOR, ".col-xs-3 > #add_btn > .mat-button-wrapper").text == "SUBMIT"

            self.driver.find_element(
                By.CSS_SELECTOR, ".col-xs-3 > #add_btn").click()

            print("\n 10 - All Details get SUBMIT successfully.")
            #self.ws['C10'] = 'Submit'
            #self.ws['G10'] = 'Pass'
            #self.wb.save(self.filename)
            #

        except Exception as e:
            print("\n\nERROR IN SUBMIT >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 10 - Unable to submit all details")
            #self.ws['C10'] = 'Submit'
            #self.ws['G10'] = 'Fail'
            #self.wb.save(self.filename)



    def OK_Button(self):
        '''

        '''
        try:
            #OK Button
            assert self.driver.find_element(
                By.CSS_SELECTOR, "#ok_btn > .mat-button-wrapper").text == "OK"
            #

            element = self.driver.find_element(By.XPATH,'//button[@type="submit" and @id="ok_btn"]')
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            #

            self.driver.find_element(By.XPATH, '//button[@type="submit" and @id="ok_btn"]').click()
            print("\n 11 - Clicking OK Button")
            #self.ws['C11'] = 'OK Button'
            #self.ws['G11'] = 'Fail'
            #self.wb.save(self.filename)
            #

        except Exception as e:
            print("\n\nERROR IN OKButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Unable to Click OK Button")
            #self.ws['C11'] = 'OK Button'
            #self.ws['G11'] = 'Fail'
            #self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = CFAuth()
    tb.setUp()
    tb.Clientfeedback()
    tb.AddNew()
    tb.ProjectName()
    tb.ClientName()
    tb.Enter_ClientFeedback()
    tb.Upload_attatchment()
    tb.Goal_Type()
    tb.Submit()
    tb.OK_Button()
    # unittest.main()
    # unittest.main(testRunner= x.HTMLTestRunner( '/home/am.bhatia/Desktop/ContriPoint/testsuits'))

