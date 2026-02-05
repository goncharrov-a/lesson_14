import json

import allure
from allure_commons.types import AttachmentType
from selene import browser

from config.settings import settings


def screenshot(name: str = "screenshot") -> None:
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        png,
        name=name,
        attachment_type=AttachmentType.PNG,
        extension=".png",
    )


def page_source(name: str = "page_source") -> None:
    allure.attach(
        browser.driver.page_source,
        name=name,
        attachment_type=AttachmentType.HTML,
        extension=".html",
    )


def browser_logs(name: str = "browser_logs") -> None:
    try:
        resp = browser.driver.execute("getLog", {"type": "browser"})
        logs = resp.get("value", resp)

        text = "\n".join(json.dumps(e, ensure_ascii=False) for e in logs)

        allure.attach(
            text if text else "Browser logs are empty",
            name=name,
            attachment_type=AttachmentType.TEXT,
            extension=".log",
        )

    except Exception as e:
        allure.attach(
            str(e),
            name="browser_logs_error",
            attachment_type=AttachmentType.TEXT,
            extension=".log",
        )


def video(name: str = "video") -> None:
    session_id = browser.driver.session_id

    if not settings.selenoid_ui:
        allure.attach(
            f"session_id={session_id}, SELENOID_UI is empty",
            name="video_error",
            attachment_type=AttachmentType.TEXT,
            extension=".txt",
        )
        return

    video_url = f"{settings.selenoid_ui.rstrip('/')}/video/{session_id}.mp4"

    allure.attach(
        video_url,
        name="video_url",
        attachment_type=AttachmentType.TEXT,
        extension=".txt",
    )

    html = (
        "<html><body><video width='100%' height='100%' controls autoplay>"
        f"<source src='{video_url}' type='video/mp4'></video>"
        "</body></html>"
    )
    allure.attach(html, name=f"{name}_{session_id}", attachment_type=AttachmentType.HTML, extension=".html")
