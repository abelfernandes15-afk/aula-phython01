estoque = {
    'camisa': 50,
    'calça' : 15,
    'bone' : 35,
    'tenis nike' : 35,
}
# mostrar  estoque atual:
print('estoque atual:')
for produto,quantidade in estoque.items():
    print(f'{produto} : {quantidade}')
# pedindo info usuarios:
nome_produto = input('\ninforme nome produto vendido:')
quantidade_vendida =int(input('\n informe quatidade vendida'))
# atualizar estoque
if nome_produto in estoque:
    if quantidade_vendida <= estoque[nome_produto]:
        estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
        print('venda realizada com sucesso')
    else:
        print('produto nao encontrada')
    #estoque atualizado:
    for produtos, quantidade in estoque .items():
        print(f'{produto} | {quantidade}')