from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username="Admin", password="admin123"):
        # Wait for the username field to be present and enter the username
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD)).send_keys(username)
        # Enter the password in the password field
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        # Click the login button to submit the form
        self.driver.find_element(*self.LOGIN_BUTTON).click()
