# tests/test_orangehrm.py
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage

def test_home_page_title(driver):
    login_page = LoginPage(driver)
    login_page.load()
    assert driver.title == "OrangeHRM", f"Expected 'OrangeHRM', got '{driver.title}'"

def test_login_functionality(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_loaded(), "Dashboard page did not load."

def test_leave_functionality(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login()
    dashboard_page = DashboardPage(driver)
    dashboard_page.is_loaded()
    dashboard_page.go_to_leave()
    leave_page = LeavePage(driver)
    assert leave_page.is_loaded(), "Leave page did not load."

def test_logout_functionality(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login()

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    wait = WebDriverWait(driver, 10)

    user_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="oxd-userdropdown-tab"]')))
    user_dropdown.click()

    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Logout"]')))
    logout_button.click()

    assert "login" in driver.current_url
