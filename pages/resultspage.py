from playwright.sync_api import sync_playwright

class results:
    def __init__(self,page):
        self.addTcart = lambda product: page.locator(f"(//h2[contains(@aria-label,'{product}')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//*[@aria-label='Add to cart'])[1]")