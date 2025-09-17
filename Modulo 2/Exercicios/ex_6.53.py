"""estoque={"tomate": [1000,2.30],
         "alface": [500, 0.45],
          "batata": [2001, 1.20],
           "feijão": [100, 1.50] }

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
        print("Preço: %6.2f\n" % dados[1])"""
import csv

applesFile = open('OCORRENCIAS_2025.csv')
applesReader = csv.reader(applesFile, delimiter=';')

Espingarda = 0
Garruchao = 0
Pistola = 0
Pistolao = 0
Carabina = 0
Rifle = 0
Revolver = 0
Fuzil = 0

for row in applesReader:
    if row[4].strip() == 'Pistolao':
        Pistolao+=1
print(Pistolao)