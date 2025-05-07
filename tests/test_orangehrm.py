from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage
from pages.logout_page import Logout
import time

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.load() # Navigate to login page
    login_page.login() # Perform login with default credentials

    # Verify dashboard loads
    dashboard_page = DashboardPage(driver)
    time.sleep(2)
    assert dashboard_page.is_loaded(), "Dashboard page did not load."
    #driver.quit() Haven't add this as it slow down the performance

def test_leavepage(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login()

    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_loaded(), "Dashboard page did not load."

    # Navigate to Leave page
    dashboard_page.go_to_leave()
    leave_page = LeavePage(driver)

    # Verify dashboard loads
    assert leave_page.is_loaded(), "Leave page did not load after navigation."
    # driver.quit() Haven't add this as it slow down the performance

def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login()

    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_loaded(), "Dashboard page did not load."

    # Perform logout
    logout_page = Logout(driver)
    logout_page.logout()
    time.sleep(1)

    # Verify logout succeeded
    assert logout_page.is_logged_out(), "Did not redirect to login page after logout."
    # driver.quit() Haven't add this as it slow down the performance
