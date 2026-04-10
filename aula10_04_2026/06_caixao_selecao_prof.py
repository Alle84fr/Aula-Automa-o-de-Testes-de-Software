from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

print("1. Acessando a página de Dropdown...")
driver.get("https://the-internet.herokuapp.com/dropdown")

elemento_dropdown = driver.find_element(By.ID, "dropdown")

menu = Select(elemento_dropdown)

print("2. Selecionando a 'Option 2' pelo texto visível...")
menu.select_by_visible_text("Option 2")

print("Sucesso! O robô escolheu a opção sem precisar 'clicar' para abrir o menu.")

driver.quit()