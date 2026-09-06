from playwright.sync_api import sync_playwright, expect, Page
import re
from pages.homepage import homepage

def test_validatecomponents(page: Page,navigateToPage):
        homepageobj=homepage() 
        homepageobj.ckickonacct()
        homepageobj.validate()
        expect(page).to_have_title(re.compile("Amazon"))
        expect(page).to_have_url("https://www.amazon.com/")
        
def test_validateheaders(page:Page, naigateToPage):
        expect(page.locator("#twotabsearchtextbox")).to_be_visible()
            
       
        
