import math
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

try:
    x = browser.find_element(By.ID, "input_value").text
    f_x = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(f_x)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button.click()
    print(browser.switch_to.alert.text)
finally:
    browser.quit()



