"""
Open page
Type username student into Username field
Type password Password123 into Password field
Puch Submit button
Verify new page URL contains practicetestautomation.com/logged-in-successfully/
Verify new page contains expected text ('Congratulations' or 'successfully logged in')
Verify button Log out is displayed on the new page
"""

import time
from selenium.webdriver.common.by import By
import pytest


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # Abrimos la página
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(3)

        # inputs = driver.find_elements(by=By.TAG_NAME,value="input")
        # userInput = inputs[0]

        # Type Username Student
        userInput = driver.find_element(by=By.ID, value="username")
        userInput.send_keys('student')

        # Type Password Student
        passwordInput = driver.find_element(by=By.ID, value="password")
        passwordInput.send_keys("Password123")

        # Clic Submit Button.
        subBtn = driver.find_element(by=By.XPATH, value='//*[@id="submit"]')
        subBtn.click()
        time.sleep(4)

        # Verificar si la URL cambió luego de loguearse.
        actualURL = driver.current_url
        assert actualURL == "https://practicetestautomation.com/logged-in-successfully/", "No se ingresó correctamente."

        # Text locator
        text_locator = driver.find_element(By.TAG_NAME, value='h1')
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully", "No se ingresó correctamente."

        # logOut locator
        log_outBtn = driver.find_element(By.LINK_TEXT, value="Log out")
        assert log_outBtn.is_displayed(), "No se visualiza el botón."

        print("Ejecución Exitosa")
        driver.quit()
