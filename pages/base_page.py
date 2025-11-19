from playwright.sync_api import Page, expect


class BasePage:
def __init__(self, page: Page):
self.page = page


def goto(self, url: str):
self.page.goto(url)


def fill(self, locator: str, value: str):
self.page.locator(locator).fill(value)


def click(self, locator: str):
self.page.locator(locator).click()


def should_have_text(self, locator: str, text: str):
expect(self.page.locator(locator)).to_have_text(text)


def wait_for_visible(self, locator: str, timeout: int = 5000):
self.page.locator(locator).wait_for(state='visible', timeout=timeout)


def screenshot(self, path: str = None):
return self.page.screenshot(path=path, full_page=True)