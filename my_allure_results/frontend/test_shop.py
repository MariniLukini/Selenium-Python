"""
Импортируем модули и отдельные классы
"""
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

URL = 'https://testqastudio.me'

def test_product_view_sku():
    """
    Test case WERT-1
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    chrome_options.add_argument("--disable-gpu") #применимо только к ОС Windows
    chrome_options.add_argument("--disable-dev-shm-usage") # преодоление проблем с ограниченными ресурсами
    #chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
	# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service()
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url=URL)

    # ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()

    # ищем по селектору карточку "ЭЛЛЬБИ Подвесная лампа" и кликаем по нему,
    # чтобы просмотреть детали
    element = driver.find_element(by=By.CSS_SELECTOR, value='[class*="post-11340"]')
    element.click()

    # ищем по имени класса артикул для "Подвесная лампа"
    sku = driver.find_element(By.CLASS_NAME, value="sku")

    # проверяем соответствие
    assert sku.text == 'BFB9ZOK210', "Unexpected sku"