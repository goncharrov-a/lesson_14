# 🧪 UI Test Automation Project

Автоматизация **UI-автотестов** для сайта **RuStore**.  
![Step1](images/0.jpg)

---

## 📑 Содержание

- [🛠 Стек технологий](#-стек-технологий)
- [🧩 Реализованные тесты](#-реализованные-тесты)
  - [🏠 Main page (test_main_page.py)](#-main-page-test_main_pagepy)
  - [⬇️ Instruction (test_instruction_page.py)](#-instruction-test_instruction_pagepy)
  - [🔍 Search page (test_search_page.py)](#-search-page-test_search_pagepy)
  - [🧪 Search results (test_search_results.py)](#-search-results-test_search_resultspy)
  - [📄 App page (test_app_page.py)](#-app-page-test_app_pagepy)
  - [🧾 Footer QR (test_footer.py)](#-footer-qr-test_footerpy)
  - [🆘 Footer support (test_footer_support_button.py)](#-footer-support-test_footer_support_buttonpy)
  - [🧨 Attachments (test_fail_header_check.py)](#-attachments-test_fail_header_checkpy)
- [▶️ Запуск](#️-запуск)
  - [Установка зависимостей](#установка-зависимостей)
  - [Запуск тестов](#запуск-тестов)
  - [Запуск с генерацией Allure-результатов](#запуск-с-генерацией-allure-результатов)
- [🖥 Запуск в Selenoid](#-запуск-в-selenoid)
- [⚙️ CI/CD в Jenkins](#️-cicd-в-jenkins)
- [📊 Allure Report](#-allure-report)
  - [Разделы отчёта (скриншоты)](#разделы-отчёта-скриншоты)
- [🧭 Интеграция с Allure TestOps](#-интеграция-с-allure-testops)
- [📬 Telegram-уведомления](#-telegram-уведомления)
  - [Пример уведомления (скриншот)](#пример-уведомления-скриншот)

---
## 🛠 Стек технологий

| Технология | Описание |
|-----------|----------|
| ![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python&logoColor=white)| язык разработки |
| ![Pytest](https://img.shields.io/badge/Pytest-9.0.2-orange?logo=pytest&logoColor=white) | тестовый фреймворк |
| ![Selene](https://img.shields.io/badge/Selene-2.0.0rc9-lightgrey) | обёртка над Selenium |
| ![Selenium](https://img.shields.io/badge/Selenium-4.39.0-lightblue?logo=selenium&logoColor=white) | драйвер для автоматизации браузера |
| ![Allure](https://img.shields.io/badge/Allure-2.15.3-pink) | отчёты о тестировании |
| ![Allure TestOps](https://img.shields.io/badge/Allure_TestOps-2.15.3-purple) | управление тестами |
| ![Selenoid](https://img.shields.io/badge/Selenoid-✓-green) | удалённый запуск браузеров |
| ![Jenkins](https://img.shields.io/badge/Jenkins-CI-red?logo=jenkins&logoColor=white)| CI/CD |
| ![Telegram Bot API](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram&logoColor=white) | уведомления о сборках |

---

## 🧩 Реализованные тесты

### 🏠 Main page (test_main_page.py)
**Цель:** Проверка открытия главной страницы и базовых элементов.

### ⬇️ Instruction (test_instruction_page.py)
**Цель:** Переход по кнопке «Скачать RuStore» на страницу инструкции.

### 🔍 Search page (test_search_page.py)
**Цель:** Проверка страницы поиска и списка «Часто ищут».

### 🧪 Search results (test_search_results.py)
**Цель:** Проверка результатов поиска по запросу «Госуслуги».

### 📄 App page (test_app_page.py)
**Цель:** Проверка карточки приложения «Госуслуги».

### 🧾 Footer QR (test_footer.py)
**Цель:** Проверка отображения QR-кода в футере.

### 🆘 Footer support (test_footer_support_button.py)
**Цель:** Проверка кнопки обращения в поддержку в футере.

### 🧨 Attachments (test_fail_header_check.py)
**Цель:** Намеренно падающий тест для проверки аттачей.

---

## ▶️ Запуск

### Установка зависимостей
```bash
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install
```
### Запуск тестов
```bash
poetry run pytest -v
```
### Запуск с генерацией Allure-результатов
```bash
poetry run pytest -v --alluredir=results
```
## 🖥 Запуск в Selenoid
Основные настройки указаны в `/Users/goncharov/qa_guru/lesson_14/core/browser.py`:
```bash
browserName: chrome
enableVNC: true
enableVideo: true
```
Видео и скриншоты автоматически прикрепляются к отчёту Allure.

---

## ⚙️ CI/CD в Jenkins
Jenkins job выполняет следующие шаги:

1. Клонирование репозитория  
2. Установка зависимостей  
3. Запуск UI-тестов в **Selenoid**  
4. Генерация **Allure Report**  
5. Уведомление в **Telegram**  

---

## 📊 Allure Report

Отчёт Allure содержит:

- пошаговое выполнение тестов  
- скриншоты  
- HTML-снимки DOM  
- видео прохождения тестов  
- логи браузера  

### Разделы отчёта (скриншоты)

- Allure report  
  [Аллюр отчет](https://jenkins.autotests.cloud/job/023-GoncharrovAS-lesson_14/12/allure/)

- Overview  
  ![Overview](images/1.jpg)

- Suites  
  ![Suites](images/2.jpg)

- Attachments  
  ![Attachments](images/3.jpg)


---

## 🧭 Интеграция с Allure TestOps

- [Тестопс запуск](https://allure.autotests.cloud/launch/51774)

В рамках проекта настроено:
- Проект в Allure TestOps  
  ![Проект в Allure TestOps](images/4.jpg)

- Загрузка результатов тестов из Jenkins  
  ![Загрузка из Jenkins](images/5.jpg)

- Аналитика и история запусков  
  ![Аналитика и история запусков](images/6.jpg)

---
## 📬 Telegram-уведомления

После завершения сборки Jenkins отправляет уведомление в Telegram, содержащее:

- окружение сборки  
- количество выполненных и пройденных тестов  
- ссылку на **Allure Report**  

### Пример уведомления (скриншот)

- Telegram message  
  ![Telegram message](images/7.jpg)

