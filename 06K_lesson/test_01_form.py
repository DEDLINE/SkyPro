import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_fill_form_and_check_colors(driver):
    driver.get("https://bonigarcia.dev/selenium"
               "-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone": "+7985899998787",
        # "zip-code": "", # Оставляем пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in data.items():
        driver.find_element(By.NAME, name).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.visibility_of_element_located((By.ID, "alert-success")))

    zip_field = driver.find_element(By.ID, "zip-code")

    expected_red_class = "alert-danger"
    assert expected_red_class in zip_field.get_attribute("class"), \
        (f"Zip code должен быть красным. Фактический класс: "
         f"{zip_field.get_attribute('class')}")

    green_fields = [
        "first-name", "last-name", "address", "email", "phone",
        "city", "country", "job-position", "company"
    ]
    expected_green_class = "alert-success"

    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        assert expected_green_class in field.get_attribute("class"), \
            (f"Поле {field_id} должно быть зеленым. Фактический класс: "
             f"{field.get_attribute('class')}")
