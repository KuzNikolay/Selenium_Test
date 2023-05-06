import os

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
link = " http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input2 = browser.find_element(By.NAME, "email")
    input2.send_keys("Petrov@ivan.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_input = browser.find_element(By.NAME, "file")
    file_input.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print(browser.switch_to.alert.text)
finally:
    browser.quit()