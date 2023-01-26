from Functionals import *
from datainputs import *


class PEvent(unittest.TestCase):

    def __init__(self):
        """ interact with the underlying operating system."""
        import os
        print(os.path.join(os.getcwd() + "\\xyz.xlsx"), ">>>>>>")
        self.filename = os.path.join(os.getcwd() + "\\xyz.xlsx")
        self.wb = load_workbook(filename=self.filename)
        self.index_sheet = 0
        if 'Polling Event' not in self.wb.sheetnames:
            self.wb.create_sheet('Polling Event')
            self.wb.save(os.path.join(os.getcwd() + "\\xyz.xlsx"))
        self.wb = load_workbook(filename=self.filename)
        self.ws = self.wb.active
        for i, n in enumerate(self.wb.sheetnames):
            if n == 'Polling Event':
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
            chrome_options.add_experimental_option(
                'debuggerAddress', 'localhost:9222')

            self.driver = webdriver.Chrome(
                options=chrome_options, executable_path="C:\\Users\\Aman Bhatia\\OneDrive - Gemini Solutions\\Desktop\\Contripoint_Project\\ChromeDriver\\chromedriver.exe")
            print("Browser Connected")

            # driver = self.driver

            self.driver.get(
                "https://dev-contripoint.geminisolutions.com/#/dashboard")

            time.sleep(5)

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

    def Events(self):
        """

        """
        try:

            # Clicking on Events
            self.driver.find_element(
                By.XPATH, '//span[text()="Events"]').click()
            time.sleep(6)
            print("\n 2 - Clicking on Events ")

            # Create New Event
            self.driver.find_element(
                By.XPATH, '//button[@id="add_btn"]').click()
            time.sleep(5)
            print("\n 3 - Creating New Event")

        except Exception as e:
            print("\n 3 - Clicking on Events gets fail")
            print("\n 3 - Error in Creating New Event")
            print(e)

    def Add_Banner_Image(self):
        """

        """
        try:
            # Adding Banner Image
            self.driver.find_element(
                By.XPATH, '//img[@src="../../../../assets/images/banner-image.png"]').click()
            time.sleep(5)
            pyautogui.write(banner_image)
            pyautogui.press('enter')
            print("\n 4 - Banner Image Upload successfully")
            self.ws['C4'] = 'Uploading Banner Image'
            self.ws['G4'] = 'Pass'

            self.wb.save(self.filename)
            time.sleep(3)

        except Exception as e:
            print("\n ERROR IN Adding Banner Image >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 4 - Unable to Add Banner Image")
            self.ws['C4'] = 'Uploading Banner Image'
            self.ws['G4'] = 'Fail'

            self.wb.save(self.filename)

    def Add_Listing_Image(self):
        """

        """
        try:
            # Adding Listing Image
            self.driver.find_element(
                By.XPATH, '//img[@src="../../../../assets/images/listing-image.png"]').click()
            time.sleep(5)
            pyautogui.write(listing_image)
            pyautogui.press('enter')
            time.sleep(3)

            print("\n 5 - Listing Image Upload successfully")

            self.ws['C5'] = 'Upload Listing Image'
            self.ws['G5'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Adding Listing Image >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 5 - Unable to Add Listing Image")

            self.ws['C5'] = 'Upload Listing Image'
            self.ws['G5'] = 'Fail'
            self.wb.save(self.filename)

    def Event_Name(self):
        """

        """
        try:
            # Entering  Event Name
            self.driver.find_element(
                By.XPATH, '//input[@formcontrolname="event_name"]').send_keys("Polling Event")
            time.sleep(5)
            print("\n 6 - Entering Event Name ")

            self.ws['C6'] = 'Event Name'
            self.ws['G6'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Event Name >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 6 - Unable to Add Event Name")

            self.ws['C6'] = 'Event Name'
            self.ws['G6'] = 'Fail'
            self.wb.save(self.filename)

    def Description(self):
        """

        """
        try:
            # Entering Description
            self.driver.find_element(
                By.XPATH, '//textarea[@formcontrolname="event_desc"]').send_keys("Please take participate in Polling Event and win Rewards")
            time.sleep(5)
            print("\n 7 - Entering Description  ")

            self.ws['C7'] = 'Description '
            self.ws['G7'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Description  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 7 - Unable to Add Description ")

            self.ws['C7'] = 'Description '
            self.ws['G7'] = 'Fail'
            self.wb.save(self.filename)

    def Next_Button(self):
        """

        """
        try:
            # Clicking on Next Button
            self.driver.find_element(
                By.XPATH, '//div//div//button[@class="mat-stepper-next" and @id="add_btn"]').click()
            time.sleep(5)
            print("\n 8 - Clicking on Next Button  ")

            self.ws['C8'] = 'Next Button '
            self.ws['G8'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Next Button  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 8 - Unable to Add Next Button ")

            self.ws['C8'] = 'Next Button '
            self.ws['G8'] = 'Fail'
            self.wb.save(self.filename)

    def Event_Type(self):
        """

        """
        try:
            # Clicking on Event Type
            self.driver.find_element(
                By.XPATH, '//span[text()="Select"]').click()
            time.sleep(5)
            print("\n 9 - Clicking on Event Type Dropdown ")

            self.driver.find_element(
                By.XPATH, '//span[text()=" Polling Event "]').click()
            time.sleep(5)

            print("\n 10 - Event Type - Polling Event")

            self.ws['C9'] = 'Event Type - Polling Event'
            self.ws['G9'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Event Type  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 10 - Unable to Select Event Type ")

            self.ws['C9'] = 'Event Type - Polling Event'
            self.ws['G9'] = 'Fail'
            self.wb.save(self.filename)

    def Start_Date(self):
        """

        """
        try:
            date = self.driver.find_element(
                By.XPATH, '//input[@formcontrolname="start_date"]').click()
            time.sleep(5)

            print("\n 11 - Clicking on Start Date Calander ")

            self.driver.find_element(
                By.CSS_SELECTOR, ".mat-calendar-body-today").click()
            time.sleep(5)

            self.ws['C10'] = 'Start Date'
            self.ws['G10'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Start Date  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 11 - Unable to Add Start Date ")

            self.ws['C10'] = 'Start Date'
            self.ws['G10'] = 'Fail'
            self.wb.save(self.filename)

    def End_Date(self):
        """

        """
        try:
            # Clicking on End Date
            self.driver.find_element(
                By.XPATH, '//input[@formcontrolname="end_date"]').click()
            time.sleep(5)
            print("\n 12 - Clicking on End Date Calander ")

            self.driver.find_element(
                By.CSS_SELECTOR, ".mat-calendar-body-today").click()
            time.sleep(5)

            self.ws['C11'] = 'End Date'
            self.ws['G11'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN End Date  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 12 - Unable to Add End Date ")

            self.ws['C11'] = 'End Date'
            self.ws['G11'] = 'Fail'
            self.wb.save(self.filename)

    def Reward(self):
        """

        """
        try:
            # Entering Reward
            self.driver.find_element(
                By.XPATH, '//textarea[@formcontrolname="reward_desc"]').send_keys("Cash Rs1000/-")
            time.sleep(5)
            print("\n 13 - Entering Reward  ")

            self.ws['C12'] = 'Reward '
            self.ws['G12'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Reward  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 13 - Unable to Add Reward ")

            self.ws['C12'] = 'Reward '
            self.ws['G12'] = 'Fail'
            self.wb.save(self.filename)

    def Next_Button1(self):
        """

        """
        try:
            # Clicking on Next Button
            self.driver.find_element(
                By.XPATH, '//div[4]//button[text()=" NEXT "]').click()
            time.sleep(5)
            print("\n 14 - Clicking on Next Button  ")

            self.ws['C13'] = 'Next Button '
            self.ws['G13'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Next Button  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 14 - Unable to Add Next Button ")

            self.ws['C13'] = 'Next Button '
            self.ws['G13'] = 'Fail'
            self.wb.save(self.filename)

    def Voters_Category(self):
        """
        """
        try:
            # Clicking on Participant Category
            self.driver.find_element(
                By.XPATH, '//span[text()="Select"]').click()
            time.sleep(5)
            print("\n 15 - Clicking on Voters Category  ")

            # Selecting Individual Voters From Dropdown
            self.driver.find_element(
                By.XPATH, '//span[text()=" Select individual participants "]').click()
            time.sleep(5)
            print("\n 16 - Selecting Individual Participants")

            self.ws['C14'] = 'Voters Category - Individual Participants '
            self.ws['G14'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Voters Category  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 16 - Unable To Select Individual Voters")

            self.ws['C14'] = 'Voters Category - Individual Participants '
            self.ws['G14'] = 'Fail'
            self.wb.save(self.filename)

    def Eligible_Voters(self):
        """

        """
        try:
            # Inserting Voter's Name (Aman Bhatia) in Field
            self.driver.find_element(
                By.XPATH, '//input[@name="searchText"]').send_keys('Aman Bhatia')
            time.sleep(5)

            # Clicking on pseudo-checkbox
            self.driver.find_element(
                By.XPATH, '//div[text()=" GSI C 1278 Aman Bhatia "]').click()
            time.sleep(5)
            print("\n 17 - Eligible Participant- Aman Bhatia")

            # clear the text entered in Field
            self.driver.find_element(
                By.XPATH, '//input[@name="searchText"]').clear()

            # Inserting Voter's Name (Alpana Upadhyay) in Field
            self.driver.find_element(
                By.XPATH, '//input[@name="searchText"]').send_keys('Alpana Upadhyay')
            time.sleep(5)

            # Clicking on pseudo-checkbox
            self.driver.find_element(
                By.XPATH, '//div[text()=" GSI G 1181 Alpana Upadhyay "]').click()
            time.sleep(5)
            print("\n 18 - Eligible Voters- Alpana Upadhyay")

            print("\n 19 - Eligible Voters - Aman Bhatia, Alpana Upadhyay")

            self.ws['C15'] = 'Eligible Voters - Aman Bhatia, Alpana Upadhyay'
            self.ws['G15'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Eligible Voters  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print(
                "\n 19 - Unable To Select Eligible Voters - Aman Bhatia, Alpana Upadhyay")

            self.ws['C15'] = 'Eligible Voters - Aman Bhatia, Alpana Upadhyay'
            self.ws['G15'] = 'Fail'
            self.wb.save(self.filename)

    def Next_Button2(self):
        """

        """
        try:
            # Clicking on Next Button
            self.driver.find_element(
                By.XPATH, '//div[3][contains(@class, "mat-horizontal-stepper-content")]//button[text()=" NEXT "]').click()
            time.sleep(5)
            print("\n 20 - Clicking on Next Button  ")

            self.ws['C16'] = 'Next Button '
            self.ws['G16'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Next Button  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 20 - Unable to Add Next Button ")

            self.ws['C16'] = 'Next Button '
            self.ws['G16'] = 'Fail'
            self.wb.save(self.filename)

    def Participant_Category(self):
        """
        """
        try:
            time.sleep(5)
            # Clicking on Participant Category

            element = self.driver.find_element(By.XPATH,'//div//mat-select[@formcontrolname="employ_select"]')
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            time.sleep(5)

            self.driver.find_element(By.XPATH,'//div//mat-select[@formcontrolname="employ_select"]').click()
            time.sleep(5)
            print("\n 21 - Clicking on Participant Category  ")

            # Selecting Individual Participants From Dropdown
            self.driver.find_element(
                By.XPATH, '//span[text()=" Select individual participants "]').click()
            time.sleep(5)
            print("\n 22 - Selecting Individual Participants")

            self.ws['C17'] = 'Participant Category - Individual Participants '
            self.ws['G17'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Participant Category  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 22 - Unable To Select Individual Participants")

            self.ws['C17'] = 'Participant Category - Individual Participants '
            self.ws['G17'] = 'Fail'
            self.wb.save(self.filename)

    def Eligible_Participant(self):
        """

        """
        try:
            # Inserting Voter's Name (Aman Bhatia) in Field
            self.driver.find_element(
                By.XPATH, '//div[4]//input[@name="searchText"]').send_keys('Aman Bhatia')
            time.sleep(5)

            # Clicking on pseudo-checkbox
            self.driver.find_element(
                By.XPATH, '//div[text()=" GSI C 1278 Aman Bhatia "]').click()
            time.sleep(5)
            print("\n 23 - Eligible Participant- Aman Bhatia")

            # clear the text entered in Field
            self.driver.find_element(
                By.XPATH, '//div[4]//input[@name="searchText"]').clear()

            # Inserting Voter's Name (Alpana Upadhyay) in Field
            self.driver.find_element(
                By.XPATH, '//div[4]//input[@name="searchText"]').send_keys('Alpana Upadhyay')
            time.sleep(5)

            # Clicking on pseudo-checkbox
            self.driver.find_element(
                By.XPATH, '//div[text()=" GSI G 1181 Alpana Upadhyay "]').click()
            time.sleep(5)
            print("\n 24 - Eligible Participant- Alpana Upadhyay")

            print("\n 25 - Eligible Participant - Aman Bhatia, Alpana Upadhyay")

            self.ws['C18'] = 'Eligible Participant - Aman Bhatia, Alpana Upadhyay'
            self.ws['G18'] = 'Pass'
            self.wb.save(self.filename)
            time.sleep(5)

        except Exception as e:
            print("\n ERROR IN Eligible Participant  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print(
                "\n 25 - Unable To Select Eligible Participant - Aman Bhatia, Alpana Upadhyay")

            self.ws['C18'] = 'Eligible Participant - Aman Bhatia, Alpana Upadhyay'
            self.ws['G18'] = 'Fail'
            self.wb.save(self.filename)

    def Submit(self):
        """

        """
        try:
            # Clicking on Submit
            self.driver.find_element(
                By.XPATH, '//button[text()="Submit"]').click()
            time.sleep(5)
            print("\n 26 - Clicking on Submit ")

            self.ws['C19'] = 'Submit '
            self.ws['G19'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Submit  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 26 - Unable to Add Submit ")

            self.ws['C19'] = 'Submit '
            self.ws['G19'] = 'Fail'
            self.wb.save(self.filename)

    def OK_Button(self):
        """

        """
        try:
            # OK Button
            ok = self.driver.find_element(
                By.XPATH, '//span[text()="OK"]').click()
            print("\n 27 - Clicking OK Button")
            self.ws['C20'] = 'OK Button'
            self.ws['G20'] = 'Pass'

            self.wb.save(self.filename)
            time.sleep(6)

        except Exception as e:
            print("\n\nERROR IN OK Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 27 - Unable to Click OK Button")
            self.ws['C20'] = 'OK Button'
            self.ws['G20'] = 'Fail'

            self.wb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = PEvent()
    tb.setUp()
    tb.Events()
    tb.Add_Banner_Image()
    tb.Add_Listing_Image()
    tb.Event_Name()
    tb.Description()
    tb.Next_Button()
    tb.Event_Type()
    tb.Start_Date()
    tb.End_Date()
    tb.Reward()
    tb.Next_Button1()
    tb.Voters_Category()
    tb.Eligible_Voters()
    tb.Next_Button2()
    tb.Participant_Category()
    tb.Eligible_Participant()
    tb.Submit()
    tb.OK_Button()
