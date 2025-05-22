n = int(input('Quantos termos da sequência de Fibonacci você quer ver? '))
a = 0
b = 1
contador = 0
while contador < n:
    print(a, end=' → ' if contador < n - 1 else ' FIM')
    c = a + b
    a = b
    b = c
    contador += 1