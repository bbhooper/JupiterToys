from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from basePage import basePage 

class storePage(basePage):
    def __init__(self, driver): 
        self.driver = driver

    ## Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear
    # Stuffed Frog button
    def buy_Frog_Btn(self, count):
        Frog_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#product-2 > div:nth-child(1) > p:nth-child(3) > a:nth-child(2)')))
        while count >0:
            Frog_btn.click()
            count -= 1

    # Fluffy Bunny button
    def buy_Bunny_Btn(self, count):
        Bunny_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#product-4 > div:nth-child(1) > p:nth-child(3) > a:nth-child(2)')))
        while count >0:
            Bunny_btn.click()
            count -= 1

    # Valentine Bear button 
    def buy_VBear_btn(self, count):
        Bear_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#product-7 > div:nth-child(1) > p:nth-child(3) > a:nth-child(2)')))
        while count >0:
            Bear_btn.click()
            count -= 1
