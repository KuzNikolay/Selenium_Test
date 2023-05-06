import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser.get(" http://suninjuly.github.io/explicit_wait2.html")

try:
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button =browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print(f'{x=} {y=}')
    y_element = browser.find_element(By.CLASS_NAME, "form-control")
    y_element.send_keys(y)

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    button.click()

    answer = browser.switch_to.alert.text.split(': ')[-1]
    print(answer)
    # time.sleep(10)
finally:
    # pass
    browser.quit()
