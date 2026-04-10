from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

print("Acessando o Google...")
driver.get("https://www.google.com")
driver.save_screenshot("1_print_google.png")

print("Abrindo nova aba para a Wikipédia...")
driver.execute_script("window.open('https://pt.wikipedia.org');")
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

driver.switch_to.window(driver.window_handles[1])
driver.save_screenshot("2_print_wikipedia.png")

print("Abrindo nova aba para o site da Impacta")
# drive....script - executa js da pag
# dentro abre nova aba
driver.execute_script("window.open('https://www.impacta.edu.br/');")
# abre a página e verifica quantidade de handless que aqui é 3
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))

# troca a aba
# faz selenium ir para outra aba
# driver.window_handles[] - vê quantidade de abas 0 = primeira, 1, seginda....
driver.switch_to.window(driver.window_handles[2])
driver.save_screenshot("3_print_python.png")

driver.quit()