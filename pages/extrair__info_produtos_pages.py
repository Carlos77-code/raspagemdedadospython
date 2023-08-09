from selenium.webdriver.common.by import By
from openpyxl import Workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser_utils import navegador
import time




class ExtraiInfoProdutoKipa:
    def __init__(self, navegador):
        self.navegador = navegador

    def product_names(self):
        # Implementação do método product_names
        page_name_elements = self.navegador.find_elements(By.CLASS_NAME, 'product-name')

        page_name_texts = [element.text for element in page_name_elements]
        return page_name_texts
    
    def product_prices(self):
        # Implementação do método product_prices
        page_price_elements = self.navegador.find_elements(By.CLASS_NAME, 'regular-price')

        page_price_texts = [element.text for element in page_price_elements]
        return page_price_texts
    
    def page_run(self):
        all_page_names = []  # Armazena todos os nomes das páginas
        all_page_prices = []  # Armazena todos os preços das páginas
        current_page = 1
        
        while True:
            page_name_texts = self.product_names()  # Extrai nomes para a página atual
            page_price_texts = self.product_prices()  # Extrai preços para a página atual
            
            all_page_names.extend(page_name_texts)  # Adiciona nomes da página atual à lista geral
            all_page_prices.extend(page_price_texts)  # Adiciona preços da página atual à lista geral
            print("Página:", current_page)  # Print do número da página
            current_page += 1
            
            try:
                button_next_page = self.navegador.find_element(By.XPATH, '//*[@id="ctl00_CPH1_toolbarBottom_NextPageNav"]')
                if not button_next_page.is_enabled():
                    break  # Sai do loop se o botão "Next Page" não estiver habilitado
                    
                self.navegador.execute_script("arguments[0].click();", button_next_page)
                
                time.sleep(2)  # Aguarda um tempo para a próxima página carregar
                
            except:
                break

        print("Nomes:", all_page_names)  # Print dos nomes coletados
        print("Preços:", all_page_prices)  # Print dos preços coletados
        
        self.create_plan(all_page_names, all_page_prices)  # Passa as listas combinadas para create_plan
                

    def create_plan(self, all_page_names, all_page_prices):
        # Criar um novo arquivo XLSX e uma planilha
        workbook = Workbook()
        sheet = workbook.active

        # Insere os cabeçalhos na planilha
        sheet.append(["Description product", "Price product"])

        # Itera sobre os dados e insere um abaixo do outro
        for name, price in zip(all_page_names, all_page_prices):
            sheet.append([name, price])
        
        # Salva o arquivo XLSX
        workbook.save(".\\arquivos\\dados_product.xlsx")

        # print("Dados extraídos e salvos no arquivo 'dados_produto.xlsx'.")
