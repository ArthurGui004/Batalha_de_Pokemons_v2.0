from classes import *

def info_pokemon(pokemon1: Pokemon, pokemon2: Pokemon):
    print()
    print('='*45)
    print(f'DADOS DOS POKEMONS'.center(45))
    print(f'{str(pokemon1.nome).upper():<20} VS {str(pokemon2.nome).upper():>18}')
    print('='*45)
    
    print(f'Vida: {pokemon1.vida} HP                     Vida: {pokemon2.vida} HP')
    print(f'\nResis: {pokemon1.resistencia}                        Resis: {pokemon2.resistencia}')
    print(f'\nElemento: {pokemon1.elemento}              Elemento: {pokemon2.elemento}')

def introducao():
    print('''
Bem Vindo ao RINHA DE POKÉMONS!

Este é um jogo criado por Arthur e inspirado na franquia de Pokémon.
O jogo é uma versão de terminal onde o usuário aposta dinheiro fictício 
com os amigos para ver qual pokémon vence a batalha. Aproveite o conteúdo!

Créditos:
Progamação do game: Arthur
    ''')
    print('='*30)
    print('ESCOLHA O POKEMON'.center(30))
    print('='*30)

    print(f'''
    1- {cor("vermelho")}Xamãder {cor("normal")}
    2- {cor("verde")}Bombasal {cor("normal")}
    3- {cor("azul claro")}Squid Turtle {cor("normal")}
    4- {cor("amarelo")}Shokito {cor("normal")}
          ''')