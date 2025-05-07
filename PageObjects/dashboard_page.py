from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class DashboardPage(BasePage):
    # Locator for the Dashboard page header
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    # Locator for the 'Leave' menu item in the sidebar
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']/ancestor::a")

    def go_to_leave(self):
        leave_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LEAVE_MENU)
        )
        leave_menu.click()

    def is_loaded(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.DASHBOARD_HEADER)
        )
