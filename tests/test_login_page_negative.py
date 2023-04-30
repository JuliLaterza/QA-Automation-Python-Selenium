import time
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
class TestNegativeScenarios:

    def test_negative_username(self):

        #   Open page
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()

        #    Type username incorrectUser into Username field
        userInput = driver.find_element(by=By.ID, value = "username")
        userInput.send_keys("incorrectUser")


        #    Type password Password123 into Password field

        #    Puch Submit button

        #    Verify error message is displayed

        #    Verify error message text is Your username is invalid!

