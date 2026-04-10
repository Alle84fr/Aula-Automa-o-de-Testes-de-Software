# espera para todos
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

print("1. Acessando o site...")
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

print("2. Clicando no botão Start...")
driver.find_element(By.CSS_SELECTOR, "#start button").click()

print("3. Procurando o texto secreto...")

texto_secreto = driver.find_element(By.ID, "finish")

print(f"\nSucesso! O robô teve paciência e capturou o texto:")
print(f"--> '{texto_secreto.text}'")

driver.quit()