from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# AUTOMAÇÃO DE MENSAGENS NO INSTAGRAM

class BaixadorBot:
    def __init__(self, site, senha, pasta):
        self.site = site
        self.senha = senha
        self.pasta = pasta
        
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def baixar(self):
        try:
            # Fazer login no SharePoint (se necessário)
        # Assumindo que você tem os campos de login e senha
        # username = self.driver.find_element(By.ID, 'username_field_id')
        # password = self.driver.find_element(By.ID, 'password_field_id')

        # username.send_keys('seu_nome_de_usuario')
        # password.send_keys('sua_senha')
        # password.send_keys(Keys.RETURN)

        # Esperar o login ser concluído (ajuste o tempo de espera conforme necessário)
            # Definir o XPath dos arquivos (ajuste conforme necessário)
            xpath_dos_arquivos = '//div[@role="row"]//span[contains(@class, "ms-DetailsRow-cell")]//a[@aria-label]'

            # Obter a lista de elementos de download
            elementos_de_download = self.driver.find_elements(By.XPATH, xpath_dos_arquivos)

            # Pasta de destino para downloads
            pasta_destino = r'C:\Users\eric_cabral\Downloads'
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            # Iterar sobre os elementos e clicar em cada um para iniciar o download
            for elemento in elementos_de_download:
                try:
                    # Armazenar o nome do arquivo a ser baixado
                    nome_do_arquivo = elemento.get_attribute('aria-label')
                    print(f"Baixando: {nome_do_arquivo}")

                    # Clicar no elemento para iniciar o download
                    elemento.click()

                    # Esperar o download ser concluído (ajuste o tempo conforme necessário)
                    time.sleep(10)

                    # Mover o arquivo baixado para a pasta de destino
                    caminho_origem = os.path.join(os.path.expanduser('~'), 'Downloads', nome_do_arquivo)
                    caminho_destino = os.path.join(pasta_destino, nome_do_arquivo)
                    if os.path.exists(caminho_origem):
                        os.rename(caminho_origem, caminho_destino)

                except Exception as e:
                    print(f"Erro ao baixar {nome_do_arquivo}: {e}")

            # Encerrar o WebDriver
            self.driver.quit()
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

# EXIBIÇÕES NO TERMINAL
print("=-"* 25)
print("BAIXADOR DE ARQUIVOS DO DRIVE")
print("=-"* 25)

print("\n")
print("INSIRA OS DADOS NECESSÁRIOS")
print("-"* 50)

input_site = input(str('Link do Sharepoint: ')).strip()
print("-"* 50)
input_senha = input(str('Senha de acesso (Caso haja): ')).strip()
print("-"* 50)
input_pasta = input(str('Nome da pasta que deseja baixar: ')).strip()

print("\n")
time.sleep(1)
print("=-"* 25)
print("AGORA INICIAREMOS A TAREFA .....")
print("=-"* 25)
time.sleep(2)
iniciar = BaixadorBot(input_site, input_senha, input_pasta)
iniciar.baixar()
