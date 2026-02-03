import allure
import pytest

from pages.footer import Footer
from pages.main_page import MainPage


@allure.tag("UI", "Футер")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("В футере отображается кнопка обращения в поддержку")
@pytest.mark.ui
@pytest.mark.footer
def test_footer_contains_support_button():
    main_page = MainPage()
    footer = Footer()

    with allure.step("Открыть главную страницу"):
        main_page.open()

    with allure.step("Прокрутить страницу к футеру"):
        footer.scroll_to_footer()

    with allure.step("Проверить отображение кнопки обращения в поддержку"):
        footer.should_have_support_button()
