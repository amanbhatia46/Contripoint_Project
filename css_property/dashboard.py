# '''
# FUncitonal

# '''
# from os import writev
# from typing import Sized
# from json import load
# import unittest
# import time
# import HtmlTestRunner as x
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from openpyxl import load_workbook
# from datetime import datetime, timedelta


# class Css_Dashboard(unittest.TestCase):

#     def __init__(self):
#         self.filename='/home/am.bhatia/Desktop/contripoint/abc1.xlsx'
#         self.wb = load_workbook(filename=self.filename)
#         self.ws=self.wb.active
#         self.wb.create_sheet('Dashboard_CSS_Properties')
#         self.ws.append([self.filename])
#         # self.ws.title = ""
#         print(self.wb)
#         print(self.wb.sheetnames)


#         # datetime object containing current date and time
#         futuredate = datetime.now()
#         print(futuredate)
#         self.ws['H2'] = futuredate


#     def setUp(self):
#         '''
#           The setUp() methods allows to define set of instructions.If this method it self raises an exception while executing tests, the test methods will not be executed.
#         '''
#         try:
#             s=Service(ChromeDriverManager().install())
#             self.driver = webdriver.Chrome(service=s)
#             print("\n\n\n\n\n>>>>>>>>>>DASHBOARD MODULES CSS PROPERTIES>>>>>>>>>>>>")

#             driver = self.driver
#             driver.maximize_window()
#             driver.get(
#                 "http://dev-contripoint.geminisolutions.com.s3-website.ap-south-1.amazonaws.com/#/dashboard")
#             button = driver.find_element(
#                 By.XPATH, '/html/body/app-root/div/div/app-login-screen/div/div/div/mat-card/div[2]/div/button')
#             button.click()
#             time.sleep(6)

#             window_handles = driver.window_handles
#             driver.switch_to.window(window_handles[1])
#             driver.find_element(
#                 By.XPATH, '//*[@id="identifierId"]').send_keys('aman.bhatia@geminisolutions.in')
#             self.ws['A2'] = 'aman.bhatia@geminisolutions.in'
#             driver.find_element(
#                 By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
#             time.sleep(3)

#             driver.find_element(
#                 By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('AmanBhatia96')
#             self.ws['B2'] = 'AmanBhatia96'
#             driver.find_element(
#                 By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
#             time.sleep(6)

#             driver.switch_to.window(window_handles[0])
#             time.sleep(6)
#             print("\n 1 - Gemini Id and Password successfully login")
#             self.ws['C2'] = 'Login'
#             self.ws['G2'] = 'login Success'

#             self.wb.save(self.filename)

#         except Exception as e:
#             print(e)
#             print("\n 1 - Gemini Id and Password  login failed")
#             self.ws['C2'] = 'Login'
#             self.ws['G2'] = 'login failed'
#             self.wb.save(self.filename)


#     def Certifications_CSSProperty(self):
#         try:
#             Certifications = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[3]/app-dash-cards/div/div[1]/div[1]/mat-card/mat-card-header/div[2]/mat-card-title')
#             print("\n Certifications:- ")

#             print("Certifications font-size: " +
#                   Certifications.value_of_css_property("font-size") + "\n  FIGMA font-size: 16px")
#             self.ws['C3'] = 'Certifications_CSSProperty'
#             self.ws['E3'] =  Certifications.value_of_css_property("font-size")
#             self.ws['F3'] = 'FIGMA font-size: 16px'
#             self.ws['G3'] = 'Pass'
#             print("\n Certifications color: " + Certifications.value_of_css_property(
#                 "color") + "\n  FIGMA Color: rgba(0, 0, 0, 1)")
#             print("\n Certifications font-family: " + Certifications.value_of_css_property(
#                 "font-family") + "\n  FIGMA font-family: Poppins")
#             print("\n Certifications text-align: " + Certifications.value_of_css_property(
#                 "text-align") + "\n FIGMA text-align: left")
#             print("\n Certifications font-style: " + Certifications.value_of_css_property(
#                 "font-style") + "\n FIGMA font-style: normal")
#             print("\n Certifications font-weight: " + Certifications.value_of_css_property(
#                 "font-weight") + "\n  FIGMA font-weight: 500")
#             print("\n Certifications line-height: " + Certifications.value_of_css_property(
#                 "line-height") + "\n  FIGMA  line-height: 24px")
#             print("\n Certifications letter-spacing: " + Certifications.value_of_css_property(
#                 "letter-spacing") + "\n FIGMA  letter-spacing: 0.03em")
#             print("\n Location : " + str(Certifications.location))
#             print("\n Size : " + str(Certifications.size))

