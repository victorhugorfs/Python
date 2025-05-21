n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    menu = int(input('Digte qual vai ser a sua escolha: [1 - somar] [2 - multiplicar] [3 - maior] [4 - novos números] [5 - sair do programa]'))
    if menu == 1:
        print('A soma de {} + {} é {}'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print('O {} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('O {} é maior que {}'.format(n2, n1))
        else:
            print('Ambos são iguais.')
    elif menu == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Programa finalizado!')
    else:
        print('Opção inválida. Tente novamente.')
print('Fim!')