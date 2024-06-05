# importa a biblioteca fpdf
from fpdf import FPDF


try:
    # Coleta os dados informados pelo usuário
    str_projeto = input('Digite o nome do projeto: ')
    str_horas_previstas = input('Digite o nome do horas previstas: ')
    str_valor_hora = input('Digite o valor da hora: ')
    str_prazo = input('Digite o nome do prazo: ')
    int_valor_Total = int(str_horas_previstas) * float(str_valor_hora)

    # Instancia um objeto PDF
    arq_pdf = FPDF()
    # Adiciona uma página
    arq_pdf.add_page()
    # Define fonte e tamanho
    arq_pdf.set_font('Arial', '', 11)
    # Seta o template.png como background do arquivo PDF
    arq_pdf.image('template.png')

    # Define coordenadas X, Y onde será impresso dos valores digitados"
    arq_pdf.text(115, 145, str_projeto)
    arq_pdf.text(115, 160, str_horas_previstas)
    arq_pdf.text(115, 175, str_valor_hora)
    arq_pdf.text(115, 190, str_prazo)
    arq_pdf.text(115, 205, str(int_valor_Total))

    # Gera o arquivo PDF
    arq_pdf.output('Orçamento.pdf')

    # Exibe mensagem de sucesso
    print('Orçamento gerado com sucesso!')
except ValueError:
    # Exibe mensagem de erro
    print('Ocorreu um erro ao gerar o PDF')
finally:
    # Fecha a instância do objeto arq_Pdf
    arq_pdf.close()