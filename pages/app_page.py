from selene import browser, have, be


class AppPage:
    APP_NAME = "[data-testid='name']"
    MAIN_INFO = "[data-testid='main-info']"

    INSTALL_BUTTON = "[data-testid='deepLinkButton']"
    QR_BUTTON = "[data-testid='qr-button']"

    def open(self, app_path: str):
        browser.open(app_path)
        return self

    def should_be_loaded(self):
        browser.element(self.MAIN_INFO).should(be.visible)
        browser.element(self.APP_NAME).should(be.visible)
        return self

    def should_have_title(self, expected_title: str):
        browser.should(have.title(expected_title))
        return self

    def should_have_name(self, expected_name: str):
        browser.element(self.APP_NAME).should(have.exact_text(expected_name))
        return self

    def should_have_action_buttons(self):
        browser.element(self.INSTALL_BUTTON).should(be.visible).should(be.clickable)
        browser.element(self.QR_BUTTON).should(be.visible)
        return self
