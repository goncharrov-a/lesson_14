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
            for name, fn in (
                    ("screenshot", attach.screenshot),
                    ("page_source", attach.page_source),
                    ("browser_logs", attach.browser_logs),
                    ("video", attach.video),
            ):
                try:
                    fn()
                except Exception as e:
                    allure.attach(
                        f"{name} attach failed: {e}",
                        name=f"{name}_attach_error",
                        attachment_type=allure.attachment_type.TEXT,
                        extension=".txt",
                    )

    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep
