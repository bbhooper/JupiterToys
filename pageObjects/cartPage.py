from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

class cartPage:
    def __init__(self, driver):
        self.driver = driver  

    # extract table contents 
        # it will return the cells which we can then grab the index for 
    def get_table_contents(self):
        # waiting for table to fully load in before trying to locate it 
        table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/form/table'))
        )
        # self.driver.implicitly_wait(2)
        # table = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/form/table')
        body = table.find_element(By.TAG_NAME, 'tbody')
        cells = body.find_elements(By.TAG_NAME, 'td')
        return cells

    # this will return the text of specific cell n 
    def get_cell_text(self, n): 
        cells = cartPage.get_table_contents(self)
        return cells[n].text
    
    # convert the text to float by removing the '$' or whatever characters
    def text_to_Float(self, cell, chr_to_remove, remove_to):
        cell = cell.replace(chr_to_remove, remove_to)
        cell = float(cell)
        return cell

    # get the footer cell that contains the total 
    def get_total(self): 
        return self.driver.find_element(By.XPATH, '/html/body/div[2]/div/form/table/tfoot/tr[1]/td/strong').text

        