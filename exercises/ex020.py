import random
aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
aluno3 = input('Digite o nome do terceiro aluno:')
aluno4 = input('Digite o nome do quarto aluno:')
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print('A ordem sorteada foi em primeiro {}, em segundo {}, em terceiro {} e em quarto {}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))