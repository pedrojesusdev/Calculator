import math
print('='*30)
print('''Bem vindo à calculadora!!!
Digite os dois números que você deseja utilizar, 
e logo após a operação.''')
print('='*30)
number1 = int(input('Digite o primeiro número:'))
number2 = int(input('Digite o segundo número:'))
print('='*30)
operation = 0
while operation != 11:
    operation = int(input('''Digite qual operation você deseja fazer:
[1] Somar
[2] Diminuir
[3] Multiplicar
[4] Dividir
[5] Fatorial
[6] Potência
[7] Raiz
[8] Maior
[9] Menor
[10] Reset (novos números)
[11] Sair do programa
'''))
    
    print('='*30)
    if operation == 1:
        print(f'A soma de {number1} + {number2} é igual a {number1+number2}')
        print('='*30)
    if operation == 2:
        print(f'A subtração de {number1} - {number2} é igual a {number1-number2}')
        print('='*30)
    if operation == 3:
        print(f' A multiplicação de {number1} vezes {number2} é igual a {number1*number2}')
        print('='*30)
    if operation == 4:
        print(f' A Divisão de {number1} vezes {number2} é igual a {number1/number2}')
        print('='*30)
    if operation == 5:
        print(f'O fatorial de {number1} é {math.factorial(number1)}, e o fatorial de {number2} é {math.factorial(number2)}')
        print('='*30)
    if operation == 6:
        print(f'{number1} elevado a {number2} é igual a {number1**number2}')
        print('='*30)
    if operation == 7:
        print(f'A raiz de {number1} é {math.sqrt(number1):.2f}, e a raiz de {number2} é {math.sqrt(number2):.2f}')
    if operation == 8:
        if number1 > number2:
            print(f'{number1} é maior do que {number2}')
            print('='*30)
        if number1 < number2:
            print(f'{number2} é maior que {number1}')
            print('='*30)
        else:
            print('São iguais!!')
            print('='*30)
    if operation == 9:
        if number1 < number2:
            print(f'{number1} é menor do que {number2}')
            print('='*30)
        if number1 > number2:
            print(f'{number2} é menor que {number1}')
            print('='*30)
        else:
            print('São iguais!!')
            print('='*30)
    if operation == 10:
        number1 = int(input('Digite o primeiro número:'))
        number2 = int(input('Digite o segundo número:'))
    if operation > 11:
        print('Número inválido')
        print('='*30)
print('Espero ter ajudado!!')
