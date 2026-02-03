from selene import browser, have, be


class SearchResultsPage:
    RESULTS_LIST = "[data-testid='appslist']"
    APP_CARD = "[data-testid='app-card']"

    def should_be_opened(self):
        browser.should(have.url_containing("/catalog/search"))
        browser.should(have.title("RuStore — Каталог приложений для Android"))
        return self

    def should_have_results(self):
        browser.element(self.RESULTS_LIST).should(be.visible)
        browser.all(self.APP_CARD).should(have.size_greater_than(0))
        return self

    def first_result_should_contain(self, text: str):
        browser.all(self.APP_CARD).first.should(be.visible).should(have.text(text))
        return self
