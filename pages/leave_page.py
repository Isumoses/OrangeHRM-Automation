# pages/leave_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LeavePage(BasePage):
    LEAVE_HEADER = (By.XPATH, "//h6[text()='Leave']")

    def is_loaded(self):
        return self.wait.until(EC.presence_of_element_located(self.LEAVE_HEADER))
