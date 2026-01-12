import pytest
from selenium import webdriver
from .slow_calculator_page import SlowCalculatorPage
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_calculator_functionality(driver):

    calc_page = SlowCalculatorPage(driver)

    calc_page.open()

    delay_time = "45"
    calc_page.set_delay(delay_time)

    expression = ["7", "+", "8", "="]
    calc_page.calculate(expression)

    expected_result = "15"
    actual_result = calc_page.get_result_text_after_wait(expected_result,
                                                         int(delay_time))

    assert actual_result == expected_result
