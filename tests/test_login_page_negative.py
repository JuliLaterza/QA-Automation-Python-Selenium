import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        #   Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()

        #    Type username incorrectUser into Username field
        userInput = driver.find_element(by=By.ID, value="username")
        userInput.send_keys(username)

        #   Type password into Password Field
        passwordInput = driver.find_element(by=By.ID, value="password")
        passwordInput.send_keys(password)

        #    Puch Submit button
        submitBtn = driver.find_element(by=By.ID, value="submit")
        submitBtn.click()
        time.sleep(2)

        #    Verify error message is displayed
        error = driver.find_element(By.ID, "error")

        assert error.is_displayed(), "Error message is not displayed, but it should be."
        #    Verify error message text is Your username is invalid!
        error_message = error.text  # Obtengo el texto del error.

        assert error_message == expected_error_message, "Error message is not expected."

        driver.quit()

    def test_negative_username(self, driver):
        #   Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()

        #    Type username incorrectUser into Username field
        userInput = driver.find_element(by=By.ID, value="username")
        userInput.send_keys("incorrectUser")

        #   Type password into Password Field
        passwordInput = driver.find_element(by=By.ID, value="password")
        passwordInput.send_keys("Password123")

        #    Puch Submit button
        submitBtn = driver.find_element(by=By.ID, value="submit")
        submitBtn.click()
        time.sleep(2)

        #    Verify error message is displayed
        error = driver.find_element(By.ID, "error")

        assert error.is_displayed(), "Error message is not displayed, but it should be."
        #    Verify error message text is Your username is invalid!
        error_message = error.text  # Obtengo el texto del error.

        assert error_message == "Your username is invalid!", "Error message is not expected."

        driver.quit()

    def test_password_negative(self, driver):
        #   Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()

        #    Type username incorrectUser into Username field
        userInput = driver.find_element(by=By.ID, value="username")
        userInput.send_keys("student")

        #   Type password into Password Field
        passwordInput = driver.find_element(by=By.ID, value="password")
        passwordInput.send_keys("passwordIncorrect")

        #    Puch Submit button
        submitBtn = driver.find_element(by=By.ID, value="submit")
        submitBtn.click()
        time.sleep(2)

        #    Verify error message is displayed
        error = driver.find_element(By.ID, "error")

        assert error.is_displayed(), "Error message is not displayed, but it should be."
        #    Verify error message text is Your username is invalid!
        error_message = error.text  # Obtengo el texto del error.

        assert error_message == "Your password is invalid!", "Error message is not expected."

        driver.quit()
