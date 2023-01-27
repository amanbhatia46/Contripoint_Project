from Functionals import *
from datainputs import *


class RBugEvent(unittest.TestCase):

    def __init__(self):
        """ interact with the underlying operating system."""
        import os
        print(os.path.join(os.getcwd() + "\\result.xlsx"), ">>>>>>")
        self.filename = os.path.join(os.getcwd() + "\\result.xlsx")
        self.wb = load_workbook(filename=self.filename)
        self.index_sheet = 0
        if 'Report Bug' not in self.wb.sheetnames:
            self.wb.create_sheet('Report Bug')
            self.wb.save(os.path.join(os.getcwd() + "\\result.xlsx"))
        self.wb = load_workbook(filename=self.filename)
        self.ws = self.wb.active
        for i, n in enumerate(self.wb.sheetnames):
            if n == 'Report Bug':
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
        self.wb.save(os.path.join(os.getcwd() + "\\result.xlsx"))

        # datetime object containing current date and time
        futuredate = str(datetime.now())
        print(futuredate)
        self.ws['H2'] = futuredate

    def setUp(self):
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option(
                'debuggerAddress', 'localhost:9222')

            self.driver = webdriver.Chrome(
                options=chrome_options, executable_path="C:\\Users\\Aman Bhatia\\OneDrive - Gemini Solutions\\Desktop\\Contripoint_Project\\ChromeDriver\\chromedriver.exe")
            print("Browser Connected")

            self.driver.implicitly_wait(12)

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

    def Report_Bug(self):
        """
            Report Bug
        """
        try:
            ''' Scroll to the page down '''
            self.driver.execute_script("window.scroll(250, 0);")
            

            # Report a Bug/Feedback
            Bug = self.driver.find_element(
                By.XPATH, '//button[text()="Report a Bug/Feedback"]')
            
            Bug.click()

            print("\n 7 - Selecting 'Report a Bug/Feedback' . .")

            self.ws['C3'] = 'Report a Bug/Feedback'
            self.ws['G3'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\n ERROR IN Report a Bug/Feedback >>>>>>>>>>>>>>>\n\n")
            print("\n 7 - Selecting Report a Bug/Feedback gets fail")

            self.ws['C3'] = 'Report a Bug/Feedback'
            self.ws['G3'] = 'Fail'
            self.wb.save(self.filename)

    def Add_New(self):
        """

        """
        try:
            ''' Scroll to the page top '''
            self.driver.execute_script("window.scroll(0, 0);")
            

            self.driver.find_element(
                By.XPATH, '//button[text()="ADD NEW"]').click()
            

            print("\n 8 - Clicking on  ADD NEW button")
            self.ws['C4'] = 'Add New'
            self.ws['G4'] = 'Pass'

            self.wb.save(self.filename)

        except Exception as e:
            print("\n\n ERROR IN ADD NEW >>>>>>>>>>>>>>>\n\n")
            print("\n 8 - Clicking on Add New Button gets fail")
            self.ws['C4'] = 'Add New'
            self.ws['G4'] = 'Fail'

            self.wb.save(self.filename)

    def Issue_Subject(self):
        """

        """
        try:
            self.driver.find_element(
                By.XPATH, '//input[@formcontrolname="bugTitle"]').send_keys("Design work")
            
            print("\n 9 - Issue Subject - 'Design work' ")
            self.ws['C5'] = 'Issue Subject'
            self.ws['G5'] = 'Pass'

            self.wb.save(self.filename)

        except Exception as e:
            print("\n\n ERROR IN ISSUE SUBJECT >>>>>>>>>>>>>>>\n\n")
            print("\n 9 - Selecting Issue Subject gets fail")
            self.ws['C5'] = 'Issue Subject'
            self.ws['G5'] = 'Fail'

            self.wb.save(self.filename)

    def Issue_Category(self):
        """

        """
        try:
            Dropdown = self.driver.find_element(
                By.XPATH, '//span[text()="Select Issue"]')
            
            Dropdown.click()
            

            Design = self.driver.find_element(
                By.XPATH, '//span[text()=" Design "]')
            
            Design.click()
            print("\n 10 - Selecting 'Design'")
            

            self.ws['C6'] = 'Issue Category - Design'
            self.ws['G6'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\n ERROR IN Selecting Issue Category >>>>>>>>>>>>>>>\n\n")
            print("\n 10 - Selecting 'Issue Category' gets fail")
            self.ws['C6'] = 'Issue Category - Design'
            self.ws['G6'] = 'Fail'

            self.wb.save(self.filename)

    def Select_Website_Feature(self):
        """

        """
        try:
            Dropdown = self.driver.find_element(
                By.XPATH, '//span[text()="Select Website Feature"]')
            
            Dropdown.click()

            self.driver.find_element(
                By.XPATH, '//span[text()=" Certificate "]').click()
            

            print("\n 11 - Selecting 'Certificate' as Website Feature")
            

            self.ws['C7'] = 'Website Feature - Certificate'
            self.ws['G7'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\n ERROR IN Selecting Website Feature >>>>>>>>>>>>>>>\n\n")
            print("\n 11 - Selecting 'Website Feature' gets fail")
            self.ws['C7'] = 'Website Feature - Certificate'
            self.ws['G7'] = 'Fail'

            self.wb.save(self.filename)

    def Description(self):
        """
            Enter Event's Description
        """
        try:
            self.driver.find_element(By.XPATH, '//textarea[@formcontrolname="description"]').send_keys(
                "Reporting a bug to the team.")

            print("\n 12 - Entering Description Done")
            

            self.ws['C8'] = 'Description'
            self.ws['G8'] = 'Pass'

            self.wb.save(self.filename)

        except Exception as e:
            print("\n\n ERROR IN DESCRIPTION >>>>>>>>>>>>>>>\n\n")
            print("\n 12 - Entering Description gets fail")

            self.ws['C8'] = 'Description'
            self.ws['G8'] = 'Fail'

            self.wb.save(self.filename)

    def attachment_button(self):
        """
            Add Listing Image
        """
        try:

            Add_Attachment = self.driver.find_element(
                By.ID, "attachment_btn")
            Add_Attachment.click()
            print("\n 13 - Clicking on Attachment Button")
            time.sleep(8)

            pyautogui.write(Attachment)
            
            pyautogui.press('enter')
            print("\n 14 - Attachment Upload successfully")

            self.ws['C9'] = 'Uploading Attachment gets Pass'
            self.ws['G9'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\n ERROR IN ATTACHMENT >>>>>>>>>>>>>>>\n\n")
            print("\n 14 - Attachment Uploading gets fail")
            self.ws['C9'] = 'Uploading Attachment gets Fail'
            self.ws['G9'] = 'Fail'

            self.wb.save(self.filename)

    def Submit(self):
        '''
        '''
        try:
            submit = self.driver.find_element(
                By.XPATH, '//button[@id="upload_btn"]')
            
            submit.click()

            print("\n 15 - All Bug Details get SUBMIT successfully.")

            self.ws['C10'] = 'Submit'
            self.ws['G10'] = 'Pass'
            self.wb.save(self.filename)

            element = self.driver.find_element_by_tag_name('h2')

            if element.text != u'Design':
                print("\n Verify Passed : element text is Design") % element.text
            else:
                print(
                    "\n Verify Failed : element text is not Design") % element.text
            

        except Exception as e:
            print("\n\n ERROR IN SUBMIT >>>>>>>>>>>>>>>\n\n")
            print("\n 15 - Unable to submit all details")

            self.ws['C10'] = 'Submit'
            self.ws['G10'] = 'Fail'
            self.wb.save(self.filename)

    def OK_Button(self):
        '''
            OK Button
        '''
        try:
            window_handles = self.driver.window_handles
            
            self.driver.switch_to.window(window_handles[0])

            ok = self.driver.find_element(
                By.XPATH,'//button//span[text()="OK"]')
            
            ok.click()
            

            print("\n 16 - Clicking OK Button")

            self.ws['C11'] = 'OK Button'
            self.ws['G11'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n\n ERROR IN OKButton >>>>>>>>>>>>>>>\n\n")
            print("\n 16 - Unable to Click OK Button")
            import traceback
            print(traceback)
            print(e)
            self.ws['C11'] = 'OK Button'
            self.ws['G11'] = 'Fail'
            self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = RBugEvent()
    tb.setUp()
    tb.Report_Bug()
    tb.Add_New()
    tb.Issue_Subject()
    tb.Issue_Category()
    tb.Select_Website_Feature()
    tb.Description()
    tb.attachment_button()
    tb.Submit()
    tb.OK_Button()
