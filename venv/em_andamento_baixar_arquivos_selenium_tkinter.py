from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
import os
from tkinter import filedialog
import tkinter as tk

# AUTOMÁÇÃO DE MENSAGENS NO INSTAGRAM

class BaixadorBot:
    def __init__(self, site, senha, pasta):
        self.site = site
        self.senha = senha
        self.pasta = pasta
        self.driver = webdriver.Edge(service=Service(r'.\venv\msedgedriver.exe'))

    # Logar no Instagram e entrar no perfil desejado
    def baixar(self):
        try:
            driver = self.driver
            driver.get(self.site)
            time.sleep(1)
            senha_element = driver.find_element(By.XPATH, '//input[@name="txtPassword"]')
            # senha_element.clear()
            senha_element.send_keys(self.senha)
            senha_element.send_keys(Keys.RETURN)
            time.sleep(1)
            
            # Escolher pasta desejada
            driver.find_element(By.XPATH, '//*[text()="' + self.pasta + '"]').click()
            time.sleep(2)
            
            # Baixar os arquivos na pasta
            driver.find_element(By.XPATH, '//button[@name="Baixar"]').click()
            time.sleep(30)
        
            downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
            os.startfile(downloads_path)
            
            
        except Exception as e:
            print(f'Ocorreu um erro: {e}')


def iniciar_baixador():
    iniciar = BaixadorBot(site_entrada, senha_entrada, nome_pasta_entrada)
    # iniciar.baixar()


# Janela do aplicativo
janela = tk.Tk()
janela.title("Baixador de Arquivos")
janela.geometry("500x400")
janela.configure(bg="#222")

titulo = tk.Label(janela, text="BAIXADOR DE ARQUIVOS - SHAREPOINT", font=("Arial", 16), fg="white", bg="#222")
titulo.pack(pady=10)

site_label = tk.Label(janela, text="Link da pasta compartilhada", fg="white", bg="#222")
site_label.pack()

site_entrada = tk.Entry(janela, fg="white", bg="#222")
site_entrada.pack()

senha_label = tk.Label(janela, text="Senha da pasta", fg="white", bg="#222")
senha_label.pack()

senha_entrada = tk.Entry(janela, fg="white", bg="#222")
senha_entrada.pack()

nome_pasta_label = tk.Label(janela, text="Nome da pasta", fg="white", bg="#222")
nome_pasta_label.pack()

nome_pasta_entrada = tk.Entry(janela, fg="white", bg="#222")
nome_pasta_entrada.pack()

botao_enviar = tk.Button(janela, text="Iniciar Processo", command=iniciar_baixador)
botao_enviar.pack()

creditos = tk.Label(janela, text="Desenvolvido por Eric Cabral", fg="white", bg="#222")
creditos.pack(pady=5)

janela.mainloop()
