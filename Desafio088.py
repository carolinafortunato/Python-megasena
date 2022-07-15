from random import randint
from time import sleep
lista = []
jogos = []
print('-'*30)
print('      JOGA NA MEGA SENA       ')
print('-'*30)
qt = int(input('Quantos jogos você quer gerar? '))
t = 1
while t <= qt:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    t += 1
print('-'*5, f'Sorteando {qt} jogos', '-'*5)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-'*5, '< BOA SORTE! >', '-'*5)
