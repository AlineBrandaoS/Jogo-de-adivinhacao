#jogo de adivinhação do exercicio 28 de python do professor Guanabara

from random import randint
from time import sleep

print('-=-' * 20)
numero = int(input('Adivinha o numero que estou pensando entre 0 a 5?'))

adivinho = randint(0, 5)

print('PROCESSANDO...')
sleep(2)

if numero == adivinho:
    print('Parabéns você me venceu!! :3 ')
else:
    print('GANHEI, eu pensei no numero {} e não no {}'.format(adivinho, numero))
print('-=-' * 20)
