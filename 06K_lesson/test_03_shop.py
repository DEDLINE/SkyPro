import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_saucedemo_purchase(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product_name in products_to_add:
        add_to_cart_xpath = (
            f"//div[text()='{product_name}']/ancestor::div[@class="
            f"'inventory_item_label']"
            f"/following-sibling::div[@class='pricebar']/button"
        )
        driver.find_element(By.XPATH, add_to_cart_xpath).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    wait = WebDriverWait(driver, 10)
    total_text_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        ".summary_total_label"))
    )

    total_text = total_text_element.text.replace("Total: ", "")

    expected_total = "$58.29"
    assert total_text == expected_total, (f"Итоговая сумма не совпадает. "
                                          f"Ожидалось: {expected_total}, "
                                          f"Фактически: {total_text}")
