codigo_produto = 'LED20'
quantidade_produto = int(input(f'informe a quantidade do {codigo_produto} em estoque: \n').upper())

quantidade_minima = 1000
quantidade_maxima = 2500

if codigo_produto == 'LED20'
if quantidade_produto < quantidade_minima:
    
    unidades_compra = quantidade_minima - quantidade_produto
    print(f'compre {unidades_compra} unidades do produto {codigo_produto}.')

elif quantidade_produto > quantidade_minima:
        unidades_venda = quantidade_minima - quantidade_produto
        print(f'venda {unidades_venda} unidades de {codigo_produto}.')

else:
    print(f'não há necessidade de comprar mais unidades do produto {codigo_produto}')




