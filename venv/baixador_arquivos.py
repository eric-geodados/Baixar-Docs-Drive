from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import os

# AUTOMAÇÃO DE MENSAGENS NO INSTAGRAM

class BaixadorBot:
    def __init__(self, site, senha, pasta):
        self.site = site
        self.senha = senha
        self.pasta = pasta
        
        s = EdgeService(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=s)

    def baixar(self):
        try:
            driver = self.driver
            driver.get(self.site)
            time.sleep(5)
            
            try:
                senha_element = driver.find_element(By.XPATH, '//input[@name="txtPassword"]')
                senha_presente = True
            except NoSuchElementException:
                print("Elemento não encontrado")
                senha_presente = False
                
            if senha_presente:
                senha_element.send_keys(self.senha)
                senha_element.send_keys(Keys.RETURN)
                time.sleep(3)

            #     # Escolher pasta desejada
            #     driver.find_element(By.XPATH, '//*[text()="' + self.pasta + '"]').click()
            #     time.sleep(5)

            #     # Baixar os arquivos na pasta
            #     driver.find_element(By.XPATH, '//button[@data-automationid="downloadCommand"]').click()
            #     time.sleep(80)

            #     downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
            #     os.startfile(downloads_path)
            # else:
            # Escolher pasta desejada
            driver.find_element(By.XPATH, '//*[text()="' + self.pasta + '"]').click()
            time.sleep(5)

            # Baixar os arquivos na pasta
            driver.find_element(By.XPATH, '//button[@data-automationid="downloadCommand"]').click()
            time.sleep(80)
        
            downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
            os.startfile(downloads_path)

        except Exception as e:
            print(f'Ocorreu um erro: {e}')

        driver.quit()


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
