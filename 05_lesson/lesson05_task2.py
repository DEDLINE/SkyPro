from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://uitestingplayground.com/dynamicid")
    driver.find_element(
        By.XPATH, "//button[text()='Button with Dynamic ID']"
    ).click()
