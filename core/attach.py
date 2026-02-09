import json
from urllib.parse import urlsplit, urlunsplit

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

    if not settings.selenoid_ui and not settings.remote_url:
        allure.attach(
            f"session_id={session_id}, SELENOID_UI and REMOTE_URL are empty",
            name="video_error",
            attachment_type=AttachmentType.TEXT,
            extension=".txt",
        )
        return

    base = settings.selenoid_ui.rstrip("/")
    userinfo = ""

    if settings.remote_url:
        remote = urlsplit(settings.remote_url)
        host = remote.hostname
        if not base and host:
            scheme = remote.scheme or "https"
            base = f"{scheme}://{host}"
            if remote.port:
                base += f":{remote.port}"

        if remote.username:
            userinfo = remote.username
            if remote.password:
                userinfo += f":{remote.password}"

    if not base:
        allure.attach(
            f"session_id={session_id}, cannot resolve video host",
            name="video_error",
            attachment_type=AttachmentType.TEXT,
            extension=".txt",
        )
        return

    public_video_url = f"{base}/video/{session_id}.mp4"
    video_url = public_video_url
    if userinfo:
        parts = urlsplit(public_video_url)
        video_url = urlunsplit(
            (
                parts.scheme,
                f"{userinfo}@{parts.netloc}",
                parts.path,
                parts.query,
                parts.fragment,
            )
        )

    html = (
        "<html><body><video width='100%' height='100%' controls autoplay>"
        f"<source src='{video_url}' type='video/mp4'></video>"
        "</body></html>"
    )
    allure.attach(html, name=f"{name}_{session_id}", attachment_type=AttachmentType.HTML, extension=".html")
