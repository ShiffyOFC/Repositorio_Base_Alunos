# _break_ é uma instrução e é utilizada para
# interromper a execução while independente-
# mente do valor de sua condição.

# _continue_ é para ignorar e continuar o
# laço de repetição, sendo o contrario do break
# sendo feito para continuar, não parar.

"""s=0

while True:
    v=int(input("digite um número a somar ou 0 para sair:"))
    if v==0:
        break
    s=s+v
print(s)"""

"""def lista_de_numeros():
    L=[]
    while True:
        n=int(input("Digite um número (0 para sair): "))
        if n==0:
            break #Caso for '0', o código irá
    #                     quebrar numerar
    #            os números usados como uma lista.
        L.append(n) #Append: adicionando
    #   elementos extras finais à uma lista.
    x=0
    while x<len(L): #Len: Retomando, 
#              exibindo números dos itens.
        print(L[x])
        x=x+1
print (lista_de_numeros())"""

"""def lista_de_palavras():
    L=[]
    while True:
        n=input("Digite uma palavra ('PARE' para sair): ")
        if n==["PARE", "pare", "Pare"]:
            break
        L.append(n)
    while len(L):
        print(L)
        break
print (lista_de_palavras())"""

def User():
    Nome=input("Qual o seu nome (Completo): ")
    print(Nome) 
    Idade=int(input("Qual a sua idade (Atual): "))
    print(Idade)
    Altura=float(input("Qual a sua altura: "))
    print(Altura)
    Pergunta=input("Você gosta de programar? Resposta: ")
    if Pergunta==("Sim"):
        print("True")
    if Pergunta==("Não"):
        print("False")
print(User)