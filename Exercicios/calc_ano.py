def calcula_idade():
    from datetime import date
    print('Digite seu ano de nascimento: ')
    ano_como_string = input()
    ano = int(ano_como_string)
    ano_atual = date.today().year
    idade = ano_atual - ano
    print('Você tem {} anos '.format(idade))


calcula_idade()
