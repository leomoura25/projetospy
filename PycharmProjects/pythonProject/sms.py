import pandas as pd
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "ACe57cac8280a1d64aac5e17ffd4580aca"
# Your Auth Token from twilio.com/console
auth_token = "57c1daedb23099958ae269d7e86d1656"
client = Client(account_sid, auth_token)

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} alguem bateu a meta. Vendedor: {vendedor} , Vendas: {vendas}")
        message = client.messages.create(
            to="+5521999565868",
            from_="+15075433521",
            body=f"No mês {mes} alguem bateu a meta. Vendedor: {vendedor} , Vendas: {vendas}")

        print(message.sid)