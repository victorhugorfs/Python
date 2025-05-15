tabuada = int(input('Digite um valor para mostrar a sua tabuada:'))
print('Tabuada de {}'.format(tabuada))
for t in range(1, 11):
    resultado = tabuada *  t
    print('{} x {} = {}'.format(tabuada, t, resultado))