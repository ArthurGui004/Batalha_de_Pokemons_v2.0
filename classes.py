from random import randint
from cores import cor

class Pokemon:
    def __init__(self):
        self.nome = None
        self.vida = randint(100, 150)
        self.ataques = [randint(30, 50) for x in range(4)]
        self.resistencia = randint(0, 30)
        self.elemento = None
        self.cor = None

    def atacar(self, rival):
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
                reducao_dmg = self.ataques[escolhido] - rival.resistencia
                if reducao_dmg > 0:
                    return reducao_dmg
                return 0

                

class Tipo_Agua(Pokemon):
    def __init__(self):
        super().__init__()
        self.nome = 'Squid Turtle'
        self.elemento = f'agua'
        self.cor = cor('azul claro')

    def definir_relacao(self, rival: Pokemon):
        if rival.elemento == 'fogo':
            for index in range(len(self.ataques)):
                self.ataques[index] *= 2
            print(f'O {self.nome} tem vantagem nessa luta')

        elif rival.elemento == 'eletrico':
            for index in range(len(self.ataques)):
                self.ataques[index] *= 0.5
            print(f'O {self.nome} tem desvantagem nessa luta')

        else:
            print(f'Luta Justa!')


class Tipo_Fogo(Pokemon):
    def __init__(self):
        super().__init__()
        self.nome = 'Xamandi'
        self.elemento = 'fogo'
        self.cor = cor('vermelho')

    def definir_relacao(self, rival: Pokemon):
        if rival.elemento == 'terra':
            for index in range(len(self.ataques)):
                self.ataques[index] *= 2
            print(f'O {self.nome} tem vantagem nessa luta')

        elif rival.elemento == 'agua':
            for index in range(len(self.ataques)):
                self.ataques[index] *= 0.5
            print(f'O {self.nome} tem desvantagem nessa luta')

        else:
            print(f'Luta Justa!')



class Tipo_Terra(Pokemon):
    def __init__(self):
        super().__init__()
        self.nome = 'Bombasal'
        self.elemento = 'terra'
        self.cor = cor('verde')

    def definir_relacao(self, rival: Pokemon):
        if rival.elemento == 'eletrico':
            for index in range(len(self.ataques)):
                self.ataques[index] *= 2
            print(f'O {self.nome} tem vantagem nessa luta')

        elif rival.elemento == 'fogo':
            for index in range(len(self.ataques)):
                self.ataques[index] *= 0.5
            print(f'O {self.nome} tem desvantagem nessa luta')

        else:
            print(f'Luta Justa!')



class Tipo_Eletrico(Pokemon):
    def __init__(self):
        super().__init__()
        self.nome = 'Shokito'
        self.elemento = 'eletrico'
        self.cor = cor('amarelo')

    def definir_relacao(self, rival: Pokemon):
        if rival.elemento == 'agua':
            for index in range(len(self.ataques)):
                self.ataques[index] *= 2
            print(f'O {self.nome} tem vantagem nessa luta')

        elif rival.elemento == 'terra':
            for index in range(len(self.ataques)):
                self.ataques[index] *= 0.5
            print(f'O {self.nome} tem desvantagem nessa luta')
            
        else:
            print(f'Luta Justa!')
