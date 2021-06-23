"Funcao para teste de captura do resto de uma divisao"


def resto():
    num = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    resultado = num % num2
    print('O resto da divisao e {} '.format(resultado))


resto()
