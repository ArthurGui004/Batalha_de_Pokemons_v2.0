def cor(x):
    cores = {'normal' : '\033[m',
        'branco' : '\033[30m',
        'vermelho' :  '\033[31m',
        'verde' : '\033[32m',
        'amarelo': '\033[33m',
        'azul escuro' : '\033[34m',
        'roxo' : '\033[35m', 
        'azul claro' : '\033[36m',
        'cinza' : '\033[37m'}
    
    return cores[x]