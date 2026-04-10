from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com.br")

print("--- EXTRAINDO DADOS DO GOOGLE ---\n")

barra_pesquisa = driver.find_element(By.NAME, "q")

barra_pesquisa.send_keys("Como aprender Selenium")

texto_digitado = barra_pesquisa.get_attribute("value")
print(f"1. O que está escrito na barra de pesquisa? R: '{texto_digitado}'")

link_gmail = driver.find_element(By.LINK_TEXT, "Gmail")

texto_do_link = link_gmail.text

destino_do_link = link_gmail.get_attribute("href")

print(f"2. O texto visível do botão é: '{texto_do_link}'")
print(f"3. O link oculto por trás dele é: '{destino_do_link}'")

driver.quit()