from __future__ import annotations

from selene import browser
from selenium.webdriver import ChromeOptions

from config.settings import settings


def configure_browser() -> None:
    browser.config.base_url = settings.base_url
    browser.config.timeout = settings.timeout

    options = ChromeOptions()

    if settings.headless:
        options.add_argument("--headless=new")

    if settings.fullscreen:
        options.add_argument("--start-maximized")
    else:
        browser.config.window_size = settings.browser_size

    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    options.set_capability("browserName", settings.browser)
    if settings.browser_version:
        options.set_capability("browserVersion", settings.browser_version)

    if settings.is_remote:
        browser.config.driver_remote_url = settings.remote_url

        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": settings.enable_vnc,
                "enableVideo": settings.enable_video,
                "name": settings.session_name,
                "videoName": settings.video_name,
            },
        )

    browser.config.driver_options = options


def open_base_url() -> None:
    browser.open("/")