#         except Exception as e:
#             print("\n \nERROR While getting Certifications CSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)
#             self.ws['C3'] = 'Certifications_CSSProperty'
#             self.ws['E3'] = Certifications.value_of_css_property("font-size")
#             self.ws['F3'] = 'FIGMA font-size: 16px'
#             self.ws['G3'] = 'Fail'
#             self.wb.save(self.filename)


#     def InterviewTaken_CSSProperty(self):
#         try:
#             InterviewTaken = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[3]/app-dash-cards/div/div[1]/div[2]/mat-card/mat-card-header/div[2]/mat-card-title')
#             print("\n InterviewTaken:- ")
#             print("InterviewTaken font-size: " +
#                   InterviewTaken.value_of_css_property("font-size") + "\n  FIGMA font-size: 16px")
#             print("\n InterviewTaken color: " + InterviewTaken.value_of_css_property(
#                 "color") + "\n  FIGMA Color: rgba(0, 0, 0, 1)")
#             print("\n InterviewTaken font-family: " + InterviewTaken.value_of_css_property(
#                 "font-family") + "\n  FIGMA font-family: Poppins")
#             print("\n InterviewTaken text-align: " + InterviewTaken.value_of_css_property(
#                 "text-align") + "\n FIGMA text-align: left")
#             print("\n InterviewTaken font-style: " + InterviewTaken.value_of_css_property(
#                 "font-style") + "\n FIGMA font-style: normal")
#             print("\n InterviewTaken font-weight: " + InterviewTaken.value_of_css_property(
#                 "font-weight") + "\n  FIGMA font-weight: 500")
#             print("\n InterviewTaken line-height: " + InterviewTaken.value_of_css_property(
#                 "line-height") + "\n  FIGMA  line-height: 24px")
#             print("\n Location : " + str(InterviewTaken.location))
#             print("\n Size : " + str(InterviewTaken.size))

#         except Exception as e:
#             print("\n \nERROR While getting Interview Taken CSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)
    
#     def TrainingSession_CSSProperty(self):
#         try:

#             Training_Session = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[3]/app-dash-cards/div/div[1]/div[3]/mat-card/mat-card-header/div[2]/mat-card-title')
#             print("\n Training_Session:- ")
#             print("Training_Session font-size: " +
#                   Training_Session.value_of_css_property("font-size") + "\n  FIGMA font-size: 16px")
#             print("\n Training_Session color: " + Training_Session.value_of_css_property(
#                 "color") + "\n  FIGMA Color: rgba(0, 0, 0, 1)")
#             print("\n Training_Session font-family: " + Training_Session.value_of_css_property(
#                 "font-family") + "\n  FIGMA font-family: Poppins")
#             print("\n Training_Session text-align: " + Training_Session.value_of_css_property(
#                 "text-align") + "\n FIGMA text-align: left")
#             print("\n Training_Session font-style: " + Training_Session.value_of_css_property(
#                 "font-style") + "\n FIGMA font-style: normal")
#             print("\n Training_Session font-weight: " + Training_Session.value_of_css_property(
#                 "font-weight") + "\n  FIGMA font-weight: 500")
#             print("\n Training_Session line-height: " + Training_Session.value_of_css_property(
#                 "line-height") + "\n  FIGMA  line-height: 24px")
#             print("\n Location : " + str(Training_Session.location))
#             print("\n Size : " + str(Training_Session.size))

