# calculo Fibonacci


def fibo(termo):
    if termo == 1:
        return 0
    elif termo == 2:
        return 1
    else:
        return fibo(termo-1) + fibo(termo-2)


termo = int(input("Digite a quantidade de termos: "))
for i in range(1,termo+1):
    print(fibo(i),end="|")
