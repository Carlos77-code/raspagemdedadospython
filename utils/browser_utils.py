from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#Criando o Robô
navegador = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

#Acessando o site
navegador.get('https://www.sefer.com.br/')


headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

#Maximizar a janela
# navegador.maximize_window()