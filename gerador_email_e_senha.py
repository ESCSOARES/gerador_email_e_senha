import string
from random import random, choice

print ('qual o nome do corpo do email você quer?')
print ('exemplo: fernandas, fernandamoura, abacaxibolado ')
corpo_email = input ()
print('escolha números para o email')
print ('possa ser que já exista um com o mesmo nome, mas não com números iguais')
numero= input()
print ('qual o tipo de extensão você quer?')
print('1- gmail.com   2- hotmail.com   3- protonmail.com')
extensao_email = input()
if extensao_email == "1":
    print(corpo_email + numero + "@gmail.com" )

    tamanho = 8
    combinacoes = string.ascii_letters
    combinacoes += string.digits
    combinacoes += string.punctuation
    tamanho_senha = tamanho
    senha = ""

    for i in range(tamanho):
        senha += choice(combinacoes)

    print('aa senha desse email é :', senha)
    input('')

if extensao_email == "2":
    print(corpo_email + numero + "@hotmail.com" )

    tamanho = 8
    combinacoes = string.ascii_letters
    combinacoes += string.digits
    combinacoes += string.punctuation
    tamanho_senha = tamanho
    senha = ""

    for i in range(tamanho):
        senha += choice(combinacoes)

    print('a senha desse email é :', senha)
    input('')
#
if extensao_email == "3":
    print(corpo_email + numero + "@protonmail.com" )

    tamanho = 8
    combinacoes = string.ascii_letters
    combinacoes += string.digits
    combinacoes += string.punctuation
    tamanho_senha = tamanho
    senha = ""

    for i in range(tamanho):
        senha += choice(combinacoes)

    print('a senha desse email é :', senha)
    input('')
