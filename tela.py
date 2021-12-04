
def parte_de_cima(*args):
    for p, texto in enumerate(args):
        print('+', end='')

        if p == len(args) - 1:
            print(' - ' * len(texto), end='')
            print('+')
        else:
            print(' - ' * len(texto), end='')


def conteudo(*args):
    for p, texto in enumerate(args):
        print('|', end='')

        if p == len(args) - 1:
            print(f'{texto.center(len(texto) * 3)}', end='')
            print('|')
        else:
            print(f'{texto.center(len(texto) * 3)}', end='')


def linha(*args):
    parte_de_cima(*args)
    conteudo(*args)
    parte_de_cima(*args)


def menu(*args):
    parte_de_cima(*args)
    conteudo(*args)
    parte_de_cima(*args)

    status_log()


def status_log():
    lista = ['1 - RECEBIDO', '2 - TEMPO ESGOTADO', '3 - INACESSIVEL']

    for log in lista:
        print('| ', end='')
        print(f'{log:<70} |')
