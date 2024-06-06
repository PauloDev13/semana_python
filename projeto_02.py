import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

try:
    # Solicita o código da ação da empresa que terá a cotação consultada
    ticker = input('Informe o código da ação desejada: ')

    # Solicita a data inicial e final para consultar a cotação das ações.
    # O formado da data deve ser 'yyyy-MM-dd'
    str_inital_date = input('Informe a data inicial no formato yyyy-mm-dd: ')
    str_final_date = input('Informe a data final no formato yyyy-mm-dd: ')

    # Usa a bliblioteca yfinance para acessar o serviço yahoo finance
    # e busca a tabela de cotações no período informado
    dados = (yfinance.Ticker(ticker).history(start=f'{str_inital_date}', end=f'{str_final_date}'))

    # Coleta os dados somente da coluna Close da tabela
    fechamento = dados.Close

    # Atribui as variáveis maxima, minima e valor_médio as cotações em R$ do período
    # formatado com duas casas decimais
    maxima = round(fechamento.max(), 2)
    minima = round(fechamento.min(), 2)
    valor_medio = round(fechamento.mean(), 2)

    # Imprime os valores das cotações
    print(maxima)
    print(minima)
    print(valor_medio)

    # Solicita a confirmação para envio do email
    str_enviar = input('Enviar dados para o email? (s para Sim ou n para Não): ')

    # Se sim, solicita o email, o assunto e formata a mensagem que será enviada
    if str_enviar == 's':
        str_destinatario = input('Informe o e-mail: ')
        str_assunto = f'Análise ações da {ticker}'
        str_mensagem = f'''
            Prezado Gestor,
            
            Seguem as análises solicitadas na ação {ticker},
            no período de {str_inital_date} a {str_final_date}.
            
            Cotação máxima: R${maxima}
            Contação mínima: R${minima}
            Valor médio: R${valor_medio}
            
            Atenciosamente,
            PR
            '''
        # Abre o navegador na aba do gmail
        webbrowser.open('www.gmail.com')
        # Espera 3 segundos
        time.sleep(3)
        pyautogui.PAUSE = 2

        # Clica no botão Escreve na tela do gmail
        pyautogui.click(-1514, 263)

        # Copia o valor da variável destinatário, cola seu conteúdo no campo
        # e pressiona a tecla TAB
        pyperclip.copy(str_destinatario)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('tab')

        # Copia o valor da variável assunto, cola seu conteúdo no campo
        # e pressiona a tecla TAB
        pyperclip.copy(str_assunto)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('tab')

        # Copia o valor da variável mensagem, cola seu conteúdo no campo
        # e pressiona a tecla TAB
        pyperclip.copy(str_mensagem)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('tab')

        # Clica no botão enviar
        pyautogui.click(x=-585, y=861)

        # Espera 3 segundos e fecha a janela do gmail no navegado
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'f4')

        # Exibe mensagem de sucesso
        print('Envio concluído com sucesso!')
    else:
        # Se não, exibe mensagem de cancelamento do envio do email
        print('Envio cancelado!')
except:
    # Se aconteceu alguma exceção durante o processo, exibe mensagem de erro
    print('Ocorreu um erro. Tente novamente.')




