#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valorh = float(input("Quanto você ganha por hora trabalhada? "))
horames = float(input("Quantas horas você trabalhou no mês? "))
salario = valorh*horames
print("O salário total do mês é: R$", salario)