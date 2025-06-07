import math
print('='*30)
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
print('='*30)
operação = 0
while operação != 11:
    operação = int(input('''Digite qual operação você deseja fazer:
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
    if operação == 1:
        print('A soma de {} + {} é igual a {}'.format(n1, n2, n1+n2))
        print('='*30)
    if operação == 2:
        print('A subtração de {} - {} é igual a {}'.format(n1, n2, n1-n2))
        print('='*30)
    if operação == 3:
        print(' A multiplicação de {} vezes {} é igual a {}'.format(n1, n2, n1*n2))
        print('='*30)
    if operação == 4:
        print(' A Divisão de {} vezes {} é igual a {}'.format(n1, n2, n1/n2))
        print('='*30)
    if operação == 5:
        print('O fatorial de {} é {}, e o fatorial de {} é {}'.format(n1, math.factorial(n1), n2, math.factorial(n2)))
        print('='*30)
    if operação == 6:
        print('{} elevado a {} é igual a {}'.format(n1, n2, n1**n2))
        print('='*30)
    if operação == 7:
        print('A raiz de {} é {:.2f}, e a raiz de {} é {:.2f}'.format(n1, math.sqrt(n1), n2, math.sqrt(n2)))
    if operação == 8:
        if n1 > n2:
            print('{} é maior do que {}'.format(n1, n2))
            print('='*30)
        if n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
            print('='*30)
        else:
            print('São iguais!!')
            print('='*30)
    if operação == 9:
        if n1 < n2:
            print('{} é menor do que {}'.format(n1, n2))
            print('='*30)
        if n1 > n2:
            print('{} é menor que {}'.format(n2, n1))
            print('='*30)
        else:
            print('São iguais!!')
            print('='*30)
    if operação == 10:
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
    if operação > 11:
        print('Número inválido')
        print('='*30)
print('Espero ter ajudado!!')
