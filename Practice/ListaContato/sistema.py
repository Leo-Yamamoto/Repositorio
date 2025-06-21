from Utilitarios import *

arq = 'contatos.txt'
try:
    open('contatos.txt').close()
except FileNotFoundError:
    open('contatos.txt', 'at+').close()
    print('arquivo contatos foi criado.')
else:
    print(f'arquivo {arq} encontrado.')

while True:
    opt = menu(['Adicionar contato', 'apresentar contatos salvos', 'sair'])
    if opt == 1:
        titulo('NOVO CONTATO')
        nome = str(input('Nome: '))
        tel = str(input('Telefone: '))
        mail = str(input('E-mail: '))
        cadastrar(arq, nome, tel, mail)
    elif opt == 2:
        abrir_lista(arq)
    elif opt == 3:
        titulo('FINALIZADO')
        break
