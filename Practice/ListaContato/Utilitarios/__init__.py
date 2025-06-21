def titulo(msg):
    tam = (len(msg) + 6)
    print('—' * tam)
    print(f'   {msg}')
    print('—' * tam)


def chkint(msg):
    ok = False
    valor = 0
    while True:
        try:
            num = int(input(msg))
        except:
            print('ERRO! digite o numero da opção!')
        else:
            valor = int(num)
            ok = True
        if ok:
            break
    return valor


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for contato in lista:
        print(f'{c} - {contato}')
        c += 1
    print('—' * 30)
    opc = chkint('selecione uma opção. ')
    while opc < 1 or opc > len(lista):
        print('digite um número válido!')
        opc = chkint('selecione uma opção. ')
    return opc


def abrir_lista(nome):
    try:
        l = open(nome, 'rt')
    except:
        print(f'Erro ao abrir o arquivo.')
    else:
        titulo('CONTATOS SALVOS')
        for linha in l:
            dados = linha.strip(). split(',')
            if len(dados) == 3:
                print(f'Nome: {dados[0]}')
                print(f'Telefone: {dados[1]}')
                print(f'E-mail: {dados[2]}')
                print('—' * 30)


def cadastrar(arq, nome='desconhecido', tel='não tem', mail='não tem'):
    try:
        a = open(arq, 'at')
    except Exception as erro:
        print(f'houve um {erro.__class__} na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}, {tel}, {mail}\n')
        except:
            print('houve um erro ao escrever no arquivo!')
        else:
            print(f'novo contato de {nome} adicionado!')
            a.close()
