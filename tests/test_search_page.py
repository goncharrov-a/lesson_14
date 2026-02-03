import allure
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage


@allure.tag("UI", "Поиск")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Страница поиска открывается и отображает список «Часто ищут»")
@pytest.mark.ui
@pytest.mark.search
def test_search_page_opens_and_shows_trends():
    main = MainPage()
    search = SearchPage()

    with allure.step("Открыть главную страницу"):
        main.open()

    with allure.step("Открыть поиск из шапки сайта"):
        main.open_search()

    with allure.step("Проверить, что открылась страница поиска"):
        search.should_be_opened()

    with allure.step("Проверить, что поле поиска пустое и плейсхолдер корректный"):
        search.should_have_empty_input_and_placeholder()

    with allure.step("Проверить, что список «Часто ищут» не пустой"):
        search.should_have_non_empty_trends()
