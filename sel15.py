import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # time.sleep(3)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window) # Swich webDriver to new window

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.CLASS_NAME, "form-control")
    y_element.send_keys(y)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    answer = browser.switch_to.alert.text.split(': ')[-1]
    print(answer)
finally:
    browser.quit()
