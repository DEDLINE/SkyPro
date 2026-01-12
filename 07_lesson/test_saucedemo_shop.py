import pytest
from selenium import webdriver
from .saucedemo_pages import (LoginPage, InventoryPage,
                              CartPage, CheckoutInfoPage)
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_full_purchase_scenario(driver):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_product_to_cart("Sauce Labs Onesie")

    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutInfoPage(driver)
    checkout_page.fill_and_continue(
        first_name="Иван",
        last_name="Тестов",
        zip_code="12345"
    )

    actual_total = checkout_page.get_total_price()
    expected_total = "$58.29"

    assert actual_total == expected_total, \
        (f"Итоговая сумма не совпадает. Ожидалось: "
         f"{expected_total}, Фактически: {actual_total}")
