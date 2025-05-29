s = 0
c = 0
while True:
    n = int(input('Digite um número, para finalizar o programa digite (999): '))
    if n == 999:
        print('Programa finalizado!')
        break
    c += 1
    s += n
print(f'Foram digitados {c} e a soma dos números digitados foi {s}')