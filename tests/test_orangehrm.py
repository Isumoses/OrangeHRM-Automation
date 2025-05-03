import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time

def test_home_page_title(driver):
    """1. Load the login page and check the title"""
    login_page = LoginPage(driver)
    login_page.load()
    time.sleep(2)
    assert driver.title == "OrangeHRM", f"Expected 'OrangeHRM', got '{driver.title}'"

def test_login_and_dashboard(driver):
    """2. Login and verify dashboard is shown"""
    login_page = LoginPage(driver)
    login_page.load()
    time.sleep(1)
    login_page.login()
    time.sleep(2)
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_loaded(), "Dashboard page did not load."
    time.sleep(2)

def test_login_dashboard_logout(driver):
    """3. Login, verify dashboard, then logout"""
    login_page = LoginPage(driver)
    login_page.load()
    time.sleep(1)
    login_page.login()
    time.sleep(2)
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_loaded(), "Dashboard page did not load."
    time.sleep(2)

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    wait = WebDriverWait(driver, 10)
    user_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="oxd-userdropdown-tab"]')))
    user_dropdown.click()
    time.sleep(1)
    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Logout"]')))
    logout_button.click()
    time.sleep(2)
    assert "login" in driver.current_url
