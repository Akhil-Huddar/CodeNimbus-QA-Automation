
import time

from google_sheet_logger import log_test_result
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invitation_template_live_demo():
    start_time = time.time()
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    status = "FAIL"
    error_reason = ""

    try:
        driver.get("https://invitationnation.in/")

        invitations_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Invitations']")
            )
        )
        invitations_button.click()

        wedding = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'a[href="/invitations/wedding"]')
            )
        )
        driver.execute_script("arguments[0].click();", wedding)

        template = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".collection-card-link")
            )
        )
        driver.execute_script("arguments[0].click();", template)

        wait.until(
            EC.url_contains("/invitations/wedding/")
        )

        live_demo = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(normalize-space(.), 'Live Demo')]")
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            live_demo
        )

        original_window = driver.current_window_handle
        windows_before = driver.window_handles

        driver.execute_script(
            "arguments[0].click();",
            live_demo
        )

        wait.until(
            lambda d: len(d.window_handles) > len(windows_before)
        )

        new_window = [
            window for window in driver.window_handles
            if window not in windows_before
        ][0]

        driver.switch_to.window(new_window)

        wait.until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        assert driver.current_url != ""

        body = wait.until(
            EC.visibility_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        assert body.is_displayed()

        print("\nTEST PASSED: Live Demo opened in a new tab.")
        print("Live Demo URL:", driver.current_url)
        print("Live Demo Title:", driver.title)

        driver.close()

        driver.switch_to.window(original_window)

        assert driver.current_window_handle == original_window

        print("TEST PASSED: Returned to original browser tab.")

        status = "PASS"

    except Exception as e:
        error_reason = str(e)

        print("\nTEST FAILED:", error_reason)

        raise

    finally:
        execution_time = round(time.time() - start_time, 2)

        log_test_result(
            "TC2 - Invitation Template Live Demo",
            status,
            execution_time,
            error_reason,
        )

        driver.quit()

