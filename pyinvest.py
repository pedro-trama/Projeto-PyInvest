'''
Integrantes do Grupo:
Lucas Notargiacomo Mustaro - RA: 10434914
Matheus Otsuka Trovo de Carvalho - RA: 10776358
Pedro Henrique Bettega Trama - RA: 10769933

Turma 01D - L12
'''

import math
import locale
from datetime import date, timedelta
import statistics
import random


def exibe_mensagem(): #exibe a mensagem do programa
    return "==================== PYINVEST ===================="

# função que calcula o valor total investido
def total_investido(capital, aporte, meses):
    return capital + (aporte * meses)

# função que converte a taxa do cdi anual em cdi mensal composta
def converter_taxa(porcentagem_cdi_anual):
    # converte o percentual para decimal
    cdi_decimal = porcentagem_cdi_anual / 100
    # Aplicando a fórmula: (1 + i_anual)^(1/12) - 1
    # math.pow(base, expoente) calcula a potência
    taxa_mensal = math.pow(1 + cdi_decimal, 1 / 12) - 1
    return taxa_mensal

# função que determina a alíquota do IR no CDB 
def determinar_imposto(prazo_dias):
    # Abaixo de 180 dias - 22.5%
    if prazo_dias <= 180:
        return 0.225
    # Entre 181 e 360 dias - 20%
    elif prazo_dias <= 360:
        return 0.2
    # Entre 361 e 720 dias - 17.5%
    elif prazo_dias <= 720:
        return 0.175
    # Acima de 720 dias - 15%
    else:
        return 0.15
    
# função que calcula o CDB
def calcular_cdb(capital, aporte ,prazo, cdi_anual, porcentagem_cdi_cdb):
    # converter CDI anual para mensal
    cdi_mensal = converter_taxa(cdi_anual) 

    # aplicar percentual de CDI ao CDB
    taxa_mensal_cdb = cdi_mensal * (porcentagem_cdi_cdb / 100)

    # saldo do capital inicial com juros compostos
    saldo_capital = capital * math.pow(1 + taxa_mensal_cdb, prazo)

    # saldo dos aportes mensais com juros compostos
    saldo_aportes = aporte * ((math.pow(1 + taxa_mensal_cdb, prazo) - 1) / taxa_mensal_cdb)

    # saldo total bruto do CDB
    saldo_cdb = saldo_capital + saldo_aportes

    # calcular lucro bruto
    valor_total_investido = total_investido(capital, aporte, prazo)
    lucro_cdb = saldo_cdb - valor_total_investido

    # determinar imposto baseado no prazo em dias
    prazo_dias = prazo * 30
    imposto_cdb = determinar_imposto(prazo_dias)

    # calcular o imposto de renda sobre o lucro
    imposto_renda = lucro_cdb * imposto_cdb

    # calcular o saldo líquido
    saldo_liquido_cdb = saldo_cdb - imposto_renda

    return saldo_liquido_cdb

# função que calcula a LCI aplicando juros compostos
def calcular_lci(capital, aporte, prazo, cdi_anual, porcentagem_cdi_lci):
    # converter CDI anual para mensal
    cdi_mensal = converter_taxa(cdi_anual)

    # aplicar percentual do CBD à LCI
    taxa_mensal_lci = cdi_mensal * (porcentagem_cdi_lci / 100)

    # saldo do capital em juros compostos
    saldo_capital = capital * math.pow((1 + taxa_mensal_lci), prazo)

    # saldo dos aportes 
    saldo_aportes = aporte * (math.pow((1 + taxa_mensal_lci), prazo) - 1) / taxa_mensal_lci

    # saldo total bruto do LCI
    saldo_lci = saldo_capital + saldo_aportes

    return saldo_lci

# função que calcula a poupança considerando rendimento fixo de 0,5% ao mês 
def calcular_poupanca(capital, aporte,  prazo):
    # saldo do capital em juros compostos
    saldo_inicial = capital * math.pow((1 + 0.005), prazo)

    # saldo dos aportes
    saldo_aportes = aporte * (math.pow((1 + 0.005), prazo) - 1) / 0.005

    # saldo total bruto da poupança
    saldo_poupanca = saldo_inicial + saldo_aportes
    return saldo_poupanca

