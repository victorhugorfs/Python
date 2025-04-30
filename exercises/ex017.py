import math
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa mede {:.2f}'.format(hipotenusa))