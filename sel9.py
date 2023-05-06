import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    print(f'{x=} {y=}')
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(5)
    browser.quit()
