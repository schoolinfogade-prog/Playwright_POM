from playwright.sync_api import sync_playwright, expect, Page
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
def navigateToPage(page: Page):
    page.goto(
        "https://www.amazon.com/",
        wait_until="domcontentloaded"
    )

    continue_button = page.get_by_role(
        "button",
        name="Continue shopping"
    )

    if continue_button.count() > 0:
        continue_button.first.click()

    return page