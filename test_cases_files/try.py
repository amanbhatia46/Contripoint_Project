from Functionals import *
from datainputs import *


class CEvent(unittest.TestCase):

    def __init__(self):
        """ interact with the underlying operating system."""
        # import os
        # print(os.path.join(os.getcwd() + "\\result.xlsx"), ">>>>>>")
        # self.filename = os.path.join(os.getcwd() + "\\result.xlsx")
        # #self.wbb = load_workbook(filename=self.filename)
        # self.index_sheet = 0
        # if 'Contest Event' not in #self.wbb.sheetnames:
        #     #self.wbb.create_sheet('Contest Event')
        #     #self.wbb.save(os.path.join(os.getcwd() + "\\result.xlsx"))
        # #self.wbb = load_workbook(filename=self.filename)
        # ##self.wbs = #self.wbb.active
        # for i, n in enumerate(#self.wbb.sheetnames):
        #     if n == 'Contest Event':
        #         self.index_sheet = i
        #         break
        # #self.wbb.active = self.index_sheet
        # ##self.wbs = #self.wbb.active
        # #self.wbb.active = 1
        # ##self.wbs['A1'] = 'Email'
        # ##self.wbs['B1'] = 'Password'
        # ##self.wbs['C1'] = 'Test Case Module'
        # ##self.wbs['G1'] = 'Result'
        # ##self.wbs['H1'] = 'Date and Time'
        # #self.wbb.save(os.path.join(os.getcwd() + "\\result.xlsx"))

        # # datetime object containing current date and time
        # futuredate = str(datetime.now())
        # print(futuredate)
        # ##self.wbs['H2'] = futuredate
        pass

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
            ##self.wbs['C2'] = 'Login'
            ##self.wbs['G2'] = 'login Success'

            #self.wbb.save(self.filename)

        except Exception as e:
            print(e)
            print("\n 1 - Gemini Id and Password  login failed")
            ##self.wbs['C2'] = 'Login'
            ##self.wbs['G2'] = 'login failed'
            #self.wbb.save(self.filename)

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
            print("\n 2 - Clicking on Events gets fail ")
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
            ##self.wbs['C3'] = 'Uploading Banner Image'
            ##self.wbs['G3'] = 'Pass'

            #self.wbb.save(self.filename)
            time.sleep(3)

        except Exception as e:
            print("\n ERROR IN Adding Banner Image >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 4 - Unable to Add Banner Image")
            ##self.wbs['C3'] = 'Uploading Banner Image'
            ##self.wbs['G3'] = 'Fail'

            #self.wbb.save(self.filename)

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

            print("\n 4 - Listing Image Upload successfully")

            ##self.wbs['C4'] = 'Upload Listing Image'
            ##self.wbs['G4'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Adding Listing Image >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 4 - Unable to Add Listing Image")

            ##self.wbs['C4'] = 'Upload Listing Image'
            ##self.wbs['G4'] = 'Fail'
            #self.wbb.save(self.filename)

    def Event_Name(self):
        """

        """
        try:
            # Entering  Event Name
            self.driver.find_element(
                By.XPATH, '//input[@formcontrolname="event_name"]').send_keys("Contest Event")
            time.sleep(5)
            print("\n 5 - Entering Event Name ")

            ##self.wbs['C5'] = 'Event Name'
            ##self.wbs['G5'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Event Name >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 5 - Unable to Add Event Name")

            ##self.wbs['C5'] = 'Event Name'
            ##self.wbs['G5'] = 'Fail'
            #self.wbb.save(self.filename)

    def Description(self):
        """

        """
        try:
            # Entering Description
            self.driver.find_element(
                By.XPATH, '//textarea[@formcontrolname="event_desc"]').send_keys("Please take participate in Contest Event and win Rewards")
            time.sleep(5)
            print("\n 6 - Entering Description  ")

            ##self.wbs['C6'] = 'Description '
            ##self.wbs['G6'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Description  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 6 - Unable to Add Description ")

            ##self.wbs['C6'] = 'Description '
            ##self.wbs['G6'] = 'Fail'
            #self.wbb.save(self.filename)

    def Next_Button(self):
        """

        """
        try:
            # Clicking on Next Button
            self.driver.find_element(
                By.XPATH, '//div//div//button[@class="mat-stepper-next" and @id="add_btn"]').click()
            time.sleep(5)
            print("\n 7 - Clicking on Next Button  ")

            ##self.wbs['C7'] = 'Next Button '
            ##self.wbs['G7'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Next Button  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 7 - Unable to Add Next Button ")

            ##self.wbs['C7'] = 'Next Button '
            ##self.wbs['G7'] = 'Fail'
            #self.wbb.save(self.filename)

    def Event_Type(self):
        """

        """
        try:
            # Clicking on Event Type
            self.driver.find_element(
                By.XPATH, '//span[text()="Select"]').click()
            time.sleep(5)
            print("\n 8 - Clicking on Event Type Dropdown ")

            self.driver.find_element(
                By.XPATH, ' //span[text()=" Contest "]').click()
            time.sleep(5)

            print("\n 9 - Event Type - Contest Event")

            ##self.wbs['C8'] = 'Event Type - Contest Event'
            ##self.wbs['G8'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Event Type  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 9 - Unable to Select Event Type ")

            ##self.wbs['C8'] = 'Event Type - Contest Event'
            ##self.wbs['G8'] = 'Fail'
            #self.wbb.save(self.filename)

    def Contribution_category(self):
        """

        """
        try:
            # Click on Category Dropdown
            self.driver.find_element(
                By.XPATH, '//span[text()="Select"]').click()
            time.sleep(6)
            print("\n 9 - Opening Dropdown list")

            # Selecting Certificate and Projects
            self.driver.find_element(
                By.XPATH, '//span[text()=" Certificate "]').click()
            time.sleep(5)
            print("\n 10 - Contribution Category - Certificate")

            self.driver.find_element(
                By.XPATH, '//span[text()=" Projects "]').click()
            time.sleep(5)
            print("\n 11 - Contribution Category - Projects ")

            print("\n 12 - Contribution Category - Certificate and Projects")

            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="Add Events"]')))

            source = self.driver.find_element(
                By.XPATH, '//p[text()="Add Events"]')
            time.sleep(6)

            # action chain object creation
            action = ActionChains(self.driver)
            time.sleep(6)

            # double click operation and perform
            action.click(source).perform()
            time.sleep(6)
            

            ##self.wbs['C9'] = 'Contribution Category - Certificate and Projects'
            ##self.wbs['G9'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Contribution Category  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 12 - Unable to Select Contributions From Dropdown list ")

            ##self.wbs['C9'] = 'Event Type - Contest Event'
            ##self.wbs['G9'] = 'Fail'
            #self.wbb.save(self.filename)

    def Start_Date(self):
        """

        """
        try:
            date = self.driver.find_element(
                By.XPATH, '//input[@formcontrolname="start_date"]').click()
            time.sleep(5)

            print("\n 13 - Clicking on Start Date Calander ")

            self.driver.find_element(
                By.CSS_SELECTOR, ".mat-calendar-body-today").click()
            time.sleep(5)

            ##self.wbs['C10'] = 'Start Date'
            ##self.wbs['G10'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Start Date  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 13 - Unable to Add Start Date ")

            ##self.wbs['C10'] = 'Start Date'
            ##self.wbs['G10'] = 'Fail'
            #self.wbb.save(self.filename)

    def End_Date(self):
        """

        """
        try:
            # Clicking on End Date
            self.driver.find_element(
                By.XPATH, '//input[@formcontrolname="end_date"]').click()
            time.sleep(5)
            print("\n 14 - Clicking on End Date Calander ")

            self.driver.find_element(
                By.CSS_SELECTOR, ".mat-calendar-body-today").click()
            time.sleep(5)

            ##self.wbs['C11'] = 'End Date'
            ##self.wbs['G11'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN End Date  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 14 - Unable to Add End Date ")

            ##self.wbs['C11'] = 'End Date'
            ##self.wbs['G11'] = 'Fail'
            #self.wbb.save(self.filename)

    def Reward(self):
        """

        """
        try:
            # Entering Reward
            self.driver.find_element(
                By.XPATH, '//textarea[@formcontrolname="reward_desc"]').send_keys("Cash Rs1000/-")
            time.sleep(5)
            print("\n 15 - Entering Reward  ")

            ##self.wbs['C12'] = 'Reward '
            ##self.wbs['G12'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Reward  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 15 - Unable to Add Reward ")

            ##self.wbs['C12'] = 'Reward '
            ##self.wbs['G12'] = 'Fail'
            #self.wbb.save(self.filename)

    def Next_Button1(self):
        """

        """
        try:
            # Clicking on Next Button
            self.driver.find_element(
                By.XPATH, '//div[4]//button[text()=" NEXT "]').click()
            time.sleep(5)
            print("\n 16 - Clicking on Next Button  ")

            ##self.wbs['C13'] = 'Next Button '
            ##self.wbs['G13'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Next Button  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 16 - Unable to Add Next Button ")

            ##self.wbs['C13'] = 'Next Button '
            ##self.wbs['G13'] = 'Fail'
            #self.wbb.save(self.filename)

    def Participant_Category(self):
        """
        """
        try:
            # Clicking on Participant Category
            self.driver.find_element(
                By.XPATH, '//span[text()="Select"]').click()
            time.sleep(5)
            print("\n 17 - Clicking on Participant Category  ")

            # Selecting Individual Participants From Dropdown
            self.driver.find_element(
                By.XPATH,'//span[text()=" Select individual participants "]').click()
            time.sleep(5)
            print("\n 18 - Selecting Individual Participants")

            ##self.wbs['C14'] = 'Participant Category - Individual Participants '
            ##self.wbs['G14'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Participant Category  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 18 - Unable To Select Individual Participants")

            ##self.wbs['C14'] = 'Participant Category - Individual Participants '
            ##self.wbs['G14'] = 'Fail'
            #self.wbb.save(self.filename)

    def Eligible_Participant(self):
        """

        """
        try:
            # Inserting Voter's Name (Aman Bhatia) in Field
            self.driver.find_element(
                By.XPATH,'//input[@name="searchText"]').send_keys('Aman Bhatia')
            time.sleep(5)

            # Clicking on pseudo-checkbox
            self.driver.find_element(
                By.XPATH, '//div[text()=" GSI C 1278 Aman Bhatia "]').click()
            time.sleep(5)
            print("\n 19 - Eligible Participant- Aman Bhatia")

            # clear the text entered in Field
            self.driver.find_element(By.XPATH,'//input[@name="searchText"]').clear()

            # Inserting Voter's Name (Alpana Upadhyay) in Field
            self.driver.find_element(
                By.XPATH,'//input[@name="searchText"]').send_keys('Alpana Upadhyay')
            time.sleep(5)

            # Clicking on pseudo-checkbox
            self.driver.find_element(
                By.XPATH, '//div[text()=" GSI G 1181 Alpana Upadhyay "]').click()
            time.sleep(5)
            print("\n 20 - Eligible Participant- Alpana Upadhyay")

            print("\n 21 - Eligible Participant - Aman Bhatia, Alpana Upadhyay")

            ##self.wbs['C15'] = 'Eligible Participant - Aman Bhatia, Alpana Upadhyay'
            ##self.wbs['G15'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Eligible Participant  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print(
                "\n 21 - Unable To Select Eligible Participant - Aman Bhatia, Alpana Upadhyay")

            ##self.wbs['C15'] = 'Eligible Participant - Aman Bhatia, Alpana Upadhyay'
            ##self.wbs['G15'] = 'Fail'
            #self.wbb.save(self.filename)

    def Cutoff_Points(self):
        """

        """
        try:
            # Clicking on Cutoff Points
            self.driver.find_element(
                By.XPATH,'//input[@ng-reflect-type="number"]').send_keys('100')
            time.sleep(5)
            print("\n 22 - Cutoff Points - 100")

            ##self.wbs['C16'] = 'Cutoff Points '
            ##self.wbs['G16'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Cutoff Points  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 22 - Unable to Add Cutoff Points ")

            ##self.wbs['C16'] = 'Cutoff Points '
            ##self.wbs['G16'] = 'Fail'
            #self.wbb.save(self.filename)

    def Submit(self):
        """

        """
        try:
            # Clicking on Submit
            self.driver.find_element(
                By.XPATH, '//button[text()="Submit"]').click()
            time.sleep(5)
            print("\n 23 - Clicking on Submit ")

            ##self.wbs['C17'] = 'Submit '
            ##self.wbs['G17'] = 'Pass'
            #self.wbb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Submit  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 23 - Unable to Add Submit ")

            ##self.wbs['C17'] = 'Submit '
            ##self.wbs['G17'] = 'Fail'
            #self.wbb.save(self.filename)

    def OK_Button(self):
        """

        """
        try:
            # Warning popup
            self.driver.find_element(
                By.XPATH, '//span[text()="CONTINUE"]').click()
            print("\n 24 - Clicking on Continue Button")
            time.sleep(6)

            # OK Button
            ok= self.driver.find_element(
                By.XPATH, '//span[text()="OK"]')
            time.sleep(6)
            ok.click()
            print("\n 25 - Clicking OK Button")
            ##self.wbs['C18'] = 'OK Button'
            ##self.wbs['G18'] = 'Pass'

            #self.wbb.save(self.filename)
           

        except Exception as e:
            print("\n\nERROR IN OK Button >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 25 - Unable to Click OK Button")
            ##self.wbs['C18'] = 'OK Button'
            ##self.wbs['G18'] = 'Fail'

            #self.wbb.save(self.filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = CEvent()
    tb.setUp()
    tb.Events()
    tb.Add_Banner_Image()
    tb.Add_Listing_Image()
    tb.Event_Name()
    tb.Description()
    tb.Next_Button()
    tb.Event_Type()
    tb.Contribution_category()
    tb.Start_Date()
    tb.End_Date()
    tb.Reward()
    tb.Next_Button1()
    tb.Participant_Category()
    tb.Eligible_Participant()
    tb.Cutoff_Points()
    tb.Submit()
    tb.OK_Button()
