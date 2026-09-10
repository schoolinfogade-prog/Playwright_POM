from playwright.sync_api import sync_playwright, expect
import re
import pytest

# @pytest.fixture()
# def validatecomponents():
#     with sync_playwright() as p:
#         browser=p.chromium.launch(headless=False)
#         context=browser.new_context()
#         page=context.new_page()
#         yield


@pytest.fixture()
def navigateToPage(page):
    page.goto("https://www.amazon.com/") 