import tkinter as tk
from tkinter import ttk, filedialog
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
import wget
import requests
from bs4 import BeautifulSoup
import time
import os
import sys
import subprocess
import ssl
import certifi
import psutil
import threading

def Chrome(caminho_saida):
    # Baixa o instalador do Chrome usando wget
    url = 'https://raw.githubusercontent.com/Bot016/AppFetch/main/files/ChromeSetup.exe'
    filename = 'Chrome-installer.exe'
    caminho_arquivo = os.path.join(caminho_saida, filename)
    
    try:
        if url:
            wget.download(url, out=caminho_arquivo,bar=bar_progresso)
            porcentagem.set(int(0))
            janela.update()
            return 'Instalado'
        else:
            return 'Não instalado'
    except Exception as e:
        return 'Não instalado'    
    
def Firefox(caminho_saida):
    # Baixa o instalador do Firefox usando filtragem em HTML
    url = 'https://www.mozilla.org/pt-BR/firefox/new/'
    filename = 'Firefox-installer.exe'
    caminho_arquivo = os.path.join(caminho_saida, filename)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        download_link = soup.select_one('#protocol-nav-download-firefox a.download-link')
        
        if download_link and 'data-direct-link' in download_link.attrs:
            wget.download(download_link['data-direct-link'], out=caminho_arquivo, bar=bar_progresso)
            porcentagem.set(int(0))
            janela.update()
            return 'Instalado'
        else:
            return 'Não instalado'
    
    except Exception as e:
        return 'Não instalado'
    
def D7zip(caminho_saida):
    # Baixa o instalador do 7zip usando filtragem em html
    url = 'https://www.7-zip.org/download.html'
    filename = '7zip-installer.exe'
    caminho_arquivo = os.path.join(caminho_saida, filename)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        download_link = soup.find('a', href=True, string='Download')
        
        if download_link:
            installer_url = download_link['href']
            download_link = 'https://www.7-zip.org/' + installer_url
            wget.download(download_link, out=caminho_arquivo, bar=bar_progresso)
            porcentagem.set(int(0))
            janela.update()
            return 'Instalado'
        else:
            return 'Não instalado'
    
    except Exception as e:
        return 'Não instalado'

def Winrar(caminho_saida):
    # Baixa o instalador do Winrar usando filtragem em html
    url = 'https://www.win-rar.com/postdownload.html?&L=0'
    filename = 'Winrar-installer.exe'
    caminho_arquivo = os.path.join(caminho_saida, filename)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        download_link_noformat = soup.select_one('.postdownloadlink')['href']
        
        if download_link_noformat:
            download_link = 'https://www.win-rar.com/' + download_link_noformat
            wget.download(download_link, out=caminho_arquivo, bar=bar_progresso)
            porcentagem.set(int(0))
            janela.update()
            return 'Instalado'
        else:
            return 'Não instalado'
    
    except Exception as e:
        return 'Não instalado'

def Thunderbird(caminho_saida):
    # Baixa o instalador do Thunderbird usando filtragem em HTML
    url = 'https://www.thunderbird.net/pt-BR/'
    filename = 'Thunderbird-installer.exe'
    caminho_arquivo = os.path.join(caminho_saida, filename)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        download_link = soup.select_one('.download-link')
        
        if download_link:
            wget.download(download_link['href'], out=caminho_arquivo, bar=bar_progresso)
            porcentagem.set(int(0))
            janela.update()
            return 'Instalado'
        else:
            return 'Não instalado'
    
    except Exception as e:
        return 'Não instalado'
 
def Anydesk(caminho_saida):
    # Baixa o instalador do Anydesk usando a URL direta
    url = 'https://download.anydesk.com/AnyDesk.exe'
    filename = 'Anydesk-installer.exe'
    caminho_arquivo = os.path.join(caminho_saida, filename)
    
    try:
        if url:
            wget.download(url, out=caminho_arquivo, bar=bar_progresso)
            porcentagem.set(int(0))
            janela.update()
            return 'Instalado'
        else:
            return 'Não instalado'
    
    except Exception as e:
        return 'Não instalado'
   
