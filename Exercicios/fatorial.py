# calculo de fat

def fat(num):
    if num < 2:
        return 1
    else:
        return num * fat(num - 1)


num = int(input("Digite o número a ser calculado: "))
print(fat(num))