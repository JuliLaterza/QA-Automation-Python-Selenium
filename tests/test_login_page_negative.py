import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self):
        #   Open page
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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

    @pytest.mark.login
    @pytest.mark.negative
    def test_password_negative(self):
        #   Open page
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
