from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#submit")
        self.success_header = page.locator("h1")
        self.logout_button = page.locator("text=Log out")

    def navigate(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def is_login_successful(self):
        # Espera explícita por la nueva página
        self.page.wait_for_url("**/logged-in-successfully/", timeout=5000)

        # Validamos encabezado
        header_ok = self.success_header.is_visible() and \
                    self.success_header.inner_text().strip() == "Logged In Successfully"

        # Validamos que exista el botón de logout
        logout_ok = self.logout_button.is_visible()

        return header_ok and logout_ok
