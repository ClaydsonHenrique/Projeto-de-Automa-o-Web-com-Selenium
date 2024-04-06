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
