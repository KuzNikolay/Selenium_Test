"""Десять правил построения хороших локаторов, мастер-класс
https://docs.google.com/forms/d/e/1FAIpQLSeH2tck0nP80ThQOaojA3hyVnMgmiz7sdav2wYWYsLfCOhpTw/viewform"""
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://litecart.stqa.ru/index.php/en/")

try:
    products = browser.find_elements(By.CLASS_NAME, "product")
    print(len(products))
finally:
    browser.quit()