print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
    if r1 == r2 == r3:
        print('Tipo: Equilátero (todos os lados iguais)')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Tipo: Isôsceles (dois lados iguais)')
    else:
        print('Tipo: Escaleno (todos os lados )')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')