#         except Exception as e:
#             print("\n \nERROR While getting Training and Session CSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)


#     def Mentorship_CSSProperty(self):
#         try:
#             Mentorship = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[3]/app-dash-cards/div/div[2]/div[1]/mat-card/mat-card-header/div[2]/mat-card-title')
#             print("\n Mentorship:- ")
#             print("Mentorship font-size: " +
#                   Mentorship.value_of_css_property("font-size") + "\n  FIGMA font-size: 16px")
#             print("\n Mentorship color: " + Mentorship.value_of_css_property(
#                 "color") + "\n  FIGMA Color: rgba(0, 0, 0, 1)")
#             print("\n Mentorship font-family: " + Mentorship.value_of_css_property(
#                 "font-family") + "\n  FIGMA font-family: Poppins")
#             print("\n Mentorship text-align: " + Mentorship.value_of_css_property(
#                 "text-align") + "\n FIGMA text-align: left")
#             print("\n Mentorship font-style: " + Mentorship.value_of_css_property(
#                 "font-style") + "\n FIGMA font-style: normal")
#             print("\n Mentorship font-weight: " + Mentorship.value_of_css_property(
#                 "font-weight") + "\n  FIGMA font-weight: 500")
#             print("\n Mentorship line-height: " + Mentorship.value_of_css_property(
#                 "line-height") + "\n  FIGMA  line-height: 24px")
#             print("\n Location : " + str(Mentorship.location))
#             print("\n Size : " + str(Mentorship.size))

#         except Exception as e:
#             print("\n \nERROR While getting Mentorship CSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)
    
#     def Projects_CSSProperty(self):
#         try:
#             Projects = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[3]/app-dash-cards/div/div[2]/div[2]/mat-card/mat-card-header/div[2]/mat-card-title')
#             print("\n Projects:- ")
#             print("Projects font-size: " +
#                   Projects.value_of_css_property("font-size") + "\n  FIGMA font-size: 16px")
#             print("\n Projects color: " + Projects.value_of_css_property(
#                 "color") + "\n  FIGMA Color: rgba(0, 0, 0, 1)")
#             print("\n Projects font-family: " + Projects.value_of_css_property(
#                 "font-family") + "\n  FIGMA font-family: Poppins")
#             print("\n Projects text-align: " + Projects.value_of_css_property(
#                 "text-align") + "\n FIGMA text-align: left")
#             print("\n Projects font-style: " + Projects.value_of_css_property(
#                 "font-style") + "\n FIGMA font-style: normal")
#             print("\n Projects font-weight: " + Projects.value_of_css_property(
#                 "font-weight") + "\n  FIGMA font-weight: 500")
#             print("\n Projects line-height: " + Projects.value_of_css_property(
#                 "line-height") + "\n  FIGMA  line-height: 24px")
#             print("\n Location : " + str(Projects.location))
#             print("\n Size : " + str(Projects.size))

#         except Exception as e:
#             print("\n \nERROR While getting Projects CSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)


