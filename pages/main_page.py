from selene import browser, have, be


class MainPage:
    LOGO = "[data-testid='header_logo']"
    DOWNLOAD_BUTTON = "[data-testid='download_rustore_button']"
    SEARCH_BUTTON = "[data-testid='header_search_button']"

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
