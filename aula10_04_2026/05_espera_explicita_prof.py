from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

print("1. Acessando o site de testes...")
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

botao_start = driver.find_element(By.CSS_SELECTOR, "#start button")
botao_start.click()
print("2. Cliquei no botão Start. O site começou a carregar...")

print("3. Aguardando o elemento secreto aparecer (Espera Explícita)...")

elemento_secreto = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "finish"))
)

print("\nSucesso! O robô teve paciência e capturou o texto:")
print(f"--> '{elemento_secreto.text}'")

driver.quit()