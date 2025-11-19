import pytest
from playwright.sync_api import sync_playwright
from utils.test_data import TestData
from utils.logger import get_logger

logger = get_logger("browser_fixture")


@pytest.fixture(scope="function")
def browser_context():
    """Crea un browser context visible si HEADLESS=false."""

    with sync_playwright() as p:

        headless = TestData.HEADLESS.lower() == "true"

        browser = p.chromium.launch(
            headless=headless,
            args=[
                "--disable-gpu",
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            locale="es-ES",
            record_video_dir="videos/"
        )

        logger.info("Browser context iniciado (headed=%s)", not headless)

        yield context

        logger.info("Cerrando browser context…")
        context.close()
        browser.close()
