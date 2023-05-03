import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    print("Creating Chrome Driver")
    my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield my_driver
    print("Close Driver")
    my_driver.quit()
