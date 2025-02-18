from classes import *
from terminal import *
from time import sleep
from os import system

introducao()
for x in range(2):
    while True:
        lutador = int(input(f'Número do lutador {x+1}: '))
        if lutador < 0 or lutador > 4:
            print('Número inválido. Escolha um número que esteja no menu de escolha')
        else:
            break
    if x == 0:
        match lutador:
            case 1:
                player_1 = Tipo_Fogo()
            case 2:
                player_1 = Tipo_Terra()
            case 3:
                player_1 = Tipo_Agua()
            case 4: 
                player_1 = Tipo_Eletrico()
        print(f'Você escolheu o {player_1.cor}{player_1.nome}{cor("normal")}')   
    
    else:
        match lutador:
            case 1:
                player_2 = Tipo_Fogo()
            case 2:
                player_2 = Tipo_Terra()
            case 3:
                player_2 = Tipo_Agua()
            case 4: 
                player_2 = Tipo_Eletrico()
        print(f'Você escolheu o {player_2.cor}{player_2.nome}{cor("normal")}')   

sleep(2)
system('clear')
player_1.definir_relacao(player_2)
player_2.definir_relacao(player_1)

vitoria = False
while not vitoria:
    info_pokemon(player_1, player_2)
    ataque_p1 = player_1.atacar(player_2)

    sleep(2)
    system('clear')

    info_pokemon(player_1, player_2)
    ataque_p2 = player_2.atacar(player_1)

    player_2.vida -= ataque_p1
    player_1.vida -= ataque_p2

    sleep(2)
    system('clear')
    if player_1.vida < 0 or player_2.vida < 0:
        vitoria = True

if player_1.vida < 0:
    print('O player 2 ganhou!')
else:
    print('O player 1 ganhou!')
