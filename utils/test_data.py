from dotenv import load_dotenv
import os

load_dotenv()

class TestData:
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    BASE_URL = os.getenv("BASE_URL")
