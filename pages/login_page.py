from pages.base_page import BasePage

class LoginPage(BasePage):

    USER_FIELD = "#username"
    PASS_FIELD = "#password"
    LOGIN_BTN = "#submit"
    SUCCESS_MESSAGE = "//h1[contains(text(),'Logged In Successfully')]"
    ERROR_MESSAGE = "#error"

    def login(self, username: str, password: str):
        self.fill(self.USER_FIELD, username)
        self.fill(self.PASS_FIELD, password)
        self.click(self.LOGIN_BTN)

    def validate_success(self):
        self.wait_for(self.SUCCESS_MESSAGE)
        self.should_have_text(self.SUCCESS_MESSAGE, "Logged In Successfully")

    def validate_error(self, expected_msg: str):
        self.wait_for(self.ERROR_MESSAGE)
        self.should_have_text(self.ERROR_MESSAGE, expected_msg)
