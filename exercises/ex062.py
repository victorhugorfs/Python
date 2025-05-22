primeiro = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
print('Os 10 primeiros termos da PA são:')
contador = 0
while contador < 10:
    print(primeiro)
    contador += 1
    primeiro += razao

pergunta = int(input('Você quer que mostre mais alguns termos? Digite um valor inteiro (0 para encerrar): '))
while pergunta !=0:
    termo = 0
    while termo < pergunta:
        print(primeiro)
        contador +=1
        primeiro += razao
        termo += 1
    pergunta = int(input('Deseja ver mais termos? Digite um valor inteiro (0 para encerrar): '))
print('Programa encerrado!')