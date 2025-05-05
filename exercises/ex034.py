s = float(input('Digite o valor do seu salario:'))
if s > 1.250:
    aumento = s * 0.10
else:
    aumento = s *0.15
novo_salario = s + aumento
print(f"O valor do aumento é: R${aumento:.2f}")
print(f"O novo salário do funcionário é: R${novo_salario:.2f}")