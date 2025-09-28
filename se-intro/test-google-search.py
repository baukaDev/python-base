# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://www.google.com")

# assert "Google" in driver.title

# element = driver.find_element(By.NAME, 'q')
# element.clear()
# element.send_keys("Cats photos")
# element.send_keys(Keys.RETURN)

# assert "ничего не найдено" not in driver.page_source

# input("Нажмите Enter для закрытия браузера...")

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.python.org/')
driver.save_screenshot('screenshot.png')
driver.quit()