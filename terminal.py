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
    print('='*30)
    print('ESCOLHA O POKEMON'.center(30))
    print('='*30)

    print(f'''
    1- {cor("vermelho")}Xamãder {cor("normal")}
    2- {cor("verde")}Bombasal {cor("normal")}
    3- {cor("azul claro")}Squid Turtle {cor("normal")}
    4- {cor("amarelo")}Shokito {cor("normal")}
          ''')