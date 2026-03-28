'''
Integrantes do Grupo:
Lucas Notargiacomo Mustaro - RA: 10434914
Matheus Otsuka Trovo de Carvalho - RA: 10776358
Pedro Henrique Bettega Trama - RA: 10769933

Turma 01D - L12
'''

import math
import locale


def exibe_mensagem(): #exibe a mensagem do programa
    return "==================== PYINVEST ===================="


# calcula o valor total investido
def total_investido(capital, aporte, meses):
    return capital + (aporte * meses)


# calcula a poupança considerando rendimento fixo de 0,5% ao mês aplicando juros compostos
def calcular_poupanca(capital, prazo_investimento):
    poupanca = capital * math.pow((1 + 0.005), prazo_investimento)
    return poupanca


# formatação dos valores monetários no padrão brasileiro
def formatacao_monetaria(valor):
    locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')
    formatado = locale.currency(valor, grouping=True)
    return formatado


 # função principal do programa
def main():
    print(exibe_mensagem())
    capital_inicial = float(input("Capital Inicial (R$): "))
    aporte = int(input("Aporte Mensal (R$): "))
    prazo_investimento = int(input("Prazo (meses): "))


    resultado = calcular_poupanca(capital_inicial, prazo_investimento)
    valor_formatado = formatacao_monetaria(resultado) # valor da poupança formatado
    total = total_investido(capital_inicial, aporte, prazo_investimento)
    total_formatado = formatacao_monetaria(total) # valor total formatado


    print(f"Poupança: {valor_formatado}")
    print(f"Total investido: {total_formatado}")


main() # chamada para a função principal