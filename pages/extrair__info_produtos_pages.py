from selenium.webdriver.common.by import By
from openpyxl import Workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser_utils import navegador




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
        number_pages_element = self.navegador.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[5]/div/section/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/p/span')
        number_pages_text = number_pages_element.text.replace("Exibindo página ", "").split(" de ")[1]
        number_pages = int(number_pages_text)

        all_page_names = []  # Armazena todos os nomes das páginas
        all_page_prices = []  # Armazena todos os preços das páginas
        # page
        for page in range(1, number_pages + 1):
            page_name_texts = self.product_names()  # Extrai nomes para a página atual
            page_price_texts = self.product_prices()  # Extrai preços para a página atual

            all_page_names.extend(page_name_texts)  # Adiciona nomes da página atual à lista geral
            all_page_prices.extend(page_price_texts)  # Adiciona preços da página atual à lista geral

            try:
                button_next_page = WebDriverWait(self.navegador, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_CPH1_toolbarBottom_NextPageNav"]'))
                )
                self.navegador.execute_script("arguments[0].click();", button_next_page)
            except:
                break

        # self.create_plan(all_page_names, all_page_prices)  # Passa as listas combinadas para create_plan

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

        print("Dados extraídos e salvos no arquivo 'dados_produto.xlsx'.")



