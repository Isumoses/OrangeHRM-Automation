from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class DashboardPage(BasePage):
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']/ancestor::a")

    def is_loaded(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.DASHBOARD_HEADER)
        )

    def go_to_leave(self):
        leave_menu = self.wait.until(EC.element_to_be_clickable(self.LEAVE_MENU))
        leave_menu.click()

    def verify_header(self):
        return self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER)).text

    def click_leave(self):
        self.driver.find_element(*self.LEAVE_MENU).click()
