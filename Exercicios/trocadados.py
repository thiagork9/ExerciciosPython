def troca_dados():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    aux = 0

    print('Os valores iniciais sao: ')
    print(a, b)

    # Troca dos dos dados sendo feita
    aux = a
    a = b
    b = aux
    print('Os valores trocados sao: ')
    print(a, b)


troca_dados()
