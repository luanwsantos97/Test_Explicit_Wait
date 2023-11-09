import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Necessário importar para usar o alert

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

wait = WebDriverWait(driver, 15)

driver.find_element(By.ID, "alert").click()
wait.until(EC.alert_is_present()) #Opção que identifica o alerta que é exibido. EC é a condição esperada. alert_is_present é a condição de alerta.
alert = driver.switch_to.alert
alert.accept()
assert alert

driver.find_element(By.ID, "populate-text").click()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@class='target-text']"), "Selenium Webdriver"))
target_text = driver.find_element(By.XPATH, "//*[@class='target-text']").text
assert target_text == "Selenium Webdriver"
time.sleep(2)

driver.find_element(By.ID, "display-other-button").click()
wait.until(EC.element_to_be_clickable((By.ID, "hidden")))
verification_button = driver.find_element(By.ID, "hidden")
assert verification_button

driver.find_element(By.ID, "enable-button").click()
wait.until(EC.element_to_be_clickable((By.ID, "disable")))
time.sleep(2)

driver.find_element(By.ID, "checkbox").click()
wait.until(EC.element_located_selection_state_to_be((By.ID, "ch"), is_selected=True))
verification_ch = driver.find_element(By.ID, 'ch')
assert verification_ch

quit()