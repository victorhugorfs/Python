num = int(input('Digite um número:'))
totao_divisoes = 0
for i in range(1, num + 1):
    if num % i == 0:
        totao_divisoes += 1
if totao_divisoes == 2:
    print('Ele é primo!')
else:
    print('Ele não é primo.')