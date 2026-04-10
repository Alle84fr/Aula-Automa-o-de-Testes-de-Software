from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


#________ fase 1__________

opcoes = Options()
driver = webdriver.Chrome()

opcoes.add_argument("--headless=new")
opcoes.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=opcoes)

print(f"🟡 🟢 🔵")

driver.get("https://the-internet.herokuapp.com/")
print(f"👽 Página {driver.title} aberta com sucesso!!")

#_____ trocar abas_____

driver.execute_script("window.open('https://the-internet.herokuapp.com/dynamic_loading/2')")

# abre a aba, esperaa té ter duas janelas, depois abre a 2° aba index 1 - aqui que valida e verifica quantidade de abas (window_handles)
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[1])

#delay para trocar abas
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

driver.execute_script("window.open('https://pt.wikipedia.org')")

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))
driver.switch_to.window(driver.window_handles[2])

driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))
driver.switch_to.window(driver.window_handles[0])

