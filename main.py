

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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#Acá se crea el driver de Chrome. La instancia de Navegador.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Abrimos la página
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(3)

#inputs = driver.find_elements(by=By.TAG_NAME,value="input")
#userInput = inputs[0]

#Type Username Student
userInput = driver.find_element(by=By.ID, value="username")
userInput.send_keys('student')

#Type Password Student
passwordInput = driver.find_element(by=By.ID, value="password")
passwordInput.send_keys("Password123")

#Clic Submit Button.
subBtn = driver.find_element(by=By.XPATH, value='//*[@id="submit"]')
subBtn.click()
time.sleep(4)


#Verificar si la URL cambió luego de loguearse.

actualURL = driver.current_url

#Text locator
text_locator = driver.find_element(By.TAG_NAME,value='h1')
actual_text = text_locator.text


#logOut locator
log_outBtn = driver.find_element(By.LINK_TEXT,value="Log out")


print("Se cierra el navegador.")
driver.quit()