from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:

    URL = ("https://bonigarcia.dev/selenium-webdriver-java"
           "/slow-calculator.html")

    DELAY_INPUT = (By.ID, "delay")
    RESULT_SCREEN = (By.CLASS_NAME, "screen")

    BUTTON_XPATH_TEMPLATE = "//span[text()='{}']"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value):
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.send_keys(value)

    def click_button(self, button_value):
        xpath = self.BUTTON_XPATH_TEMPLATE.format(button_value)
        self.driver.find_element(By.XPATH, xpath).click()

    def calculate(self, expression_list):
        for item in expression_list:
            self.click_button(item)

    def get_result_text_after_wait(self, expected_result, timeout):
        wait = WebDriverWait(self.driver, timeout + 1)

        wait.until(EC.text_to_be_present_in_element(self.RESULT_SCREEN,
                                                    expected_result))

        return self.driver.find_element(*self.RESULT_SCREEN).text
