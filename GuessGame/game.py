from random import randint

cont = 0
comp = randint(1, 10)
while True:
    try:
        player = int(input('Vou pensar em um número de 1 a 10. Tente adivinhar! '))
        if player < 1 or player > 10:
            print('Escolha um número entre 1 a 10. ')
            continue
    except ValueError:
        print('Escolha um número válido!')
        continue        
    cont += 1
    if comp < player:
        print('Menos! Tente outra vez!')
    elif comp > player:
        print('Mais! Tente outra vez!')
    else:
        break
print(f'Parabéns! O número que pensei foi {comp}!\nVocê acertou em {cont} tentativas!\nAté a próxima!')
