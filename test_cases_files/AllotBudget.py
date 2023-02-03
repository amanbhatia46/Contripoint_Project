from Functionals import *
from datainputs import *


class AllotBudget(unittest.TestCase):

    def __init__(self):
        """ interact with the underlying operating system."""
        # import os
        # print(os.path.join(os.getcwd() + "\\result.xlsx"), ">>>>>>")
        # self.filename = os.path.join(os.getcwd() + "\\result.xlsx")
        # #self.wb = load_workbook(filename=self.filename)
        # self.index_sheet = 0
        # if 'Allot Budget' not in #self.wb.sheetnames:
        #     #self.wb.create_sheet('Allot Budget')
        #     #self.wb.save(os.path.join(os.getcwd() + "\\result.xlsx"))
        # #self.wb = load_workbook(filename=self.filename)
        # #self.ws = #self.wb.active
        # for i, n in enumerate(#self.wb.sheetnames):
        #     if n == 'Allot Budget':
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
        # future date = str(datetime.now())
        # print(future date)
        # #self.ws['H2'] = future date
        pass

    def setUp(self):
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option(
                'debuggerAddress', 'localhost:9222')

            self.driver = webdriver.Chrome(
                options=chrome_options, executable_path="C:\\Users\\Aman Bhatia\\OneDrive - Gemini Solutions\\Desktop\\Contripoint_Project\\ChromeDriver\\chromedriver.exe")
            print("Browser Connected")

            self.driver.implicitly_wait(10)

            self.driver

            self.driver.get(
                "https://dev-contripoint.geminisolutions.com/#/dashboard")

            print("\n Login Successfully \n")

            print("\n 1 - Gemini Id and Password successfully login")
            # self.ws['C2'] = 'Login'
            # self.ws['G2'] = 'login Success'

            # self.wb.save(self.filename)

        except Exception as e:
            print(e)
            print("\n 1 - Gemini Id and Password  login failed")
            # self.ws['C2'] = 'Login'
            # self.ws['G2'] = 'login failed'
            # self.wb.save(self.filename)

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
            # self.ws['C3'] = 'Admin Portal--Add New button'
            # self.ws['G3'] = 'Pass'

            # self.wb.save(self.filename)

        except Exception as e:
            print("\n 2 - Clicking on Admin Portal gets fail.")
            print("\n 3 - Selecting Add New button gets fail.")
            print(e)
            print("\n 4 - Error in selecting Admin portal--Add New button button")
            # self.ws['C3'] = 'Admin Portal--Add New button'
            # self.ws['G3'] = 'Fail'

            # self.wb.save(self.filename)

    def Allotment_Type(self):
        """
        """
        try:
            # selecting Dropdown
            self.driver.find_element(
                By.XPATH, '//mat-select[@formcontrolname="allotmentData"]').click()

            # Allot Budget
            self.driver.find_element(
                By.XPATH, '//span[text()=" Allot Budget "]').click()

            print("\n 5 - Selecting 'Allot Budget'")
            # self.ws['C4'] = 'Dropdown--Allot Budget'
            # self.ws['G4'] = 'Pass'

            # self.wb.save(self.filename)

        except Exception as e:
            print("\n 5 - Selecting 'Allot Budget' gets fail")
            print(e)
            # self.ws['C4'] = 'Dropdown--Allot Budget'
            # self.ws['G4'] = 'Pass'

            # self.wb.save(self.filename)

    def Members_Type(self):
        """
        """
        try:
            # Selecting Member's type dropdown
            self.driver.find_element(
                By.XPATH, '//mat-select[@formcontrolname="member_type"]').click()

            # Upload Employee Excel
            self.driver.find_element(
                By.XPATH, '//span[text()=" Upload Employee Excel "]').click()

            print("\n 6 - Selecting 'Upload Employee Excel'")
            # self.ws['C5'] = 'Dropdown--Upload Employee Excel'
            # self.ws['G5'] = 'Pass'

            # self.wb.save(self.filename)

        except Exception as e:
            print("\n 6 - Selecting 'Upload Employee Excel' gets fail")
            print(e)

            # self.ws['C5'] = 'Dropdown--Upload Employee Excel'
            # self.ws['G5'] = 'Fail'

            # self.wb.save(self.filename)

    def Import_excel(self, pyautogui=None):
        """
        """
        try:
            # Import Data from Excel Button
            self.driver.find_element(
                By.XPATH, '//button[text()=" Import Data from Excel "]').click()

            # Import Data Screen
            self.driver.find_element(
                By.XPATH, '//label[@id="attachment_btn"]').click()
            time.sleep(5)

            pyautogui.write(Pdf_file)
            pyautogui.press('enter')
            print("\n 7 - Budget Excel sheet Upload successfully")
            # self.ws['C5'] = 'Allot Budget Excel sheet'
            # self.ws['G5'] = 'Pass'

            # self.wb.save(self.filename)

        except Exception as e:
            print("\n 7 - Budget Excel sheet Uploading gets fail")
            # self.ws['C5'] = 'Allot Budget Excel sheet'
            # self.ws['G5'] = 'Fail'

            # self.wb.save(self.filename)

    def Submit(self):
        """
        """
        try:
            self.driver.find_element(
                By.XPATH, '//button[@id="add_btn" and text()=" SUBMIT "]').click()

            print("\n 8 - All Details get SUBMIT successfully.")

            # self.ws['C6'] = 'SUBMIT'
            # self.ws['G6'] = 'Pass'
            # self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN SubmitButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 8 - All Details get fail while SUBMIT.")
            # self.ws['C6'] = 'SUBMIT'
            # self.ws['G6'] = 'Fail'
            # self.wb.save(self.filename)

    def OKButton(self):
        """

        """
        try:
            # OK Button
            self.driver.find_element(By.XPATH, '//span[text()="OK"]').click()
            print("\n 9 - Clicking OK Button")

            # self.ws['C7'] = 'OK BUTTON'
            # self.ws['G7'] = 'Pass'
            # self.wb.save(self.filename)

            # self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN OKButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 9 - Unable to click OK Button")
            # self.ws['C7'] = 'OK BUTTON'
            # self.ws['G7'] = 'Fail'
            # self.wb.save(self.filename)

    def SplitAmount(self):
        """
        """
        try:
            self.driver.find_element(
                By.XPATH, '//input[@type="number"]').send_keys("600")

            print("\n 10 - AllotBudget(₹)= 600")

            # ConversionRatio
            print("Conversion Ratio= " + (WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@ng-reflect-name="conversionRatio"]'))).text))

            # Split Amount
            self.driver.find_element(
                By.XPATH, '//button[text()="Split Amount"]').click()

            print("\n 11 - Split Amount Done")

            # AllotButton
            self.driver.find_element(
                By.XPATH, '//button[text()="Allot"]').click()

            print("\n 10 - Alloting Budget(₹) to selected employees")

            # self.ws['C8'] = 'Allot Budget(₹)'
            # self.ws['G8'] = 'Pass'
            # self.wb.save(self.filename)

            # self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN OKButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 10 - Unable to Allot the Budget(₹)")
            # self.ws['C8'] = 'Alloting Budget(₹)'
            # self.ws['G8'] = 'Fail'
            # self.wb.save(self.filename)

    def OK(self):
        """

        """

        try:
            # OK Button
            self.driver.find_element(
                By.XPATH, '//button[@id="ok_btn"]').click()
            print("\n 11 - Clicking OK Button")

            # self.ws['C9'] = 'OK BUTTON'
            # self.ws['G9'] = 'Pass'
            # self.wb.save(self.filename)

            # self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN OKButton >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Unable to click OK Button")
            # self.ws['C9'] = 'OK BUTTON'
            # self.ws['G9'] = 'Fail'
            # self.wb.save(self.filename)

    def ActionButton(self):
        """

        """
        try:
            # View Button
            self.driver.find_element(
                By.XPATH, '//mat-icon[text()="arrow_drop_down"]').click()
            print("\n 11 - Clicking View Button")

            # self.ws['C9'] = 'Action-View BUTTON'
            # self.ws['G9'] = 'Pass'
            # self.wb.save(self.filename)

            # self.wb.save(self.filename)

        except Exception as e:
            print("\n\nERROR IN View Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Unable to click View Button")
            # self.ws['C9'] = 'Action-View BUTTON'
            # self.ws['G9'] = 'Fail'
            # self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = AllotBudget()
    tb.setUp()
    tb.Admin_Portal()
    tb.Allotment_Type()
    tb.Members_Type()
    tb.Import_excel()
    tb.Submit()
    tb.OKButton()
    tb.SplitAmount()
    tb.OK()
    tb.ActionButton()
