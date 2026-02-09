import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def _get_bool(name: str, default: bool = False) -> bool:
    val = os.getenv(name)
    if val is None:
        return default
    return val.strip().lower() in {"1", "true", "yes", "y", "on"}


def _build_remote_url() -> str:
    explicit = os.getenv("REMOTE_URL", "").strip()
    if explicit:
        return explicit

    login = os.getenv("SELENOID_LOGIN", "").strip()
    password = os.getenv("SELENOID_PASS", "").strip()
    host = os.getenv("SELENOID_URL", "").strip()
    if login and password and host:
        return f"https://{login}:{password}@{host}/wd/hub"

    return ""


def _build_selenoid_ui() -> str:
    explicit = os.getenv("SELENOID_UI", "").strip()
    if explicit:
        return explicit

    host = os.getenv("SELENOID_URL", "").strip()
    if host:
        return f"https://{host}"

    return ""


def _build_is_remote(remote_url: str) -> bool:
    if os.getenv("IS_REMOTE") is not None:
        return _get_bool("IS_REMOTE", False)
    return bool(remote_url)


_REMOTE_URL = _build_remote_url()
_SELENOID_UI = _build_selenoid_ui()
_IS_REMOTE = _build_is_remote(_REMOTE_URL)


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://www.rustore.ru")
    browser: str = os.getenv("BROWSER", "chrome")
    browser_version: str = os.getenv("BROWSER_VERSION", "128.0")

    browser_size: str = os.getenv("BROWSER_SIZE", "1920x1080")
    headless: bool = _get_bool("HEADLESS", True)
    fullscreen: bool = _get_bool("FULLSCREEN", True)
    timeout: float = float(os.getenv("TIMEOUT", "5"))

    is_remote: bool = _IS_REMOTE
    remote_url: str = _REMOTE_URL

    enable_vnc: bool = _get_bool("SELENOID_ENABLE_VNC", True)
    enable_video: bool = _get_bool("SELENOID_ENABLE_VIDEO", True)

    session_name: str = os.getenv("SELENOID_SESSION_NAME", "ui-tests")
    video_name: str = os.getenv("SELENOID_VIDEO_NAME", "video.mp4")

    selenoid_ui: str = _SELENOID_UI


settings = Settings()
