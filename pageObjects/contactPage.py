from basePage import basePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from basePage import basePage

class contactPage:
    def __init__(self, driver):
        self.driver= driver
    
    def click_Submit(self):
        buttonSubmit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-contact')))
        buttonSubmit.click()

    ### Functions to fill out the contact form ###
    # fill out forename cell
    def set_forename(self, forename:str):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.ID, 'forename'))).send_keys(forename)
        return self 
    
    # fill out surname cell 
    def set_surname(self, surname:str):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.ID, 'surname'))).send_keys(surname)
        return self 
    
    # fill out email cell 
    def set_email(self, email:str):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.ID, 'email'))).send_keys(email)
        return self 
    # fill out telephone cell    
    def set_telephone(self, phone:str):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.ID, 'telephone'))).send_keys(phone)
        return self 
    
    #fill out message cell 
    def set_message(self, message:str):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.ID, 'message'))).send_keys(message)
        return self 

    # Functions relating to the error messages when empty form is submitted 
    # get error text #
    def get_error_text(self, locator_type, locator_value, istest = False):
        target = self.driver.find_elements(locator_type, locator_value)
        if not target: 
            return ""
        if istest: 
            return target[0].text
        return target[0].text

    # get the forname error 
    def get_forename_error(self) -> str: 
        return contactPage.get_error_text(self, By.ID, 'forename-err')
  
    # get the email error 
    def get_email_error(self) -> str: 
        return contactPage.get_error_text(self, By.ID, 'email-err')
    # get the message error 
    def get_message_error(self) -> str: 
        return contactPage.get_error_text(self, By.ID, 'message-err')
        
    ## function to provide submitted form success message 
    def submit_success(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'strong.ng-binding')))   
        return self.driver.find_element(By.CSS_SELECTOR, 'strong.ng-binding').text