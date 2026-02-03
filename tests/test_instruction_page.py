import allure
import pytest

from pages.instruction_page import InstructionPage
from pages.main_page import MainPage


@allure.tag("UI", "Смоук")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Кнопка «Скачать RuStore» на главной открывает страницу инструкции")
@pytest.mark.ui
@pytest.mark.smoke
def test_download_button_opens_instruction_page():
    main = MainPage()
    instruction = InstructionPage()

    with allure.step("Открыть главную страницу"):
        main.open()

    with allure.step("Проверить наличие кнопки «Скачать RuStore» на главной"):
        main.should_have_download_button()

    with allure.step("Нажать «Скачать RuStore» и перейти на страницу инструкции"):
        main.go_to_instruction()

    with allure.step("Проверить, что открылась страница инструкции"):
        instruction.should_be_opened()

    with allure.step("Проверить заголовок страницы инструкции"):
        instruction.should_have_correct_title()

    with allure.step("Проверить наличие кнопки скачивания и кликабельность ссылки"):
        instruction.should_have_download_button()

    with allure.step("Проверить атрибуты ссылки скачивания"):
        instruction.should_have_download_link_attrs()
