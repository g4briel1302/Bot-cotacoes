import requests
import pandas as pd
from pandas_datareader import data as pdr
import datetime
import time

dia = datetime.date.today()
dia = dia.strftime("%m/%d/%Y")

token = "5730414137:AAGUKTpS5g3vNqm0pLsqqFNubsVy9FgVcM4"
chat_id = '-769961642'

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")#Request para saber os valores das moedas atuais
requisicao_dicionario = requisicao.json()

cotacao_oi = pd.DataFrame()
cotacao_oi = pdr.DataReader('OIBR3.SA', data_source='yahoo', start=f"{dia}",)
cotacao_deva = pd.DataFrame()
cotacao_deva = pdr.DataReader('DEVA11.SA', data_source='yahoo', start=f"{dia}",)
cotacao_quasar = pd.DataFrame()
cotacao_quasar = pdr.DataReader('QAMI11.SA', data_source='yahoo', start=f"{dia}",)


cotacaoDolar = float(requisicao_dicionario['USDBRL']['bid'])
cotacaoEuro = float(requisicao_dicionario['EURBRL']['bid'])
cotacaoBitcoin = float(requisicao_dicionario['BTCBRL']['bid'])


Texto_Principal = f''' 
--------------------------🚨Moedas🚨-----------------------------

Bom dia Gabriel, a cotação das moedas de interesses estao abaixo:

💲Dolar: $ {cotacaoDolar}
💶Euro: € {cotacaoEuro}
🪙Bitcoin BTC {cotacaoBitcoin}

--------------------------🚨Ativos🚨---------------------------
Seus ativos e seus fundos imobiliarios estao listados abaixo:

OIBR3(Açâo)

{cotacao_oi[['Open','Close']]}

Deva11(FILL)

{cotacao_deva[['Open','Close']]}

Quasar(FILL)

{cotacao_quasar[['Open','Close',]]}

'''
while True:
    Enviar_Mensagem = "https://api.telegram.org/bot5730414137:AAGUKTpS5g3vNqm0pLsqqFNubsVy9FgVcM4/sendMessage?chat_id=-769961642&text={}".format(Texto_Principal)
    requests.get(Enviar_Mensagem)
    time.sleep(43300)
