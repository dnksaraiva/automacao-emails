# importando as bibliotecas necessárias
import yagmail
from datetime import datetime

# listar endereços de email que irão receber a mensagem

lista =[('teste', 'teste@gmail.com,' '24/11') ]

# verificar data atual

hoje = datetime.now().strftime('%d/%m')
print(hoje)    #verificamos que o formato da data está igual ao da lista criada

# comparar a data atual/desejada com as datas na lista de quem irá receber a mensagem

emailServer = yagmail.SMTP ('emailEnvia@gmail.com', 'senha')
for nome in lista:
    if nome[2] == hoje:
        emailServer.send(nome[1], subject = 'Assunto do Email', contents = 'Corpo do Email')