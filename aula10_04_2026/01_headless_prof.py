# selenium - automatização de navegador
# webdriver - controla o navegador
# para criar e navegar no chrome, por exemplo
from selenium import webdriver
# importa caminho interno 
# configura opções do Chrome, personaliza como vai abrir e funcionar, como rodar headless(sem abrir janelas visíveis na tela, roda por baixo do Chrome, sem ser visto), tamanho de janela (), perfil de usuário(), mudar usuários ....
from selenium.webdriver.chrome.options import Options


options = Options()

# .add_agument - argumento de iniciação ao chrome
# --headless=new - hedless na nova versão
options.add_argument("--headless=new") 
# usado para layout responsivo, para tirar screenshot e garantir que elementos estejam no devido lugar
options.add_argument("--window-size=1920,1080") 

# para iniciar o navegador
driver = webdriver.Chrome(options=options) 

# drive controla o navegador
# .get() abre url
driver.get("https://www.google.com")
# driver.title retona o tpítula da página aberta
print(f"Sucesso! Título: {driver.title}")
# .save_screenshot = print
driver.save_screenshot("tela-login.png") 
driver.quit()