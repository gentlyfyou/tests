from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class TestYandexLogin:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_login_page_loads(self):
        self.driver.get("https://passport.yandex.ru/auth/")
        
        assert "Яндекс" in self.driver.title

        login_field = self.driver.find_element(By.ID, "passp-field-login")
        assert login_field.is_displayed(), "Поле ввода логина не найдено или не отображается"