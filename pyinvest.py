'''
Integrantes do Grupo:
Lucas Notargiacomo Mustaro - RA: 10434914
Matheus Otsuka Trovo de Carvalho - RA: 10776358
Pedro Henrique Bettega Trama - RA: 10769933

Turma 01D - L12
'''

import math
import locale
from datetime import date


def exibe_mensagem(): #exibe a mensagem do programa
    return "==================== PYINVEST ===================="


# calcula o valor total investido
def total_investido(capital, aporte, meses):
    return capital + (aporte * meses)

# converte a taxa anual em taxa mensal composta
def converter_taxa(porcentagem_cdi):
    cdi_mensal = math.pow(1 + (porcentagem_cdi / 100), (1 / 12)) - 1
    return cdi_mensal


# calcula a poupança considerando rendimento fixo de 0,5% ao mês aplicando juros compostos
def calcular_poupanca(capital, aporte,  prazo):
    valor_inicial = capital * math.pow((1 + 0.005), prazo)
    valor_aporte = aporte * (math.pow((1 + 0.005), prazo) - 1) / 0.005
    poupanca = valor_inicial + valor_aporte
    return poupanca


# formatação dos valores monetários no padrão brasileiro
def formatacao_monetaria(valor):
    locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')
    formatado = locale.currency(valor, grouping=True)
    return formatado

def data_atual(): # obtém a data atual
    data = date.today()
    data_atual = data.strftime("%d/%m/%Y")
    return data_atual


# função principal do programa
def main():
    print(exibe_mensagem())
    capital_inicial = float(input("Capital Inicial (R$): "))
    aporte = int(input("Aporte Mensal (R$): "))
    prazo_investimento = int(input("Prazo (meses): "))
    cdi_anual = int(input("CDI anual (%): "))

    cdi_mensal = converter_taxa(cdi_anual)

    poupanca = calcular_poupanca(capital_inicial, aporte, prazo_investimento)
    poupanca_formatada = formatacao_monetaria(poupanca) # valor da poupança formatada
    total = total_investido(capital_inicial, aporte, prazo_investimento)
    total_formatado = formatacao_monetaria(total) # valor total formatado

    print(f"RELATÓRIO PYINVEST - {data_atual()}")
    print(f"Poupança: {poupanca_formatada}")
    print(f"Total investido: {total_formatado}")


main() # chamada para a função principal