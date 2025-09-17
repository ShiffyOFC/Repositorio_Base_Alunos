# valor_total=0
# raças=['Pug',
#        'Pastor-alemão',
#        'Labrador']
# print(raças[0])
# print(raças[1])
# print('Labrador' in raças)

"""

exercicio: crie um programa que peça ao usuário para inserir uma raça de cachorro. 
Se a raça existe na lista (utilize ''In'') adicione o valor do atendimento ao valor total
e exiba o valor do atendimento. Se a raça não existe, exiba "Atendimento não disponivel". 
RAÇAS           ATENDIMENTO

Pug             R$70.99

Pastor-alemão   R$120.99

Labrador        R$110.99
"""
def atendimento_animal():
     valor_total=0
raças=['pug','pastor-alemão','labrador']
raça=input("Insira a raça de seu cachorro: ")
if (raça == 'pug'):
    valor_total=+70.99
    print('\nSeu valor de atendimento é de:',valor_total)
elif (raça =='pastor-alemão'):
    valor_total=+120.99
    print('\nSeu valor de atendimento é de:',valor_total)
elif (raça == 'labrador'):
    valor_total=+110.99
    print('\nSeu valor de atendimento é de:',valor_total)
else:
    print("\nO atendimento para está raça não está disponivel.")