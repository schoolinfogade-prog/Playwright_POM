from playwright.sync_api import sync_playwright, expect, Page
import re, pytest
from pages.homepage import homepage

@pytest.mark.test4
def test_validatecomponents(page: Page,navigateToPage):
        homepageobj=homepage(page) 
       # homepageobj.clickonacct()
        homepageobj.validate()
        expect(page).to_have_title(re.compile("Amazon"))
        expect(page).to_have_url("https://www.amazon.com/")
        
@pytest.mark.test4
def test_validateheaders(page:Page, navigateToPage):
        expect(page.locator("#twotabsearchtextbox")).to_be_visible()
        
# add=lambda a,b:a+b

# print(add(3,5))    
    
@pytest.mark.test4
def test_validatecomponentsneg(page: Page,navigateToPage):
        homepageobj=homepage(page) 
       # homepageobj.clickonacct()
        homepageobj.validate()
        expect(page).to_have_title(re.compile("Amazon"))
        expect(page).to_have_url("https://www.amazon.com/")
        
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

       
        
