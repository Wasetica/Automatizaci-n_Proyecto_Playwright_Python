from playwright.sync_api import Page

class LoginPage:
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#submit"
    SUCCESS_H1 = "//h1[contains(text(),'Logged In Successfully')]"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.page.is_visible(self.SUCCESS_H1)
