from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим WebDriver искать каждый элемент в течение 5 секунд
#    browser.implicitly_wait(5)
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#    button = WebDriverWait(browser, 12).until(
#        EC.element_to_be_clickable((By.ID, "book"))
#    )

#    assert substring in full_string, \            проверка вхождения строки и вывод с помощью F
#        f"expected {substring} in {full_string}"

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(str(y))

    
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение