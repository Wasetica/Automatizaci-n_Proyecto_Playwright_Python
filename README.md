🧪 Proyecto de Automatización QA con Playwright + Pytest

Automatización de pruebas end-to-end utilizando Playwright en Python, arquitectura Page Object Model (POM), reportes en Allure y pytest-html, junto con trazas automáticas en caso de fallo.

📁 Estructura del Proyecto
Proyecto Play Python/
│
├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── artifacts/
│   └── (se generan trazas, capturas y videos automáticamente)
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

⚙️ Instalación del entorno
1️⃣ Crear entorno virtual
python -m venv venv

2️⃣ Activar entorno
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Instalar navegadores de Playwright
playwright install

🚀 Ejecución de pruebas
▶ Ejecutar todas las pruebas
pytest -v

▶ Ejecutar solo pruebas con marca smoke
pytest -m smoke

📊 Reportes
📌 Generar reporte HTML
pytest --html=report.html --self-contained-html


El archivo se genera en la raíz del proyecto.

🎯 Reportes Allure (Opcional)
1️⃣ Ejecutar pruebas generando resultados de Allure
pytest --alluredir=allure-results

2️⃣ Ver el reporte
allure serve allure-results

🧱 Arquitectura Page Object Model (POM)

Ejemplo del Page Object:

class LoginPage:

    def __init__(self, page):
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
        self.page.wait_for_url("**/logged-in-successfully/")
        return self.success_header.inner_text().strip() == "Logged In Successfully"

🧪 Ejemplo de caso de prueba
@pytest.mark.smoke
def test_login_exitoso(page):
    login = LoginPage(page)
    login.navigate(TestData.BASE_URL)
    login.login(TestData.USERNAME, TestData.PASSWORD)
    assert login.is_login_successful(), "❌ El login exitoso falló"

📁 Trazas y evidencias

Automáticamente se guardan en:

artifacts/test_name/
- trace.zip
- screenshot.png


Esto ocurre gracias a la configuración en conftest.py.

🔧 Configuración Pytest

Archivo pytest.ini:

[pytest]
testpaths = tests
addopts = --disable-warnings -q
markers =
    smoke: Pruebas críticas y rápidas

🧩 Requerimientos utilizados

Archivo requirements.txt:

pytest
pytest-html
pytest-metadata
playwright
allure-pytest

👨‍💻 Autor

Sebastián Pérez (KSM)
QA Engineer – Automatización, pruebas funcionales y gestión de defectos.

📬 Contacto
