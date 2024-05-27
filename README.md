Projeto de Automação Web com Selenium

Este projeto é um exemplo de automação web utilizando a biblioteca Selenium no Python. O script abre uma página da web, insere um email e uma senha em campos de login, aguarda alguns segundos e fecha o navegador.
Requisitos

    Python 3.x
    Selenium
    Google Chrome
    WebDriver do Chrome

Instalação

    Instalar o Python 3.x:

    Verifique se você tem o Python instalado no seu sistema. Você pode baixar o Python aqui.

    Instalar o Selenium:

    Para instalar a biblioteca Selenium, execute o seguinte comando no seu terminal:

    bash

    pip install selenium

    Instalar o WebDriver do Chrome:

    Faça o download do WebDriver do Chrome compatível com a versão do seu navegador aqui.

    Depois de baixar, extraia o executável e coloque-o em um diretório acessível pelo PATH do sistema.

Uso

    Configurar o script:

    Crie um arquivo Python (por exemplo, automacao.py) e adicione o seguinte código:

    python

from selenium import webdriver
import time

navegation = webdriver.Chrome()
url = "https://www.origamid.com/conta/"

navegation.get(url)

userEmail = navegation.find_element("xpath", '//*[@id="log"]').send_keys(
    "email@teste.com"
)

userPassword = navegation.find_element("xpath", '//*[(@id="pwd")]').send_keys(
    "NovaSenha"
)

time.sleep(15)

navegation.quit()

Executar o script:

Execute o script Python usando o terminal:

bash

    python automacao.py

    O script irá:
        Abrir o navegador Google Chrome.
        Navegar para a página de login especificada.
        Inserir o email "email@teste.com" no campo de email.
        Inserir a senha "NovaSenha" no campo de senha.
        Aguardar 15 segundos.
        Fechar o navegador.

Observações

    Certifique-se de que o WebDriver do Chrome está no PATH do seu sistema ou forneça o caminho completo para o executável ao criar a instância do WebDriver:

    python

    navegation = webdriver.Chrome(executable_path='/caminho/para/chromedriver')

    Ajuste os seletores XPath se a estrutura HTML da página de login mudar.

    Modifique o tempo de espera (time.sleep) conforme necessário para o seu caso de uso.

