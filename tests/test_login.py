from pages.login_page import LoginPage
from utils.test_data import TestData

def test_login_success(page):
    login = LoginPage(page)

    login.goto(TestData.BASE_URL)
    login.login(TestData.USERNAME, TestData.PASSWORD)

    login.validate_success()


def test_login_incorrect_password(page):
    login = LoginPage(page)

    login.goto(TestData.BASE_URL)
    login.login("student", "wrong123")

    login.validate_error("Your password is invalid!")


def test_login_incorrect_username(page):
    login = LoginPage(page)

    login.goto(TestData.BASE_URL)
    login.login("wrongUser", "Password123")

    login.validate_error("Your username is invalid!")
