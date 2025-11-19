import os
import shutil
from pathlib import Path
import pytest
import allure

from utils.test_data import TestData
from fixtures.browser_fixture import browser_context
from utils.logger import get_logger


ARTIFACTS_DIR = Path(os.getenv('ARTIFACTS_DIR', 'artifacts'))
ARTIFACTS_DIR.mkdir(exist_ok=True)
logger = get_logger('conftest')


@pytest.fixture
def page(browser_context, request):
    """Crea una nueva página por test. Se encarga de arrancar/stop tracing y crear carpeta de artefactos por test."""

    test_name = request.node.name
    test_dir = ARTIFACTS_DIR / test_name

    # reset carpeta por test
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir(parents=True)

    # iniciar tracing
    browser_context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = browser_context.new_page()
    yield page

    # detener tracing y guardar
    trace_path = str(test_dir / f"trace_{test_name}.zip")
    try:
        browser_context.tracing.stop(path=trace_path)
        logger.info(f"Saved trace to {trace_path}")
    except Exception as e:
        logger.exception("Could not save trace: %s", e)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para adjuntar capturas, videos, trace y logs a Allure cuando falle el test."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        test_name = item.name
        test_dir = ARTIFACTS_DIR / test_name

        # Adjuntar artefactos del directorio
        if test_dir.exists():
            for file in test_dir.iterdir():
                try:
                    with open(file, 'rb') as f:
                        allure.attach(
                            f.read(),
                            name=file.name,
                            attachment_type=allure.attachment_type.BINARY
                        )
                except Exception:
                    logger.exception("Adjuntar artefacto %s falló", file)

        # Si hay fixture page, tomar screenshot final
        page_fixture = item.funcargs.get('page') if 'page' in getattr(item, 'funcargs', {}) else None
        if page_fixture:
            try:
                screenshot = page_fixture.screenshot(full_page=True)
                allure.attach(
                    screenshot,
                    name=f"screenshot_{test_name}.png",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                logger.exception("No se pudo tomar screenshot final")

    return rep
