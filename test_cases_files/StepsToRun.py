
"""
1. Open cmd and run command only 1 time --
cd C:\Program Files\Google\Chrome\Application

chrome.exe --remote-debugging-port=9222 --user-data-dir=C:\Selenium\Chromedata

2. when new tab gets open then minimize it and run our code.

3. switch to newly open window to see changes .




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option('debuggerAddress', 'localhost:9222')

browser = webdriver.Chrome(options=chrome_options,executable_path="C:\\Users\\Aman Bhatia\\OneDrive - Gemini Solutions\\Desktop\\Contripoint_Project\\ChromeDriver\\chromedriver.exe")

print("Browser Connected")

browser.get("https://dev-contripoint.geminisolutions.com/#/login")
print("opening contripoint")

"""