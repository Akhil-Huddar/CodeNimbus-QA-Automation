import time
import os
from pathlib import Path
from dotenv import load_dotenv
from google_sheet_logger import log_test_result
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv(Path(__file__).parent.parent / ".env")
def test_login_and_dashboard():
    start_time = time.time()
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    email = os.getenv("INVITATION_EMAIL")
    password = os.getenv("INVITATION_PASSWORD")
    status = "FAIL"
    error_reason = ""
    try:
        assert email, "INVITATION_EMAIL is missing from .env"
        assert password, "INVITATION_PASSWORD is missing from .env"
        driver.get("https://invitationnation.in/")
        sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "user-signin-signup")))
        sign_in_button.click()
        wait.until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])
        email_box = wait.until(EC.visibility_of_element_located((By.ID, "signin-email")))
        email_box.send_keys(email)
        password_box = wait.until(EC.visibility_of_element_located((By.ID, "signin-password")))
        password_box.send_keys(password)
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "signin-submit-button")))
        login_button.click()
        dashboard_heading = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Welcome to Invitation Nation')]")))
        assert dashboard_heading.is_displayed()
        status = "PASS"
        print("TEST PASSED: Login successful and User Dashboard loaded.")
    except Exception as e:
        error_reason = str(e)
        print("TEST FAILED:", error_reason)
        raise
    finally:
        execution_time = round(time.time() - start_time, 2)
        log_test_result("TC1 - Login and User Dashboard", status, execution_time, error_reason)
        driver.quit()
