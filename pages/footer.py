from selene import browser, be, command


class Footer:
    FOOTER_QR = "[data-testid='footer_qrCode']"
    SUPPORT_BUTTON = "[data-testid='support_button_id']"

    def scroll_to_footer(self):
        browser.element(self.FOOTER_QR).perform(command.js.scroll_into_view)
        return self

    def should_have_qr_code(self):
        browser.element(self.FOOTER_QR).should(be.visible)
        return self

    def should_have_support_button(self):
        browser.element(self.SUPPORT_BUTTON).should(be.visible).should(be.clickable)
        return self