# função que calcula a FII com simulação de risco
def calcular_fii_simulacao(capital, aporte, prazo, rentabilidade_fii):
    # função que calcula o saldo de uma simulação individual do FII
    def calcular_saldo_fii_unico(variacao_aleatoria):
        taxa_mensal = (rentabilidade_fii / 100) + (variacao_aleatoria / 100)

        saldo_capital = capital * math.pow(1 + taxa_mensal, prazo)
        saldo_aportes = aporte * ((math.pow(1 + taxa_mensal, prazo) -1 ) / taxa_mensal)

        return saldo_capital + saldo_aportes
    # gera 5 variações aleatórias com map()
    variacoes = list(map(lambda x: random.uniform(-3, 3), range(5)))

    # calcula os saldos com map()
    simulacoes = list(map(calcular_saldo_fii_unico, variacoes))
    
    return simulacoes

# função que retorna os valores das simulações (mediana, média, desvio padrão)
def analisar_fii(simulacoes):
    return{
        "media": statistics.mean(simulacoes),
        "mediana": statistics.median(simulacoes),
        "desvio_padrao": statistics.stdev(simulacoes)
    }

# formatação dos valores monetários no padrão brasileiro
def formatacao_monetaria(valor):
    locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')
    formatado = locale.currency(valor, grouping=True)
    return formatado

def data_atual(): # obtém a data atual
    data = date.today()
    data_atual = data.strftime("%d/%m/%Y")
    return data_atual

def data_resgate(meses): # obtém a data de resgate considerando 30 dias por mês
    data_atual = date.today()
    dias = meses * 30
    data_estimada_resgate = data_atual + timedelta(days=dias)
    return data_estimada_resgate


# função principal do programa
def main():
    print(exibe_mensagem())

    # entrada de dados
    capital_inicial = float(input("Capital Inicial (R$): "))
    aporte = int(input("Aporte Mensal (R$): "))
    prazo_investimento = int(input("Prazo (meses): "))
    cdi_anual = float(input("CDI anual (%): "))
    percentual_cdb = float(input("Percentual CDI na CDB (%): "))
    percentual_lci = float(input("Percentual CDI na LCI (%): "))
    rentabilidade_fii = float(input("Rentabilidade FII (%): "))
    meta_financeira = float(input("Meta Financeira (R$): "))

    # processamento dos dados

    # conversão da taxa CDI mensal para taxa anual
    cdi_mensal = converter_taxa(cdi_anual) 

    # cálculo do valor total investido
    valor_total = total_investido(capital_inicial, aporte, prazo_investimento)
    # valor total formatado 
    total_formatado = formatacao_monetaria(valor_total) 

    # obtenção da data estimada de resgate
    data_estimada_resgate = data_resgate(prazo_investimento)

    # cálculo do CDB
    valor_cdb = calcular_cdb(capital_inicial, aporte, prazo_investimento, cdi_anual, percentual_cdb)
    # valor do CDB formatado
    cdb_formatado = formatacao_monetaria(valor_cdb)

    # cálculo da LCI
    valor_lci = calcular_lci(capital_inicial, aporte, prazo_investimento, cdi_anual, percentual_lci)
    # valor da LCI formatada
    lci_formatada = formatacao_monetaria(valor_lci) 

    # cálculo da poupança
    valor_poupanca = calcular_poupanca(capital_inicial, aporte, prazo_investimento)
    # valor da poupança formatada 
    poupanca_formatada = formatacao_monetaria(valor_poupanca) 

    # cálculo da fii (média estatística)
    simulacao = calcular_fii_simulacao(capital_inicial, aporte, prazo_investimento, rentabilidade_fii)
    valor_fii_media = analisar_fii(simulacoes)

    # saída dos dados

    # estrutura condicional que verifica se os valores do capital, aporte e prazo são negativos
    if capital_inicial < 0 or aporte < 0 or prazo_investimento < 0:
        print("ERRO! Insira apenas valores positivos.") # exibe mensagem de erro em caso positivo
    else:
        print("=" * 50)
        print(f"RELATÓRIO PYINVEST - {data_atual()}")
        print(f"Data estimada de resgate: {data_estimada_resgate.strftime("%d/%m/%Y")}")
        print(f"Total investido: {total_formatado}")
        print("-" * 50)
        print(f"CDB: {cdb_formatado}")
        print(f"LCI/LCA: {lci_formatada}")
        print(f"Poupança: {poupanca_formatada}")
    

main() # chamada para a função principal