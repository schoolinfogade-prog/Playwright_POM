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
        
#         1st time workflow
#         git init 
#         git add .
#         git commit -m "first commit"
#         git branch -M main
#         git remote add origin <GitHub URL>
#         git push -u origin main
        
#         2nd time workflow 
#         git remote add origin <GitHub URL>
#         git branch -M main
#         git push -u origin main

       
        
