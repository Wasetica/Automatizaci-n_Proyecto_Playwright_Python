import pytest
from pages.login_page import LoginPage
from utils.test_data import TestData

@pytest.mark.smoke
def test_login_exitoso(page):
    """Caso de prueba exitoso"""

    login = LoginPage(page)
    login.navigate(TestData.BASE_URL)

    login.login(TestData.USERNAME, TestData.PASSWORD)

    assert login.is_login_successful(), "❌ El login exitoso falló"
    print("✅ Login exitoso validado correctamente")


@pytest.mark.regression
def test_login_fallido(page):
    """Caso fallido con espera de tiempo"""

    login = LoginPage(page)
    login.navigate(TestData.BASE_URL)

    login.login("usuario_incorrecto", "clave_mala")

    # Espera 3 segundos para que cargue el mensaje de error
    page.wait_for_timeout(3000)

    assert not login.is_login_successful(), "❌ El login fallido debería fallar y no lo hizo"
    print("✅ Login fallido detectado correctamente")
