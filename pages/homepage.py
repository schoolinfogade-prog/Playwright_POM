import allure
from playwright.sync_api import expect

class homepage:
    
    def __init__(self,page):
        self.acctbtn=page.locator('[aria-controls="nav-flyout-accountList"]')
        
    @allure.step("clickonacct")
    def clickonacct(self):
        self.acctbtn.click()
        
    @allure.step("validate")    
    def validate(self):
        expect(self.acctbtn).to_be_visible()