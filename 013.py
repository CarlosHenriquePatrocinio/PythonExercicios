""" Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. """

sal = float(input(f'Qual é o salário do funcionário? R$'))
novo = sal+(sal*15/100)
print(f'Um funcionário que ganhava R${sal:.2f}, com 15% de aumento, passa a receber R${novo:.2f}.')