def CCleaner(caminho_saida):
    # Baixa o instalador do CCleaner usando filtragem em HTML
    filename = 'CCleaner-installer.exe'
    caminho_arquivo = os.path.join(caminho_saida, filename)
    
    try:
        # Configurar as opções do navegador Microsoft Edge
        edge_options = Options()
        edge_options.use_chromium = True
        edge_options.add_argument('--enable-javascript') # Habilitar a execução do JavaScript
        edge_options.add_argument('--headless')  # Executar em modo headless (sem janela)
        edge_options.add_argument('--log-level=0')
        edge_options.add_argument('--disable-dev-shm-usage')
        edge_options.add_argument('--remote-debugging-port=0')
        edge_options.add_argument('---disable-back-forward-cache')
        edge_options.add_argument('--disable-features=BackForwardCache')
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Inicia o Microsoft Edge
        driver = webdriver.Edge(options=edge_options)

        # Acessa a página e espera ela carregar
        driver.get('https://www.ccleaner.com/pt-br/ccleaner/download/standard')
        time.sleep(5)
        html_pagina = driver.page_source
        driver.quit()
        
        soup = BeautifulSoup(html_pagina, 'html.parser')
        links = soup.find_all('a', {'data-qa-id': 'start-download-link'})
        for link in links:
            link_download = link.get('href')
        
        if link_download:
            wget.download(link_download, out=caminho_arquivo, bar=bar_progresso)
            porcentagem.set(int(0))
            janela.update()
            return 'Instalado'
        else:
            return 'Não instalado'
    
    except subprocess.CalledProcessError as e:
        return 'Não instalado'
    
    except requests.exceptions.RequestException as e:
        return 'Não instalado'
    
    except Exception as e:
        return 'Não instalado'
 
def Java(caminho_saida):

    # Baixa o instalador usando uma emulação do navegador para conseguir o código HTML
    filename = 'Java-installer.exe'
    caminho_arquivo = os.path.join(caminho_saida, filename)
    
    try:
        # Configurar as opções do navegador Microsoft Edge
        edge_options = Options()
        edge_options.use_chromium = True
        edge_options.add_argument('--enable-javascript') # Habilitar a execução do JavaScript
        edge_options.add_argument('--headless')  # Executar em modo headless (sem janela)
        edge_options.add_argument('--log-level=3')
        edge_options.add_argument('--disable-dev-shm-usage')
        edge_options.add_argument('--remote-debugging-port=0')
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Inicia o Microsoft Edge
        driver = webdriver.Edge(options=edge_options)

        # Acessa a página e espera ela carregar
        driver.get('https://www.java.com/pt-BR/download/manual.jsp')
        time.sleep(5)
        html_content = driver.page_source
        driver.quit()

        # Analisa o HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        html_content = soup.find('a', title="Fazer download do software Java para Windows On-line")['href']
        
        if html_content:
            wget.download(html_content, out=caminho_arquivo, bar=bar_progresso)
            porcentagem.set(int(0))
            janela.update()
            return 'Instalado'
        else:
            return 'Não instalado'
    
    except subprocess.CalledProcessError as e:
        return 'Não instalado'
    
    except requests.exceptions.RequestException as e:
        return 'Não instalado'
    
    except Exception as e:
        return 'Não instalado'

def Kasperskiantivirus(caminho_saida):
    # Baixa o instalador do Kaspersky usando wget
    url = 'https://raw.githubusercontent.com/Bot016/AppFetch/main/files/Ainvirus-Kasperski.exe'
    filename = 'Antivirus-installer.exe'
    caminho_arquivo = os.path.join(caminho_saida, filename)
    
    try:
        if url:
            wget.download(url, out=caminho_arquivo, bar=bar_progresso)
            porcentagem.set(int(0))
            janela.update()
            return 'Instalado'
        else:
            return 'Não instalado'
    
    except Exception as e:
        return 'Não instalado'

def Kasperskisallofiice(caminho_saida):
    # Baixa o instalador do Kaspersky Small Office usando wget
    url = 'https://raw.githubusercontent.com/Bot016/AppFetch/main/files/smalloffice.exe'
    filename = 'smalloffice-installer.exe'
    caminho_arquivo = os.path.join(caminho_saida, filename)
    
    try:
        if url:
            wget.download(url, out=caminho_arquivo, bar=bar_progresso)
            porcentagem.set(int(0))
            janela.update()
            return 'Instalado'
        else:
            return 'Não instalado'
    
    except Exception as e:
        return 'Não instalado'

def baixar_selecionar_pasta():
    instalado_label.config(text=" ", fg="white") 
    janela.geometry("320x463")
    janela.update()
    global caminho_saida
    caminho_saida = filedialog.askdirectory()
    if caminho_saida:
        download_thread = threading.Thread(target=baixar_aplicativos(caminho_saida))
        download_thread.start()
        
    else:
        return

