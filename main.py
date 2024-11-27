# -*- coding: utf-8 -*-
import download_coff as d_coff
import subprocess

# Fun��o para exibir a sele��o do dashboard
def selecionar_dashboard():
    print("Selecione o dashboard desejado:")
    print("1 - EOLICA")
    print("2 - FOTOVOLTAICA")
    
    # Recebe a escolha do usu�rio
    escolha = input("Digite o numero correspondente ao dashboard desejado: ")

    return escolha

# Fun��o para executar o script com base na escolha do usu�rio
def executar_dashboard(escolha):
    if escolha == "1":
        print("Executando o dashboard de Constrained off das Usinas Eolicas...")
        # Executa o script appEOL.py (assumindo que o Python esteja instalado corretamente)
        subprocess.run(["python", "appEOL.py"])
    elif escolha == "2":
        print("Executando o dashboard Constrained off das Usinas Fotovoltaicas...")
        # Executa o script app.py
        subprocess.run(["python", "app.py"])
    else:
        print("Valor invalido. Tente novamente.")

# Fun��o principal que controla o fluxo
def inicio():
    escolha = selecionar_dashboard()  # Recebe a escolha do usu�rio
    executar_dashboard(escolha)  # Executa o dashboard com base na escolha

# Download do banco de dados
d_coff.download_files()  # Baixa os arquivos de coff de usinas fotovoltaicas
d_coff.download_filesEOL()  # Baixa os arquivos de coff de usinas e�licas

inicio()



