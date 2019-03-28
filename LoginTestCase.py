import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from enum import Enum
import time

class TextCases(Enum):
    InvalidLogin = 1
    InvalidEmail = 2
    EmptyEmail = 3
    EmptyPassword =4


class ormucoLogin(unittest.TestCase):

    def setUp(self):
        chrome_opt = webdriver.ChromeOptions()
        prefs = {"credentials_enable_service":False}
        prefs = {"profile.password_manager_enabled": False}
        self.driver =  webdriver.Firefox()
       
    def testvalidate_testCases(self, testcase,   email_id, email_value, password_id, password_value, button_id, result_label, url):
        """
        validate that an incorrect email returns incorrect email message

        """
        
        driver= self.driver
        driver.get(url)

        self.assertIn("Portal - hydroquebec", driver.title)
       
        time.sleep(2)# give the page 2sec to load the page 
        
        email = driver.find_element_by_id(email_id)
        email.send_keys(email_value)

        password = driver.find_element_by_id(password_id)
        password. send_keys(password_value)

        submit_button = driver.find_element_by_css_selector("button[type='"+button_id+"']")
        submit_button.click()
    
        print("Your test case is: {0}".format(TextCases(testcase)))
        lblTxt=  driver.find_element_by_css_selector("span[class='" + result_label+ "']")
        htmlVal = lblTxt.get_attribute("innerHTML")
        if TextCases.InvalidLogin == testcase:

        
            print(htmlVal)
            result = self.assertTrue(htmlVal, "The email or password is incorrect")
            print(result)
          
        elif TextCases.EmptyPassword == testcase:
            
            result = self.assertFalse(htmlVal, "Password not supplied")
            print(result)

        elif TextCases.InvalidEmail ==testcase:
            result =self.assertFalse(htmlVal, "Invalid email")
            print(result)

        elif TextCases.EmptyEmail == testcase:
            result=self.assertFalse(htmlVal, "Email not supplies")
            print(result)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ ==  "__main__":
    self =  ormucoLogin()
    self.driver =  webdriver.Firefox()

    #invalid login details
    #ormucoLogin.testvalidate_testCases(self,TextCases.InvalidLogin,"username","harkin.tune@gmail.com", "password", "pass@3eee", "submit", "warning", "https://uat.ormuco.com/login" )

    #invalid login details
    ormucoLogin.testvalidate_testCases(self,TextCases.EmptyEmail,"username","", "password", "pass@3eee", "submit", "warning", "https://uat.ormuco.com/login")

    #invalid email
    #ormucoLogin.testvalidate_testCases(self,TextCases.InvalidEmail,"username","harkin.tune.com", "password", "pass@3eee", "submit", "warning", "https://uat.ormuco.com/login")
    
    #Empty password
    #ormucoLogin.testvalidate_testCases(self,TextCases.EmptyPassword,"username","harkin.tune@gmail.com", "password", "pass@3eee", "submit", "warning", "https://uat.ormuco.com/login")
    
    
  

    



