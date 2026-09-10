from playwright.sync_api import sync_playwright, expect, Page
import re

def test_validateresultspage(page:Page,navigateToPage):
    page.locator("#twotabsearchtextbox").fill("iphone")
    page.locator("#nav-search-submit-button").click(timeout=5000)
    page.locator("//h2[text()='Results']").wait_for(state="visible")
    expect(page).to_have_title(re.compile("Amazon"))

def test_iphone_results_are_related(page: Page, navigateToPage):
    page.locator("#twotabsearchtextbox").fill("iphone")
    page.locator("#nav-search-submit-button").click(timeout=5000)

    product_titles = page.locator("div[data-component-type='s-search-result'] h2")
    expect(product_titles).not_to_have_count(0)

    titles = [title.inner_text().lower() for title in product_titles.all()]
    assert titles, "No search results displayed on the results page"
    assert all("iphone" in title for title in titles), (
        "Expected all displayed products to be iPhone related, but found: "
        + str(titles[:5])
    )
