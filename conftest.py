import pytest
from selene.support.shared import config, browser


@pytest.fixture(scope='module')
def browser_():
    config.browser_name = "chrome"
    yield browser
    browser.quit()
