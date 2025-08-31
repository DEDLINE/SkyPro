from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://uitestingplayground.com/classattr")
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
