# Финальный тестовый проект SkillFactory курса QAP:
- Выбран сайт Ozon.ru, для которого необходимо написать 50-70 автоматизированных тестов с использованием PyTest и Selenium.
- Для запуска теста необходимо выполнить команду: python -m pytest -v --driver Chrome --driver-path <путь к файлу chromedriver.exe> tests.py. 
- Необходимо выбрать версию chromedriver и загрузить webdriver, который совместим с Вашим браузером.
- В файле elements.py находится конструктор webdriver и общие для всех тестируемых страниц методы.
- В файле conftest.py находится фикстура с функцией открытия и закрытия браузера.
- В папке tests и файле tests.py находятся тесты.
- В файле main.py указаны локаторы для элементов.
- В работе применена Page Object Мodel (POM) от Master QA Timur Nurlygayanov.
