from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

## Открывает браузер Chrome.
driver = webdriver.Chrome()

## Переходит на сайт http://www.python.org.
driver.get("http://www.python.org")
## Проверяет, что в заголовке страницы есть слово "Python".
## Если нет, выбрасывает исключение с сообщением "Не удалось загрузить python.org
if not "Pythond" in driver.title:
    print("Не удалось загрузить python.org")
assert "Python" in driver.title

## Находит текстовое поле поиска по имени элемента.
elem = driver.find_element(By.NAME, 'q')

## Очищает текстовое поле (input поиска).
elem.clear()

## Вводит в текстовое поле слово "pycon".
elem.send_keys("pycon")

## Отправляет форму (нажимает Enter).
elem.send_keys(Keys.RETURN)

## Если на странице результатов поиска появится текст "No results found.", то строка: вызовет исключение AssertionError, и выполнение скрипта прервётся. Это означает, что поиск не дал результатов, и скрипт считает это ошибкой.
assert "No results found." not in driver.page_source
## Закрывает браузер. Если всё прошло успешно, то браузер закроется без ошибок.
driver.close()