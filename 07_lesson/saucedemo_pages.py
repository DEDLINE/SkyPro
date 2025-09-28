from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()


class InventoryPage:

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        add_to_cart_xpath = (
            f"//div[text()='{product_name}']/ancestor::div"
            f"[@class='inventory_item_label']"
            f"/following-sibling::div[@class='pricebar']/button"
        )
        self.driver.find_element(By.XPATH, add_to_cart_xpath).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()


class CartPage:

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()


class CheckoutInfoPage:

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_and_continue(self, first_name, last_name, zip_code):
        (self.driver.find_element(*self.FIRST_NAME_INPUT)
         .send_keys(first_name))
        (self.driver.find_element(*self.LAST_NAME_INPUT)
         .send_keys(last_name))
        (self.driver.find_element(*self.POSTAL_CODE_INPUT)
         .send_keys(zip_code))
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_price(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_PRICE)
        )
        total_text = total_element.text.replace("Total: ", "")
        return total_text