def baixar_aplicativos(caminho_saida):
    baixar_botao ['state'] = 'disabled'
    janela.geometry("320x525")
    progress_bar.pack(after=instalado_label, pady=10)
    janela.update()
    instalado_label.config(text="Baixando...", fg="yellow") 
    janela.update()

    global nomes
    global variaveis_botao
    nomes = ["Google Chrome","Firefox","7zip","Winrar","Thunderbird","Anydesk","CCleaner","Java","Kasperski Antivírus", "Kasperski Small Office"]
    variaveis_botao = [chrome_var,firefox_var,zip_var,winrar_var,thunder_var,Anydesk_var,CCleaner_var,java_var, antivirus_var, smalloffice_var]
    funcao = [Chrome,Firefox,D7zip,Winrar,Thunderbird,Anydesk,CCleaner,Java, Kasperskiantivirus, Kasperskisallofiice]
    for nome, variaveis, funcao_D in zip(nomes, variaveis_botao, funcao):
        if variaveis.get() == 1:
            texto_baixando = nome + " baixando..."
            instalado_label.config(text=texto_baixando, fg="yellow")
            janela.update()
            install = funcao_D(caminho_saida)
            texto_nao = nome + " não baixado!"
            texto_sim = nome + " baixado!"
            if install == 'Não instalado':
                instalado_label.config(text=texto_nao, fg="red")
                janela.update()
            else:
                instalado_label.config(text=texto_sim, fg="green")
                janela.update()
            time.sleep(3)

    time.sleep(1)
    progress_bar.pack_forget() 
    instalado_label.config(text="Arquivos baixados!", fg="green") 
    janela.update()
    janela.geometry("320x525")
    baixar_botao ['state'] = 'enable'
    return

def bar_progresso(current, total, width=80):
    progresso = current / total
    porcentagem.set(int(progresso * 100))
    progress_bar['value'] = int(progresso * 100)
    janela.update()

def instalar_apks():
    instalar_botao['state'] = 'disabled'
    instalado_label.config(text="Iniciando instalação...", fg="yellow")
    janela.update()
    time.sleep(1)
    
    instalador = ['Chrome', 'Firefox', '7zip', 'Winrar', 'Thunderbird', 'Anydesk','CCleaner', 'Java', 'Antivirus', 'smalloffice']
    for nome, variaveis, instaladores in zip(nomes, variaveis_botao, instalador):
        if variaveis.get() == 1:
            nome_instalador = instaladores + '-installer.exe'
            caminho_instalar = os.path.join(caminho_saida, nome_instalador)
            processo_instalador = subprocess.Popen(caminho_instalar, shell=True)
            processo_instalador.wait()
            if os.path.exists(caminho_instalar):
                try:
                    os.remove(caminho_instalar)
                except PermissionError:
                    pass

            texto_instalador = nome + ' instalado!'
            instalado_label.config(text=texto_instalador, fg="green")
            janela.update()
    time.sleep(1)
    instalado_label.config(text="Instalação Concluída!", fg="green")
    janela.update()
    time.sleep(1)
    instalar_botao['state'] = 'enable'
    janela.destroy()

def on_antivirus_checkbox_changed():
    if antivirus_var.get() == 1:
        smalloffice_var.set(0)

def on_smalloffice_checkbox_changed():
    if smalloffice_var.get() == 1:
        antivirus_var.set(0)

# Desabilita o SLL das paginas
ssl._create_default_https_context = ssl._create_unverified_context

# Procura o icone no EXE   
root_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#icon_path = os.path.join(root_path, "icon.ico")

#Cria a janela principal
janela = tk.Tk()
janela.title("Aplicativos Padrões")
#janela.iconbitmap(icon_path)
janela.geometry("320x463")
janela.configure(bg="#242424")

# Variável para armazenar a porcentagem de progresso
porcentagem = tk.IntVar()

# Variável para armazenar o status do download
status = tk.StringVar()

# Definir estilo geral para os botões e caixas de seleção
style = ttk.Style()
style.configure('Custom.TCheckbutton', background='#242424', foreground='white', selectcolor='#242424', activebackground='#242424', highlightthickness=0, activeforeground='white', font=("Bahnschrift", 10))

style = ttk.Style()
style.configure("Custom.TButton", font=("Bahnschrift", 10), foreground="#242424", background="#242424", padding=-1)

# Título
title_label = tk.Label(janela, text="SELECIONE OS APLICATIVOS", font=("Bahnschrift", 17, "bold"), bg="#242424", fg="white")
title_label.pack(pady=10)

# Linha separadora
separator = tk.Frame(janela, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=10)

# Navegador
navegador_frame = tk.Frame(janela)
navegador_frame.configure(bg="#242424")
navegador_frame.pack(pady=5)

navegador_label = tk.Label(navegador_frame, text="NAVEGADORES", font=("Bahnschrift", 13), bg="#242424", fg="white")
navegador_label.pack(anchor='center', pady=2)

chrome_var = tk.IntVar()
chrome_checkbox = ttk.Checkbutton(navegador_frame, text="Chrome", variable=chrome_var, style='Custom.TCheckbutton', takefocus=False)
chrome_checkbox.pack(side=tk.LEFT)

firefox_var = tk.IntVar()
firefox_checkbox = ttk.Checkbutton(navegador_frame, text="Firefox", variable=firefox_var, style='Custom.TCheckbutton', takefocus=False)
firefox_checkbox.pack(side=tk.LEFT, padx=5)

