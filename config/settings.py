import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def _get_bool(name: str, default: bool = False) -> bool:
    val = os.getenv(name)
    if val is None:
        return default
    return val.strip().lower() in {"1", "true", "yes", "y", "on"}


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://www.rustore.ru")

    browser: str = os.getenv("BROWSER", "chrome")

    browser_version: str = os.getenv("BROWSER_VERSION", "128.0")

    browser_size: str = os.getenv("BROWSER_SIZE", "1920x1080")
    headless: bool = _get_bool("HEADLESS", True)
    fullscreen: bool = _get_bool("FULLSCREEN", False)

    timeout: float = float(os.getenv("TIMEOUT", "5"))

    is_remote: bool = _get_bool("IS_REMOTE", False)
    remote_url: str = os.getenv("REMOTE_URL", "")

    enable_vnc: bool = _get_bool("SELENOID_ENABLE_VNC", True)
    enable_video: bool = _get_bool("SELENOID_ENABLE_VIDEO", True)

    session_name: str = os.getenv("SELENOID_SESSION_NAME", "rustore-ui-tests")
    video_name: str = os.getenv("SELENOID_VIDEO_NAME", "video.mp4")

    selenoid_ui: str = os.getenv("SELENOID_UI", "")


settings = Settings()
