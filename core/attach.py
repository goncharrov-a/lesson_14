import json

import allure
from selene import browser


def screenshot(name: str = "screenshot") -> None:
    png = browser.driver.get_screenshot_as_png()
    allure.attach(png, name=name, attachment_type=allure.attachment_type.PNG)


def page_source(name: str = "page_source") -> None:
    allure.attach(browser.driver.page_source, name=name, attachment_type=allure.attachment_type.HTML)


def browser_logs(name: str = "browser_logs") -> None:
    try:
        logs = browser.driver.get_log("browser")
        allure.attach(
            json.dumps(logs, ensure_ascii=False, indent=2),
            name=name,
            attachment_type=allure.attachment_type.JSON,
        )
    except Exception as e:
        allure.attach(str(e), name="browser_logs_error", attachment_type=allure.attachment_type.TEXT)


def video_link(name: str = "video") -> None:
    from config.settings import settings

    try:
        session_id = browser.driver.session_id
        if settings.selenoid_ui:
            url = f"{settings.selenoid_ui.rstrip('/')}/video/{settings.video_name}"
            allure.attach(url, name=f"{name} (session {session_id})", attachment_type=allure.attachment_type.URI_LIST)
        else:
            allure.attach(
                f"session_id={session_id}, set SELENOID_UI to attach link",
                name=name,
                attachment_type=allure.attachment_type.TEXT,
            )
    except Exception as e:
        allure.attach(str(e), name="video_error", attachment_type=allure.attachment_type.TEXT)
