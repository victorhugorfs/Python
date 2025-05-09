n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) /2
if media < 5.0:
    print('Reprovado!')
elif media >= 5.0 and media <= 6.9:
    print('Recuperação!')
elif media >= 7.0:
    print('Aprovado!')