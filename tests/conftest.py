import allure
import pytest
from selene import browser

from config.settings import settings
from core import attach
from core.browser import configure_browser


def pytest_addoption(parser):
    parser.addoption(
        "--browser_version",
        action="store",
        default=None,
        help="Browser version override (e.g. 128.0)",
    )


@pytest.fixture(autouse=True)
def ui_driver(request):
    browser_version = request.config.getoption("--browser_version")

    if browser_version:
        object.__setattr__(settings, "browser_version", browser_version)

    configure_browser()
    yield

    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        with allure.step("Приложить артефакты"):
            attach.screenshot()
            attach.page_source()
            attach.browser_logs()
            attach.video()

    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep
