from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LeavePage(BasePage):
    # Locator for the Leave page header
    LEAVE_HEADER = (By.XPATH, "//h6[text()='Leave']")

    def is_loaded(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LEAVE_HEADER)
        )