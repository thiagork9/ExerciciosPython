# ordenação de uma lista utilizando função / import


def ordena_string():
    estudantes_lista = [
        ('Pedro da silva', 14),
        ('Maria souza', 12),
        ('José de paula', 13),
        ('Guilherme santos', 15)
    ]
    print("Lista desordenada",estudantes_lista)
    print("                              ")
    print("                              ")
    print("ORDENANDO PELA IDADE")
    print(sorted(estudantes_lista, key=lambda estudante: estudante[1]))
    print("                              ")
    print("ORDENANDO PELO NOME")
    print(sorted(estudantes_lista, key=lambda estudante: estudante[0]))
    exit()


def ordena_sem_variavel():
    print("ORDENANDO SEM VARIAVEL")
    print(sorted([10, 1, 22, 6, 8, 3, 14]))
    print("                              ")
    exit()


def ordena_com_variavel():
    print("ORDENANDO COM VARIAVEL")
    a = [10, 1, 22, 6, 8, 3, 14]
    print("Lista desordenada: ",a)
    a.sort()
    print("Lista ordenada: ",a)
    print("                              ")
    exit()


def menu_escolha():
    escolha = 1
    while escolha != 0:
        escolha = int(input(
            "1 - Ordenar String\n 2 - Ordenar sem a variável\n 3 - Ordenar com variavel (apenas armazena a ordenação em uma variável, com possibilidade de exibição da lista desornedada)\n 0 - Para encerrar\n"))
        if escolha == 1:
            ordena_string()
        if escolha == 2:
            ordena_sem_variavel()
        if escolha == 3:
            ordena_com_variavel()
        if escolha == 0:
            exit()


menu_escolha()
