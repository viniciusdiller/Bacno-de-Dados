#   pyautogui.click     #cliclar com o mouse 
#   pyautogui.write     # escrever um texto
#   pyautogui.press     # apertar a tecla (como o "enter")
#   pyautogui.hotkey     # combinação de teclas (Crtl+ C)
#   pyautogui.scroll     # rolar a tela para cima ou para baixo

import pyautogui
import time 
import pandas #TRABALHAR COM BASE DE DADOS ( os produtos )
#passo 1
pyautogui.PAUSE = 0.5    # A CADA COMANDO DO CÓDIGO VAI DEMORAR ESSE TEMPO
#abrir no navegador
pyautogui.press("win")
pyautogui.write("Chrome")
time.sleep(0.7)
pyautogui.press("enter")
pyautogui.write("http://127.0.0.1:5500/Banco%20de%20Dados.html")
pyautogui.press("enter")

#entrar no site
time.sleep(1)          # SOMENTE NESSE PASSO DO CÓDIGO
#entrou no site, clica e bota o emailzinho
pyautogui.click(x=689, y=406)
pyautogui.hotkey("ctrl, a")
pyautogui.write("usuariofictício@hotmail.com")
pyautogui.press("tab")
pyautogui.write("vivizinhoo")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)
#TEMPINHO PARA IR PARA A OUTRA PÁGINA


#tabela é uma VARIÁVEL
tabela = pandas.read_csv("produtos.csv")

print(tabela)

#para cada linha da minha tabela
for linha in tabela.index:

    # CADASTRAR O PRODUTO 
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.click(x=676, y=296)
    pyautogui.write(codigo)

    #marca 
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)
    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)
    #preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)
    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)
    #obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs !="nan":
        pyautogui.write(obs)

    #clicar em enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
