"""L=[8,9,15]
for sim in L:
    print(sim""" #eu finjo que não percebo Mas tudo está sendo observado, o esperto se faz de bobo pra ver ate onde o burro se faz de inteligente, nesse jogo sutil cada movimento é estratégico, e cada palavra tem um significado oculto, por trás do meu sorriso sereno estou atento a cada detalhe, absorvendo informações e compreendendo motivações, aprendi que nem sempre a prudente revelar todas as cartas que tem na manga, pois o conhecimento é poder, e a paciência, é uma virtude, as vezes, é mais facil agir com descrição, permitindo que outros revelem suas intenções sem interferencia, afinal, a melhor defesa é a percepção aguçada, capaz de desvendar as tramas sutis que permeiam as interações humanas, Enquanto alguns tentam me iludir com suas artimanhas, observo, observo calmamente ciente de que minha aparente ingenuidade, é apenas uma estratégia para extrair informações, e desvendar as camadas Ocultas das personalidades alheias não se trata de malicia, mas sim de autopreservação, de proteger meus valores e princípios, enquanto navego por um mar De relações Complexas e desafios diários.
#While: Você não sabe quando acabar, For: Você sabe
"""L=["Maçãs", "Peras", "Kiwis",
    "Melancias", "Amoras", "Melões",
    "Bananas", "Morangos",  "Blueberries",
     "NãoSei" ]
for s in L:
    for letra in s:
        print(letra)"""
"""def exibir_maior():
    L=[4,7,10,8]
    máximo=L[0]
    for e in L:
        if e > máximo:
            máximo=e #'máximo' recebe o 'e'
    print(máximo)
exibir_maior()"""

"""def exibir():
    l1=int(input("Defina o primeiro número: "))
    l2=int(input("Defina o segundo número: "))
    l3=int(input("Defina o terceiro número: "))
    l4=int(input("Defina o quarto número: "))
    if l1==l2==l3==l4:
        print("Todos os números são iguais, tente novamente.")
    else:
        L=[l1, l2, l3, l4]
        posição=L[0]
        escolha=input("Escolha qual deseja saber? Maior ou Menor: ")
        if escolha=="Maior" or "menor":
            for e in L:
                if e > posição:
                    posição=e #'posição' recebe o 'e'
            print(posição)
        if escolha=="Menor" or "menor":
            for e in L:
                if e < posição:
                    posição=e
            print(posição)
        if escolha!="Menor"or"menor"or"Maior"or"maior":
            print("Você não escolheu corretamente, tente novamente.")
exibir()"""
#range=Inicia e fim (inicio, fim):
#ex: for v in range(5, 8):
#   print(v)

#%d=marcador de posição de números inteiros
#%s=marcador de posição de strings/textos
#%f=marcador de posição de números decimais
# Usados para adicionar/ocupar posições,
# você consegue usar para que caso queira
# que tal coisa você queira que ocupe tal posição

#ex: 
# >>> print("%5f" % 5)
#     5.00000
#>>>print("%5.2f" % 5)
#     5.00
#print("%10.5f" % 5)
#          5.00000
"""def composição_string():
    nome=input("Defina seu nome: ")
    idade=int(input("Defina sua idade: "))
    dinheiro=float(input("Defina sua quantidade de dinheiro: "))
    print("%s tem %d anos e R$%5.2f no banco." % (nome,idade,dinheiro))
composição_string()"""
