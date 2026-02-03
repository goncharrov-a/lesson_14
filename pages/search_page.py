from selene import browser, have, be


class SearchPage:
    SEARCH_INPUT = "[data-testid='search_input']"
    FIND_BUTTON = "[data-testid='findAppsButton']"
    APPS_LIST = "[data-testid='apps_list']"
    TRENDS = "[data-testid='search_trend']"

    def should_be_opened(self):
        browser.element(self.SEARCH_INPUT).should(be.visible)
        return self

    def should_have_empty_input_and_placeholder(self):
        search_input = browser.element(self.SEARCH_INPUT)
        search_input.should(be.visible).should(be.enabled)
        search_input.should(have.value(""))
        search_input.should(have.attribute("placeholder").value("Поиск приложений и игр"))
        return self

    def should_have_non_empty_trends(self):
        browser.element(self.APPS_LIST).should(be.visible)
        browser.all(self.TRENDS).should(have.size_greater_than(0))
        return self

    def type_query(self, query: str):
        inp = browser.element(self.SEARCH_INPUT).should(be.visible).should(be.enabled)
        inp.click()
        inp.set_value(query)
        return self

    def submit(self):
        search_input = browser.element(self.SEARCH_INPUT).should(be.visible).should(be.enabled)
        search_input.click()

        find_btn = browser.element(self.FIND_BUTTON)

        if find_btn.matching(be.visible):
            find_btn.should(be.clickable).click()
            return self

        search_input.press_enter()
        return self