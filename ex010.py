carteira= float(input("Digite o valor em R$ que você tem em sua carteira para verificar quantos em dolar você consegue comprar "))
dolar = carteira /5.60
print('Você pode comprar com o valor  R${:.2f} em dolar ${:.2f}!'.format(carteira, dolar))