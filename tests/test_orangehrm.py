import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time

def test_login_to_dashboard(driver):
    login_page = LoginPage(driver)
    login_page.load()
    time.sleep(1)
    login_page.login()
    time.sleep(2)
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_loaded(), "Dashboard page did not load."

def test_dashboard_close_button(driver):
    login_page = LoginPage(driver)
    login_page.load()
    time.sleep(1)
    login_page.login()
    time.sleep(2)
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_loaded(), "Dashboard page did not load."
    time.sleep(2)
    driver.quit()

def test_dashboard_logout(driver):
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
    assert "login" in driver.current_url, "Did not redirect to login page after logout."
