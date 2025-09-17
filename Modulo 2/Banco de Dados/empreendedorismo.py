estoque={   "Bola Futebol": [1500, 179.90],
        "Bola Futsal": [750, 166.90],
        "Bola Handbol": [950, 106.59],
        "Bola Basquete": [550, 202.59],
        "Bola Queimada": [402, 94.90],
        "Bola Tênis": [325, 59.9],
        "Bola Voleibol": [750, 159.44],
        "Bola Tênis de mesa": [1700, 22.50],
        "Bola Golfe": [377, 244.69],
        "Bola Futebol Americano": [223, 179.50],
        "Bola Rugby": [179, 122.70],
        "Chuteira Futebol": [620, 277.35],
        "Chuteira Futebol Americano": [390, 154.56],
        "Chuteira Baseball": [160, 220.90],
        "Taco de Baseball": [290, 120.90],
        "Bola Baseball": [400, 71.90],
        "Tênis Basquete": [569, 369.67],
        "Raquete Tênis": [600, 120.99],
        "Raquete Tênis de mesa": [609, 89.50],
        "Taco de Golfe": [298, 682.26]  }
print("Este é seu estoque:\n", estoque, "\n")
produto=input("Digite o produto selecionado: ")
quantidade=float(input("Digite a quantidade: "))
venda=[ [produto, quantidade] ]
total=0

if produto in estoque:
    print("Vendas:\n")
    for operação in venda:
        produto, quantidade = operação
        preço=estoque[produto][1]
        custo=preço*quantidade
        print("%12s: %3d x %6.2f=%6.2f" %
              (produto, quantidade, preço, custo))
        estoque[produto][0]-=quantidade
        total+=custo
    else:
        print("Não temos este produto no nosso estoque!")
    print(" Custo total: %21.2f/n" % total)
    print("Estoque: \n")
    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print("Preço: %6.2f\n" % dados[1])