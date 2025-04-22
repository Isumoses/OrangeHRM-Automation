from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import time

class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        time.sleep(2)

    def load(self):
        self.driver.get(self.URL)

    def login(self, username="Admin", password="admin123"):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD)).send_keys(username)
        time.sleep(1)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(2)
