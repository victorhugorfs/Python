import time
print('Todos os número impares e múltiplos por três:')
for n in range(0, 501):
    if n % 2 != 0 and n % 3 == 0:
        print(n)
        time.sleep(0.3)