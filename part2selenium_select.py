from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    x1_el = browser.find_element_by_id("num1")
    x2_el = browser.find_element_by_id("num2")
    x1 = x1_el.text
    x2 = x2_el.text
    sum = int(x1) + int(x2)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))

    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

#Напишите код, который реализует следующий сценарий:

# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"