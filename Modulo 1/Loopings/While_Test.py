"""def Operacao():
    x=10
    while x>=0:
        print(x)
        x=x-1
    print('FOGO!!')
Operacao()

def Operacao():
    x=?
    while x<=y:
        print(x)
        x=x+1"""
#Imprimindo números pares.
"""fim=int(input("Digite o último número a imprimir:"))

def numeros_pares():
    x=0
    while x<=fim:
        if x%2==0:
            print(x)
        x=x+1
numeros_pares()"""

"""def numeros_impares():
    x=1
    while x<=fim:
        if x%2==1:
            print(x)
        x=x+1
numeros_impares()"""

def arvore_de_natal():
    linha=1
    while linha<=10:
        coluna=1
        while coluna<=linha:
            if coluna%3==0:
                print('🍥',end="")
            if coluna %2==0:
                print('🫓', end="")
            print('🍓',end="")
            coluna=coluna+1
        print()
        linha=linha+1
arvore_de_natal()