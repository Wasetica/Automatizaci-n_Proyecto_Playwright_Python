from dotenv import load_dotenv
import os

load_dotenv()

class TestData:
    """Variables globales de datos de prueba."""

    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    BASE_URL = os.getenv('BASE_URL')
    HEADLESS = os.getenv('HEADLESS', 'true')
    ARTIFACTS_DIR = os.getenv('ARTIFACTS_DIR', 'artifacts')
