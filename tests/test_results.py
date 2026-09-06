from playwright.sync_api import sync_playwright, expect, Page
import re

def test_validateresultspage(page:Page,navigateToPage):
    page.locator("#twotabsearchtextbox").fill("iphone")
    page.locator("#nav-search-submit-button").click(timeout=5000)
    page.locator("//h2[text()='Results']").wait_for(state="visible")
    expect(page).to_have_title(re.compile("Amazon"))
    