# Linha separadora
separator = tk.Frame(janela, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=20, pady=5)

# Compressão
compressao_frame = tk.Frame(janela)
compressao_frame.configure(bg="#242424")
compressao_frame.pack(pady=5)

compressao_label = tk.Label(compressao_frame, text="COMPRESSÃO", font=("Bahnschrift", 13), bg="#242424", fg="white")
compressao_label.pack(anchor='center')  

zip_var = tk.IntVar()
zip_checkbox = ttk.Checkbutton(compressao_frame, text="7Zip", variable=zip_var, style='Custom.TCheckbutton', takefocus=False)
zip_checkbox.pack(side=tk.LEFT)

winrar_var = tk.IntVar()
winrar_checkbox = ttk.Checkbutton(compressao_frame, text="Winrar", variable=winrar_var, style='Custom.TCheckbutton', takefocus=False)
winrar_checkbox.pack(side=tk.LEFT, padx=5)

# Linha separadora
separator = tk.Frame(janela, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=20, pady=5)

# E-mail
email_frame = tk.Frame(janela)
email_frame.configure(bg="#242424")
email_frame.pack(pady=5)

compressao_label = tk.Label(email_frame, text="E-MAIL", font=("Bahnschrift", 13), bg="#242424", fg="white")
compressao_label.pack(anchor='center')

thunder_var = tk.IntVar()
thunder_checkbox = ttk.Checkbutton(email_frame, text="Thunderbird", variable=thunder_var, style='Custom.TCheckbutton', takefocus=False)
thunder_checkbox.pack(anchor='center')

# Linha separadora
separator = tk.Frame(janela, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=20, pady=5)

# Antivírus
antivirus_frame = tk.Frame(janela)
antivirus_frame.configure(bg="#242424")
antivirus_frame.pack(pady=5)

antivirus_label = tk.Label(antivirus_frame, text="KASPERSKI", font=("Bahnschrift", 13), bg="#242424", fg="white")
antivirus_label.pack(anchor='center')

antivirus_var = tk.IntVar()
antivirus_checkbox = ttk.Checkbutton(antivirus_frame, text="Aintivírus", variable=antivirus_var, style='Custom.TCheckbutton', takefocus=False, command=on_antivirus_checkbox_changed)
antivirus_checkbox.pack(side=tk.LEFT, padx=5)

smalloffice_var = tk.IntVar()
smalloffice_checkbox = ttk.Checkbutton(antivirus_frame, text="Small Officce", variable=smalloffice_var, style='Custom.TCheckbutton', takefocus=False, command=on_smalloffice_checkbox_changed)
smalloffice_checkbox.pack(side=tk.LEFT, padx=5)

# Linha separadora
separator = tk.Frame(janela, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=20, pady=5)

# Outros
outros_frame = tk.Frame(janela)
outros_frame.configure(bg="#242424")
outros_frame.pack(pady=5)

outros_label = tk.Label(outros_frame, text="MAIS", font=("Bahnschrift", 13), bg="#242424", fg="white")
outros_label.pack(anchor='center')

Anydesk_var = tk.IntVar()
Anydesk_checkbox = ttk.Checkbutton(outros_frame, text="Anydesk", variable=Anydesk_var, style='Custom.TCheckbutton', takefocus=False)
Anydesk_checkbox.pack(side=tk.LEFT, padx=5)

CCleaner_var = tk.IntVar()
CCleaner_checkbox = ttk.Checkbutton(outros_frame, text="CCleaner", variable=CCleaner_var, style='Custom.TCheckbutton', takefocus=False)
CCleaner_checkbox.pack(side=tk.LEFT, padx=5)

java_var = tk.IntVar()
java_checkbox = ttk.Checkbutton(outros_frame, text="Java 8", variable=java_var, style='Custom.TCheckbutton', takefocus=False)
java_checkbox.pack(side=tk.LEFT, padx=5)

# Linha separadora
separator = tk.Frame(janela, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=20, pady=5)

# Botão Instalar
baixar_botao = ttk.Button(janela, text="BAIXAR APLICATIVOS", style="Custom.TButton", takefocus=False, command=baixar_selecionar_pasta)
baixar_botao.pack(anchor='center', pady=10)

instalado_label = tk.Label(janela, text=" ", font=("Bahnschrift", 12), bg="#242424", fg="white")
instalado_label.pack(anchor='center')

# Barra de progresso
progress_bar = ttk.Progressbar(janela, length=300, variable=porcentagem, takefocus=False)
progress_bar.pack(pady=10)

instalar_botao = ttk.Button(janela, text="INSTALAR APLICATIVOS", takefocus=False, style="Custom.TButton", command=instalar_apks)
instalar_botao.pack(anchor='center', pady=10)

janela.mainloop()