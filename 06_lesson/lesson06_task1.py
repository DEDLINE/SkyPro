from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://uitestingplayground.com/ajax")

    driver.find_element(By.ID, "ajaxButton").click()

    ajax_text_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content > p"))
    )

    print(ajax_text_element.text)
