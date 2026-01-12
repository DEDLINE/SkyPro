from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://uitestingplayground.com/textinput")

    text_input = driver.find_element(By.ID, "newButtonName")
    text_input.send_keys("SkyPro")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    print(button.text)
