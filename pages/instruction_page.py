from selene import browser, be, have


class InstructionPage:
    DOWNLOAD_BTN_WRAPPER = "[data-testid='download_button']"
    DOWNLOAD_LINK = "[data-testid='download_link']"

    def should_be_opened(self):
        browser.should(have.url_containing("/instruction"))
        return self

    def should_have_correct_title(self):
        browser.should(
            have.title(
                "Скачать RuStore с официального сайта | Инструкция по скачиванию и установке магазина приложений Рустор"
            )
        )
        return self

    def should_have_download_button(self):
        browser.element(self.DOWNLOAD_BTN_WRAPPER).should(be.visible)
        browser.element(self.DOWNLOAD_LINK).should(be.visible).should(be.clickable)
        return self

    def should_have_download_link_attrs(self):
        link = browser.element(self.DOWNLOAD_LINK)
        link.should(have.attribute("href").value_containing("/download"))
        link.should(have.attribute("target").value("_blank"))
        return self
