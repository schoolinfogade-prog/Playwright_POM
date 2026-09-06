from playwright.sync_api import expect

class homepage:
    
    def __init__(self,page):
        accbtn=page.locator("[aria-controls='nav-line-1-container'']")
    
    def ckickonacct(self):
        self.acctbtn.click()
        
    def validate(self):
        expect(self.acctbtn).to_be_visible()