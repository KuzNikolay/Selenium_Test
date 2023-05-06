import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # x_element = browser.find_element(By.ID, "input_value")
    # x = x_element.text
    # y = calc(x)
    # y_element = browser.find_element(By.CLASS_NAME, "form-control")
    # y_element.send_keys(y)
    # option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    # option1.click()
    # option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    # option2.click()
    # time.sleep(1)
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

    # browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    # browser.find_element_by_id('robotCheckbox').click()
    # browser.find_element_by_id('robotsRule').click()
    # browser.find_element_by_tag_name('button').click()
    # print(browser.switch_to.alert.text)
    # browser.find_element(By.ID, 'answer').send_keys(calc(browser.find_element(By.ID, 'input_value').text))
    # browser.find_element(By.ID, 'robotCheckbox').click()
    # browser.find_element(By.ID, 'robotsRule').click()
    # browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # print(browser.switch_to.alert.text)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked") # TRUE
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None


finally:
    time.sleep(10)
    browser.quit()