#     def TeamBuildingActivity_CSSProperty(self):
#         try:
#             TeamBuildingActivity = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[3]/app-dash-cards/div/div[2]/div[3]/mat-card/mat-card-header/div[2]/mat-card-title')
#             print("\n TeamBuildingActivity:- ")
#             print("TeamBuildingActivity font-size: " +
#                   TeamBuildingActivity.value_of_css_property("font-size") + "\n  FIGMA font-size: 16px")
#             print("\n TeamBuildingActivity color: " + TeamBuildingActivity.value_of_css_property(
#                 "color") + "\n  FIGMA Color: rgba(0, 0, 0, 1)")
#             print("\n TeamBuildingActivity font-family: " + TeamBuildingActivity.value_of_css_property(
#                 "font-family") + "\n  FIGMA font-family: Poppins")
#             print("\n TeamBuildingActivity text-align: " + TeamBuildingActivity.value_of_css_property(
#                 "text-align") + "\n FIGMA text-align: left")
#             print("\n TeamBuildingActivity font-style: " + TeamBuildingActivity.value_of_css_property(
#                 "font-style") + "\n FIGMA font-style: normal")
#             print("\n TeamBuildingActivity font-weight: " + TeamBuildingActivity.value_of_css_property(
#                 "font-weight") + "\n  FIGMA font-weight: 500")
#             print("\n TeamBuildingActivity line-height: " + TeamBuildingActivity.value_of_css_property(
#                 "line-height") + "\n  FIGMA  line-height: 24px")
#             print("\n Location : " + str(TeamBuildingActivity.location))
#             print("\n Size : " + str(TeamBuildingActivity.size))

#         except Exception as e:
#             print("\n \nERROR While getting Team Building Activity CSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)


#     def ClientFeedback_CSSProperty(self):
#         try:

#             ClientFeedback = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[3]/app-dash-cards/div/div[3]/div[1]/mat-card/mat-card-header/div[2]/mat-card-title')
#             print("\n ClientFeedback:- ")
#             print("ClientFeedback font-size: " +
#                   ClientFeedback.value_of_css_property("font-size") + "\n  FIGMA font-size: 16px")
#             print("\n ClientFeedback color: " + ClientFeedback.value_of_css_property(
#                 "color") + "\n  FIGMA Color: rgba(0, 0, 0, 1)")
#             print("\n ClientFeedback font-family: " + ClientFeedback.value_of_css_property(
#                 "font-family") + "\n  FIGMA font-family: Poppins")
#             print("\n ClientFeedback text-align: " + ClientFeedback.value_of_css_property(
#                 "text-align") + "\n FIGMA text-align: left")
#             print("\n ClientFeedback font-style: " + ClientFeedback.value_of_css_property(
#                 "font-style") + "\n FIGMA font-style: normal")
#             print("\n ClientFeedback font-weight: " + ClientFeedback.value_of_css_property(
#                 "font-weight") + "\n  FIGMA font-weight: 500")
#             print("\n ClientFeedback line-height: " + ClientFeedback.value_of_css_property(
#                 "line-height") + "\n  FIGMA  line-height: 24px")
#             print("\n Location : " + str(ClientFeedback.location))
#             print("\n Size : " + str(ClientFeedback.size))

#         except Exception as e:
#             print("\n \nERROR While getting Client Feedback CSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)
    

    
#     def SelfDevelopmentActivity_CSSProperty(self):
#         try:
#             SelfDevelopmentActivity = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[3]/app-dash-cards/div/div[3]/div[2]/mat-card/mat-card-header/div[2]/mat-card-title')
#             print("\n SelfDevelopmentActivity:- ")
#             print("SelfDevelopmentActivity font-size: " +
#                   SelfDevelopmentActivity.value_of_css_property("font-size") + "\n  FIGMA font-size: 16px")
#             print("\n SelfDevelopmentActivity color: " + SelfDevelopmentActivity.value_of_css_property(
#                 "color") + "\n  FIGMA Color: rgba(0, 0, 0, 1)")
#             print("\n SelfDevelopmentActivity font-family: " + SelfDevelopmentActivity.value_of_css_property(
#                 "font-family") + "\n  FIGMA font-family: Poppins")
#             print("\n SelfDevelopmentActivity text-align: " + SelfDevelopmentActivity.value_of_css_property(
#                 "text-align") + "\n FIGMA text-align: left")
#             print("\n SelfDevelopmentActivity font-style: " + SelfDevelopmentActivity.value_of_css_property(
#                 "font-style") + "\n FIGMA font-style: normal")
#             print("\n SelfDevelopmentActivity font-weight: " + SelfDevelopmentActivity.value_of_css_property(
#                 "font-weight") + "\n  FIGMA font-weight: 500")
#             print("\n SelfDevelopmentActivity line-height: " + SelfDevelopmentActivity.value_of_css_property(
#                 "line-height") + "\n  FIGMA  line-height: 24px")
#             print("\n Location : " + str(SelfDevelopmentActivity.location))
#             print("\n Size : " + str(SelfDevelopmentActivity.size))
#         except Exception as e:
#             print("\n \nERROR While getting Self Development Activity CSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)
        


