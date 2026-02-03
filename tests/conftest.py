import allure
import pytest
from selene import browser

from core import attach
from core.browser import configure_browser


@pytest.fixture(autouse=True)
def ui_driver(request):
    configure_browser()
    yield
    # attach при fail
    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        with allure.step("Attach artifacts"):
            attach.screenshot()
            attach.page_source()
            attach.browser_logs()
            attach.video_link()

    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep
