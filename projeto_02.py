import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

ticker = input('Informe o código da ação desejada: ')

dados = yfinance.Ticker(ticker).history('2020-01-01', '2020-12-31')
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

print(maxima)
print(minima)
print(valor_medio)

destinatario = 'devpgm2020@gmail.com'
assunto = 'Análise do Projeto 2020'

mensagem = f'''
Prezado Gestor,

Seguem as análises solicitadas na ação {ticker}

Cotação máxima: {maxima}
Contação mínima: {minima}
Valor médio: {valor_medio}

Atencionamente,
PR
'''

webbrowser.open('www.gmail.com')
time.sleep(3)

pyautogui.PAUSE = 2

pyautogui.click(-1838, 222)

pyperclip.copy(destinatario)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')


pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')


pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

pyautogui.click(x=-616, y=1013)




