# o programa calcula o salário com % de acrescimo inserida pelo usuário

def calc_asc():
    salario = float(input("Digite seu salário atual: "))
    porcentagem = float(input("Digite a porcentagem de acrescimento: "))
    porcentagem_n = porcentagem / 100
    salario_reajustado = salario + (salario * porcentagem_n)
    print("O salário com {:.0f}% de acréscimo foi de R${:.2f} para R${:.2f}".format(porcentagem, salario, salario_reajustado))


calc_asc()
