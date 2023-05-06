import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/selects1.html'
browser.get(link)
try:
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    summa = str(int(num1)+int(num2))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(summa)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(3)
    browser.quit()