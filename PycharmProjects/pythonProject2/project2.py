import pandas as pd
import smtplib
import email.message

tabela_vendas = pd.read_excel("Vendas.xlsx")
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})


def enviar_email():
    corpo_email = f"""
    <p>Prezados,</p>
    
    
    <p>Segue o relatório de vendas de cada loja.</p>

    <p>Faturamento:</p>
    {faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}
    <p>Quantidade vendida:</p>
    {quantidade.to_html()}
    <p>Ticket médio dos produtos em cada loja:</p>
    {ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}
    
    <p>Qualquer dúvida estou à disposição.</p>
    
    <p>Abs</p>
    <p>Leonardo Moura</p>
    
    """

    msg = email.message.Message()
    msg['Subject'] = 'Relatório das Lojas'
    msg['From'] = 'lekomoura19@gmail.com'
    msg['To'] = 'valmoura29@gmail.com'
    password = 'GetJinxed006'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
enviar_email()