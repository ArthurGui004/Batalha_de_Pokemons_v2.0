from __future__ import annotations
from random import randint
from cores import cor

class Pokemon:
    '''Modela todos os Tipos de pokémons.'''
    def __init__(self):
        '''Método construtor.'''
        self.nome = None
        self.vida = randint(100, 150)
        self.vida_max = self.vida
        self.ataques = [randint(30, 50) for x in range(4)]
        self.resistencia = randint(0, 30)
        self.bloqueio = False
        self.elemento = None
        self.cor = None

    def atacar(self, rival: Pokemon, bloqueio: bool) -> int:
        '''Função para o pokémon atacar.
        
        Parâmetros:
            rival -> Pokémon adversário
            bloqueio -> True se o adversário estiver bloqueando, False se o adversário não estiver bloqueando
        
        Retorna o dano advindo do ataque realizado pelo pokémon
        '''
        self.bloqueio = False
        print('='*30)
        print(f'Lista de ataques {self.nome}:'.center(30))
        print('='*30)
        print(f'''
    1. {self.ataques[0]:.2f} de dano
    2. {self.ataques[1]:.2f} de dano
    3. {self.ataques[2]:.2f} de dano
    4. {self.ataques[3]:.2f} de dano
        ''')
        while True:
            escolhido = (int(input(f'Escolha o ataque do {self.nome}: '))-1)
            if escolhido < 0 or escolhido > 4:
                print('ERRO! Digite um número válido.')
            else:
                if bloqueio:
                    reducao_dmg = self.ataques[escolhido] - rival.bloquear()
                    if reducao_dmg > 0:
                        return reducao_dmg
                    return 0

                else:
                    reducao_dmg = self.ataques[escolhido] - rival.resistencia
                    if reducao_dmg > 0:
                        return reducao_dmg
                    return 0
    
    def bloquear(self) -> int:
        '''Função para o pokémon bloquear.
        
        Retorna o dobro da resistência do pokémon
        '''
        self.bloqueio = True
        return self.resistencia * 2
    
    def curar(self) -> str | int:
        '''Função para o pokémon se curar.
        
        Retorna um inteiro correspondente ao quanto de vida o pokémon vai recuperar
        '''
        self.bloqueio = False
        if self.vida < self.vida_max:
            if (self.vida+20) > self.vida_max:
                self.vida = self.vida_max
                print(f'Curado {self.vida_max-self.vida} de HP')
            else:
                self.vida += 20
                print('Curado 20 de HP')
        else:
            print('Sua vida está cheia!')

    def agir(self) -> int:
        '''Função para escolher o que o pokémon vai fazer.
        
        Retorna o número escolhido
        '''
        print('''
1- Atacar
2- Bloquear
3- Se Curar''')
        while True:
            escolha = int(input('Sua escolha: '))
            if escolha < 0 or escolha > 3:
                print("Erro. Escolha um número que esteja no menu.")
            else:
                return escolha

                

class Tipo_Agua(Pokemon):
    '''Modela o Tipos de pokémons Água.'''
    def __init__(self):
        super().__init__()
        '''Método construtor.'''
        self.nome = 'Squid Turtle'
        self.elemento = f'agua'
        self.cor = cor('azul claro')

    def definir_relacao(self, rival: Pokemon):
        '''Função que define a vantagem e desvantagem do pokémon em relação ao seu adversário.
        
        Parâmetros:
            rival -> Pokémon adversário'''
        if rival.elemento == 'fogo':
            self.ataques = [atk * 2 for atk in self.ataques]
            print(f'O {self.nome} tem vantagem nessa luta')

        elif rival.elemento == 'eletrico':
            self.ataques = [atk * 0.5 for atk in self.ataques]
            print(f'O {self.nome} tem desvantagem nessa luta')

        else:
            print(f'Luta Justa!')


class Tipo_Fogo(Pokemon):
    '''Modela o Tipos de pokémons fogo.'''
    def __init__(self):
        super().__init__()
        '''Método construtor.'''
        self.nome = 'Xamandi'
        self.elemento = 'fogo'
        self.cor = cor('vermelho')

    def definir_relacao(self, rival: Pokemon):
        '''Função que define a vantagem e desvantagem do pokémon em relação ao seu adversário.
        
        Parâmetros:
            rival -> Pokémon adversário'''
        if rival.elemento == 'terra':
            self.ataques = [atk * 2 for atk in self.ataques]
            print(f'O {self.nome} tem vantagem nessa luta')

        elif rival.elemento == 'agua':
            self.ataques = [atk * 0.5 for atk in self.ataques]
            print(f'O {self.nome} tem desvantagem nessa luta')

        else:
            print(f'Luta Justa!')



class Tipo_Terra(Pokemon):
    '''Modela o Tipos de pokémons terra.'''
    def __init__(self):
        super().__init__()
        '''Método construtor.'''
        self.nome = 'Bombasal'
        self.elemento = 'terra'
        self.cor = cor('verde')

    def definir_relacao(self, rival: Pokemon):
        '''Função que define a vantagem e desvantagem do pokémon em relação ao seu adversário.
        
        Parâmetros:
            rival -> Pokémon adversário'''
        if rival.elemento == 'eletrico':
            self.ataques = [atk * 2 for atk in self.ataques]
            print(f'O {self.nome} tem vantagem nessa luta')

        elif rival.elemento == 'fogo':
            self.ataques = [atk * 0.5 for atk in self.ataques]
            print(f'O {self.nome} tem desvantagem nessa luta')

        else:
            print(f'Luta Justa!')



class Tipo_Eletrico(Pokemon):
    '''Modela o Tipos de pokémons elétricos.'''
    def __init__(self):
        super().__init__()
        '''Método construtor.'''
        self.nome = 'Shokito'
        self.elemento = 'eletrico'
        self.cor = cor('amarelo')

    def definir_relacao(self, rival: Pokemon):
        '''Função que define a vantagem e desvantagem do pokémon em relação ao seu adversário.
        
        Parâmetros:
            rival -> Pokémon adversário'''
        if rival.elemento == 'agua':
            self.ataques = [atk * 2 for atk in self.ataques]
            print(f'O {self.nome} tem vantagem nessa luta')

        elif rival.elemento == 'terra':
            self.ataques = [atk * 0.5 for atk in self.ataques]
            print(f'O {self.nome} tem desvantagem nessa luta')
            
        else:
            print(f'Luta Justa!')
