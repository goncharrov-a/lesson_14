from selene import browser, have, be
from selene.core.exceptions import TimeoutException


class MainPage:
    LOGO = "[data-testid='header_logo']"
    DOWNLOAD_BUTTON = "[data-testid='download_rustore_button']"
    SEARCH_BUTTON = "[data-testid='header_search_button']"

    HEADER_LINKS = "[data-testid='header_routeLink']"

    def open(self):
        browser.open("/")
        return self

    def open_search(self):
        browser.element(self.SEARCH_BUTTON).should(be.visible).should(be.clickable).click()
        return self

    def go_to_instruction(self):
        browser.element(self.DOWNLOAD_BUTTON).should(be.visible).should(be.clickable).click()
        return self

    def should_have_correct_title(self):
        browser.should(
            have.title(
                "RuStore официальный магазин приложений для Android - "
                "Гарантированно безопасные приложения"
            )
        )
        return self

    def should_have_clickable_logo(self):
        browser.element(self.LOGO).should(be.visible).should(be.clickable)
        return self

    def should_have_download_button(self):
        browser.element(self.DOWNLOAD_BUTTON).should(be.visible).should(be.clickable)
        return self

    def header_link(self, text: str):
        return browser.all(self.HEADER_LINKS).element_by(have.exact_text(text))

    def should_have_clickable_header_link(self, text: str):
        try:
            self.header_link(text).should(be.visible).should(be.clickable)
        except TimeoutException as e:
            # Обработка ошибки для примера
            raise AssertionError(f"Пункт меню хедера '{text}' не найден/не кликабелен") from e
        return self
