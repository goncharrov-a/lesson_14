import allure
import pytest

from pages.main_page import MainPage


@allure.tag("UI", "Негатив", "Аттачи")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка аттачей: намеренно падающий тест меню хедера")
@pytest.mark.ui
@pytest.mark.attachments
def test_header_links_should_fail_to_check_attachments():
    main_page = MainPage()

    with allure.step("Открыть главную страницу"):
        main_page.open()

    with allure.step("Проверить пункт меню «Приложения»"):
        main_page.should_have_clickable_header_link("Приложения")

    with allure.step("Проверить пункт меню «Игры»"):
        main_page.should_have_clickable_header_link("Игры")

    with allure.step("Проверить пункт меню «Киоск»"):
        main_page.should_have_clickable_header_link("Киоск")

    with allure.step("Проверить пункт меню «Блог»"):
        main_page.should_have_clickable_header_link("Блог")

    with allure.step("Проверить пункт меню «Разработчикам»"):
        main_page.should_have_clickable_header_link("Разработчикам")

    with allure.step("Проверить пункт меню «Помощь»"):
        main_page.should_have_clickable_header_link("Помощь")

    # намеренно ломаем
    with allure.step("Намеренно сломать тест для проверки аттачей"):
        main_page.should_have_clickable_header_link("Несуществующий пункт меню")
