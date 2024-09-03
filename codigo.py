# Bibliotecas usadas
    # # pip install pyautogui 
    # # pip install pandas numpy openpyxl

import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey

# aperta a tecla do windows

pyautogui.press('win')

# digita o nome do programa, para demonstração usar navegador

pyautogui.write('edge')

# aperta enter

pyautogui.press('enter')

# esperar 1 segundo

time.sleep(1)

# digitar o link

link = 'https://site-omega-bay.vercel.app/'
pyautogui.write(link)

# apertar enter

pyautogui.press('enter')

# esperar 5 segundos

time.sleep(1)

# Fazer login

pyautogui.click(x=1070, y=560)
pyautogui.write('emailcadastrado@gmail.com')
pyautogui.press('enter')
pyautogui.write('123')   
pyautogui.press('enter')

# Importar a base de dados 

tabela = pandas.read_csv('produtos.csv')

# Cadastrar um produto

for linha in tabela.index:
    pyautogui.click(x=1137, y=413)

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')
    
    if not pandas.isna(str(tabela.loc[linha, 'obs'])):
         pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)

# Repetir isso até acabar a base de dados
