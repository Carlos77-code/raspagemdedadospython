from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Buscarproduto:
    def __init__(self, navegador):
        self.navegador = navegador

    def pesquisar_por_kipa(self, kipa_prod):
        name_kipa = self.navegador.find_element(By.ID, "ctl00_headerSearch_search")
        name_kipa.clear()
        name_kipa.send_keys(kipa_prod)
    
    def click_button_pesquisar(self):
        button_click = self.navegador.find_element(By.ID, "ctl00_headerSearch_searchButton")
        button_click.click()

    def wait_until_loaded(self):
        WebDriverWait(self.navegador, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "label.Busca:"))
        )

    def kipa(self, kipa_prod, button_click):
        self.wait_until_loaded()
        self.pesquisar_por_kipa(kipa_prod)
        self.click_button_pesquisar(button_click)
