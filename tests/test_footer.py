import allure
import pytest

from pages.footer import Footer
from pages.main_page import MainPage


@allure.tag("UI", "Футер")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("В футере отображается QR-код для скачивания RuStore")
@pytest.mark.ui
@pytest.mark.footer
def test_footer_contains_qr_code():
    main_page = MainPage()
    footer = Footer()

    with allure.step("Открыть главную страницу"):
        main_page.open()

    with allure.step("Прокрутить страницу к футеру"):
        footer.scroll_to_footer()

    with allure.step("Проверить отображение QR-кода"):
        footer.should_have_qr_code()
