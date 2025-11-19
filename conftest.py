from fixtures.browser_fixture import browser_context
import pytest

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    return page
