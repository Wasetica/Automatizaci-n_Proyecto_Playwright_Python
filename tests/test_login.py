import pytest
from pages.login_page import LoginPage
from utils.test_data import TestData


@pytest.mark.smoke
def test_login(page):
    """Caso de prueba: validar login exitoso"""

    login = LoginPage(page)

    # Navegar a la página del login
    page.goto(TestData.BASE_URL)

    # Realizar login
    login.login(TestData.USERNAME, TestData.PASSWORD)

    # Validar login exitoso
    assert login.is_login_successful(), "El login no fue exitoso"