#     def RecentContributionsToGemini_CSSProperty(self):
#         try:
#             Recent_Contributions_To_Gemini = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[4]/app-dash-activities/div/mat-tab-group/mat-tab-header/div[2]/div/div/div[1]/div')
#             print("\n Recent_Contributions_To_Gemini:- ")
#             print("Recent_Contributions_To_Gemini font-size: " +
#                   Recent_Contributions_To_Gemini.value_of_css_property("font-size") + "\n  FIGMA font-size: 18px")
#             print("\n Recent_Contributions_To_Gemini color: " + Recent_Contributions_To_Gemini.value_of_css_property(
#                 "color") + "\n  FIGMA Color: rgba(0, 0, 0, 1)")
#             print("\n Recent_Contributions_To_Gemini font-family: " + Recent_Contributions_To_Gemini.value_of_css_property(
#                 "font-family") + "\n  FIGMA font-family: Poppins")
#             print("\n Recent_Contributions_To_Gemini text-align: " + Recent_Contributions_To_Gemini.value_of_css_property(
#                 "text-align") + "\n FIGMA text-align: Center")
#             print("\n Recent_Contributions_To_Gemini font-style: " + Recent_Contributions_To_Gemini.value_of_css_property(
#                 "font-style") + "\n FIGMA font-style: normal")
#             print("\n Recent_Contributions_To_Gemini font-weight: " + Recent_Contributions_To_Gemini.value_of_css_property(
#                 "font-weight") + "\n  FIGMA font-weight: 500")
#             print("\n Recent_Contributions_To_Gemini line-height: " + Recent_Contributions_To_Gemini.value_of_css_property(
#                 "line-height") + "\n  FIGMA  line-height: 27px")
#             print("\n Recent_Contributions_To_Gemini letter-spacing: " + Recent_Contributions_To_Gemini.value_of_css_property(
#                 "letter-spacing") + "\n FIGMA  letter-spacing: 0.02em")
#             print("\n Location : " + str(Recent_Contributions_To_Gemini.location))
#             print("\n Size : " + str(Recent_Contributions_To_Gemini.size))

#         except Exception as e:
#             print("\n \nERROR While getting Recent Contributions To Gemini CSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)


#     def MyActivity_CSSProperty(self):
#         try:
#             My_Activity = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[4]/app-dash-activities/div/mat-tab-group/mat-tab-header/div[2]/div/div/div[2]/div')
#             print("\n My_Activity:- ")
#             print("My_Activity font-size: " +
#                   My_Activity.value_of_css_property("font-size") + "\n  FIGMA font-size: 18px")
#             print("\n My_Activity color: " + My_Activity.value_of_css_property(
#                 "color") + "\n  FIGMA Color: rgba(0, 0, 0, 1)")
#             print("\n My_Activity font-family: " + My_Activity.value_of_css_property(
#                 "font-family") + "\n  FIGMA font-family: Poppins")
#             print("\n My_Activity text-align: " + My_Activity.value_of_css_property(
#                 "text-align") + "\n FIGMA text-align: Center")
#             print("\n My_Activity font-style: " + My_Activity.value_of_css_property(
#                 "font-style") + "\n FIGMA font-style: normal")
#             print("\n My_Activity font-weight: " + My_Activity.value_of_css_property(
#                 "font-weight") + "\n  FIGMA font-weight: 500")
#             print("\n My_Activity line-height: " + My_Activity.value_of_css_property(
#                 "line-height") + "\n  FIGMA  line-height: 27px")
#             print("\n My_Activity letter-spacing: " + My_Activity.value_of_css_property(
#                 "letter-spacing") + "\n FIGMA  letter-spacing: 0.02em")
#             print("\n Location : " + str(My_Activity.location))
#             print("\n Size : " + str(My_Activity.size))

