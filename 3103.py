import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Открываем страницу
browser = webdriver.Chrome()
browser.get("https://SunInJuly.github.io/execute_script.html")

try:
    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Скроллим страницу вниз до текстового поля
    answer_field = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", answer_field)
    
    # Вводим ответ
    answer_field.send_keys(y)
    
    # Отмечаем checkbox
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    # Выбираем radiobutton
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("arguments[0].click();", radiobutton)
    
    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
finally:
    # Даем время для копирования результата
    time.sleep(10)
    browser.quit()