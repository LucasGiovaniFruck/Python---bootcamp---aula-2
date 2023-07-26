# Passo a passo do projeto

# pyautogui.write -> Escrever um texto
# pyautogui.press -> Apertar 1 tecla
# pyautogui.click -> Clicar em algum lugar da tela

# Passo 1: Entrar no sistema da empresa
import pyautogui
import time

pyautogui.PAUSE = 0.4
# Abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("Google")
pyautogui.press("enter")
pyautogui.click(x=605, y=456)

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(0.4)

# Passo 2: Fazer login

# Selecionar o campo de email
pyautogui.press("tab")
# Escrever seu email
pyautogui.write("Lucas.f.giovani@gmail.com")

# Escrever sua senha
pyautogui.press("tab")
pyautogui.write("123456789")

# CLicar em logar
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de produtos para cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    print(linha)
    # Clicar no campo de código
    pyautogui.click(x=639, y=243)
    # Pegar da tabela o valor do campo que a gente quer preencher 
    codigo = tabela.loc[linha, "codigo"]
    # Preencher o campo
    pyautogui.write(str(codigo))

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))

    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))

    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))

    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))

    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        obs = tabela.loc[linha, "obs"]
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    # Dar scroll pra cima
    pyautogui.scroll(5000)  


    # Passo 5: Repetir o processo de cadastro até o fim

