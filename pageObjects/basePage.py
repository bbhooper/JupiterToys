from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


class basePage():
    def __init__(self, driver):
        self.driver = driver
    
    def load(self):
        self.driver.get('https://jupiter.cloud.planittesting.com/')
        self.driver.maximize_window()

    def click_ContactPage(self):
        # navigate to the contact us page
        buttonContact = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#nav-contact')))
        buttonContact.click()
    
    def click_StorePage(self):
        # navigate to the contact us page 
        buttonContact = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#nav-shop')))
        buttonContact.click()
    
    def click_CartPage(self): 
        # navigate to the contact us page 
        buttonContact = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'nav-cart')))
        buttonContact.click()
