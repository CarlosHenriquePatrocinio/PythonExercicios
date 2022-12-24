""" Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. """

prod = float(input('Qual o preço do produto? R$'))
novo = prod-(prod*5/100)
print(f'O produto que custava R${prod:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}.')
