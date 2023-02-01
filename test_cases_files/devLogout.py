from Functionals import *
from datainputs import *


class LogoutFunctionality(unittest.TestCase):

    def __init__(self):
        pass

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

            button = self.driver.find_element(
                By.XPATH, '//button[contains(., "Login with Gemini mail")]')
            button.click()

            print("\n Login Successfull \n")
            print("\n 1 - Gemini Id and Password successfully login")


        except Exception as e:
            print(e)
            print("\n 1 - Gemini Id and Password  login failed")

    def Profile(self):
        """
            Report Bug
        """
        try:
            #Profile
            button = self.driver.find_element(
                By.XPATH, '//a//img[@src="../../assets/images/navbar-person.png"]')
            button.click()

            print("\n 1 - Selecting Profile")


        except Exception as e:
            print("\n\n ERROR IN Selecting Profile >>>>>>>>>>>>>>>\n\n")
            print("\n 1 - Selecting Profile gets fail")


    def Logout(self):
        """
            Report Bug
        """
        try:
            #Logout
            self.driver.find_element(
                By.XPATH, '//button//span[text()="Logout"]').click() 

            print("\n 2 - Logging out")

            time.sleep(2)
            print(
                "\n 3 - You have logout successfully from: " + self.driver.title)
            print("\n 4 - The URL of the page is: ", self.driver.current_url)
            print("\n 5 - All the details are successfully printed.")

        except Exception as e:
            print("\n\n ERROR IN Report a Bug/Feedback >>>>>>>>>>>>>>>\n\n")
            print("\n 2 - Selecting Report a Bug/Feedback gets fail")

            print(
                "\n 3 - You have login successfully and welcome to the site: " + self.driver.title)
            print("\n 4 - The URL of the page is: ", self.driver.current_url)
            print("\n 5 - All the details are successfully printed.")


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    tb = LogoutFunctionality()
    tb.setUp()
    tb.Profile()
    tb.Logout() 