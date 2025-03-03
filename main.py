from classes import *
from terminal import *
from arquivo import exibir_ranking, adicionar_ou_atualizar_usuario
from time import sleep
import os

def main():
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
    os.system('cls' if os.name == 'nt' else 'clear')
    print('HORA DE APOSTAR!!!')
    aposta = int(input('Quanto você quer apostar? (Só recebemos valores inteiros) -> '))
    player_1.definir_relacao(player_2)
    player_2.definir_relacao(player_1)

    while True:
        print('='*45)
        print('PLAYER 1 TURN'.center(45))
        print('='*45)
        info_pokemon(player_1, player_2)
        escolha_p1 = player_1.agir()
        match escolha_p1:
            case 1:
                ataque_p1 = player_1.atacar(player_2, player_2.bloqueio)
                player_2.vida -= ataque_p1
            case 2:
                player_1.bloquear()
                print(f'Sua resistência para o próximo ataque agora é {player_1.resistencia*2}')
            case 3:
                player_1.curar()

        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        if player_1.vida <= 0 or player_2.vida <= 0:
            break

        print('='*45)
        print('PLAYER 2 TURN'.center(45))
        print('='*45)
        info_pokemon(player_1, player_2)
        escolha_p2 = player_2.agir()
        match escolha_p2:
            case 1:
                ataque_p2 = player_2.atacar(player_1, player_1.bloqueio)
                player_1.vida -= ataque_p2
            case 2:
                player_2.bloquear()
                print(f'Sua resistência para o próximo ataque agora é {player_2.resistencia*2}')
            case 3:
                player_2.curar()

        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        if player_1.vida <= 0 or player_2.vida <= 0:
            break

    if player_1.vida <= 0:
        print('O player 2 ganhou!')
        print('Agora coloque seu nome para registramos sua vitória!')
        nome = str(input('Digite seu nome: '))
        adicionar_ou_atualizar_usuario(nome, aposta*2)
        exibir_ranking()

    else:
        print('O player 1 ganhou!')
        nome = str(input('Digite seu nome: '))
        adicionar_ou_atualizar_usuario(nome, aposta*2)
        exibir_ranking()
    
if __name__ == '__main__':
    main()
