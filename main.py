from pages.home_pages import Buscarproduto
from utils.browser_utils import navegador
from pages.extrair__info_produtos_pages import ExtraiInfoProdutoKipa
import time

#Extancia
kipa = Buscarproduto(navegador)
extract = ExtraiInfoProdutoKipa(navegador)


#Pesquisar produto
kipa.pesquisar_por_kipa("kipa")
kipa.click_button_pesquisar()

time.sleep(3)

# Extrai os nomes dos produtos e preços
product_names = extract.product_names()
product_prices = extract.product_prices()
extract.page_run()
# Cria a planilha com os dados
extract.create_plan(product_names, product_prices)