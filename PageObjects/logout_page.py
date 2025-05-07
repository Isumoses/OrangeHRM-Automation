from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class Logout(BasePage):
    USER_DROPDOWN = (By.XPATH, '//span[@class="oxd-userdropdown-tab"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[text()="Logout"]')

    def logout(self):
        # Click the user dropdown
        user_dropdown = self.wait.until(
            EC.element_to_be_clickable(self.USER_DROPDOWN)
        )
        user_dropdown.click()

        # Click the logout button
        logout_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON)
        )
        logout_button.click()

    def is_logged_out(self):
        # Check if redirected to login page
        return "login" in self.driver.current_url
