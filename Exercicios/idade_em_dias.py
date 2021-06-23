# -*- coding: UTF-8 -*-

"Faça um algoritmo que leia a idade de uma pessoa expressa em anos"
"meses e dias e escreva a idade dessa pessoa expressa em dias."
"Considerar 365 dias e mês com 30 dias."


def idade_em_dias():

    print('Digite a idade em anos: ')
    ano = int(input())
    print('Digite os meses: ')
    mes = int(input())
    print('Digite os dias: ')
    dia = int(input())

    ano = ano * 365
    mes = mes * 30
    idade = ano + mes + dia

    print('Essa pessoa tem ', idade, ' dias de vida !')


idade_em_dias()
