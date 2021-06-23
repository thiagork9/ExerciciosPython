# -*- coding: UTF-8 -*-

"Pegar idade em dias e transformar em anos, meses e dias"


def idade_em_anos():
    print('Digite sua idade em dias: ')
    idade = int(input())

    anos = int(idade / 365)
    meses = int(idade % 365 / 30)
    dias = int(idade % 365) % 30

    print('A pessoa tem ', anos, ' anos, ', meses, ' meses, ', dias, ' dias!')


idade_em_anos()