#         except Exception as e:
#             print("\n \nERROR While getting MyActivity CSSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)

#     def Leaderboard_CSSProperty(self):
#         try:
#             Leaderboard = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[1]/app-dash-info-cards/div/div[2]/mat-card/div[1]/div[1]/mat-card-title')
#             print("\n Leaderboard:- ")
#             print("Leaderboard font-size: " +
#                   Leaderboard.value_of_css_property("font-size") + "\n  FIGMA font-size: 22px")
#             print("\n Leaderboard color: " + Leaderboard.value_of_css_property(
#                 "color") + "\n  FIGMA Color: rgba(255, 255, 255, 1)")
#             print("\n Leaderboard font-family: " + Leaderboard.value_of_css_property(
#                 "font-family") + "\n  FIGMA font-family: Poppins")
#             print("\n Leaderboard text-align: " + Leaderboard.value_of_css_property(
#                 "align") + "\n FIGMA text-align: Center")
#             print("\n Leaderboard font-style: " + Leaderboard.value_of_css_property(
#                 "font-style") + "\n FIGMA font-style: normal")
#             print("\n Leaderboard font-weight: " + Leaderboard.value_of_css_property(
#                 "font-weight") + "\n  FIGMA font-weight: 600")
#             print("\n Leaderboard line-height: " + Leaderboard.value_of_css_property(
#                 "line-height") + "\n  FIGMA  line-height: 33px")
#             print("\n Location : " + str(Leaderboard.location))
#             print("\n Size : " + str(Leaderboard.size))

#         except Exception as e:
#             print("\n \nERROR While getting Leaderboard CSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)

#     def LeaderboardTable_CSSProperty(self):
#         try:
#             Leaderboard_Table = self.driver.find_element(
#                 By.XPATH, '/html/body/app-root/div[3]/div/app-dash-board/div[1]/app-dash-info-cards/div/div[2]/mat-card')
#             print("\n Leaderboard_Table:- ")
#             print("Height of Table: " +
#                   Leaderboard_Table.value_of_css_property("height"))
#             print("\n width of Table: " +
#                   Leaderboard_Table.value_of_css_property("width"))
#             print("\n color: " + Leaderboard_Table.value_of_css_property("color"))
#             print("\n text-align: " +
#                   Leaderboard_Table.value_of_css_property("text-align"))
#             print("\n font-weight: " +
#                   Leaderboard_Table.value_of_css_property("font-weight"))
#             print("\n line-height: " +
#                   Leaderboard_Table.value_of_css_property("line-height"))
#             print("\n letter-spacing: " +
#                   Leaderboard_Table.value_of_css_property("letter-spacing"))
#             print("\n Location : " + str(Leaderboard_Table.location))
#             print("\n Size : " + str(Leaderboard_Table.size))

#         except Exception as e:
#             print("\n \nERROR While getting LeaderboardTable CSSProperty >>>>>>>>>>>>>>>\n\n")
#             print(e)


# if __name__ == '__main__':
#     tb = Css_Dashboard()
#     tb.setUp()
#     tb.Certifications_CSSProperty()   
#     tb.InterviewTaken_CSSProperty()
#     tb.TrainingSession_CSSProperty()
#     tb.Mentorship_CSSProperty()
#     tb.Projects_CSSProperty()
#     tb.TeamBuildingActivity_CSSProperty()
#     tb.ClientFeedback_CSSProperty()
#     tb.SelfDevelopmentActivity_CSSProperty()
#     tb.RecentContributionsToGemini_CSSProperty()
#     tb.MyActivity_CSSProperty()
#     tb.Leaderboard_CSSProperty()
#     tb.LeaderboardTable_CSSProperty()
