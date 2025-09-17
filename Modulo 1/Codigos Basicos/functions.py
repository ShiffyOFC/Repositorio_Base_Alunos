texto_escrito="Este livro é legal!"
outro_texto='Vou aprender a programar.'
texto="""
primeira linha
segunda linha
terceira linha
"""
print('\n')
print(texto_escrito)
print('\n')
print(outro_texto)
print('\n')
print(texto)
print('\n')
print("Uso de parentêses entre as aspas precisa do uso de '\'/(invertida)\''. Ex: \"(Aspas)\"")
print('\n')
print("\tOi!\nEu me chamo \"(Thomy)\"!!!")
print('\n')
textinho="Gostei do livro!"
texto_='vou aprender a programar mais..'
texto_=textinho
print(texto_)
print('\n')
print("Operações Compostas\n")
chocolates_menos=13
chocolates_quantia=32
chocolates_mais=14
pessoas_dividir=3
magia_duplicar=2
chocolates_quantia-=chocolates_menos
print(chocolates_quantia)
print('\n')
chocolates_quantia+=chocolates_mais
print(chocolates_quantia)
print('\n')
chocolates_quantia/=pessoas_dividir
print(chocolates_quantia)
print('\n')
chocolates_quantia*=magia_duplicar
print(chocolates_quantia)
print('\n')
carteira_digital=65.7
print(carteira_digital)
print('#Valor atual')
print('\n')
carteira_digital+=200
print(carteira_digital)
print('#Ganhei 200R$ no pix')
print('\n')
carteira_digital-=140.7
print(carteira_digital)
print('#Depositei 140 no cofre')
print('\n')
carteira_digital+=50
print(carteira_digital)
print('#Minha mãe depositou 50 ontem na minha conta')
print('\n')
def dizer_ola( nome_usuario = "Pão 🍞" ):
    print("Olá", nome_usuario)
dizer_ola("Meithieus")
print('\n')
dizer_ola("Anthony")
print('\n')
dizer_ola()
print('\n')
dizer_ola(3+2/2*1**3-40*3+79*2)
print('\n')
print('\t \'Comentários\'')
print("Podemos usá-lo para colocar em meio ao código o que queremos memorizar, basta apenas usar '#olá' ou aspas duplas três vezes")
#Comer pão é bom pra caramba 🍞
"""
ISSO É UM
COMENTÁRIO
CAR@#H-!!!
"""
print('Reveja em meio aos textos, não é visualizável no terminal.')
print('\n')
"""\tImput
Usuário digita no teclado e é guardado como um texto(string)
para que você possa usar depois no seu código.
\t Serve para PEDIR DADOS ao usuário enquanto o programa está rodando.
"""
"""
Função Input
nome=input("Insira seu nome:)
    nome=input()
    saudacao="Olá "+nome
print(saudacao)
R: Insira seu nome: Rapaz
Olá Rapaz
"""
"""
Casting de string para int
numero_string=input()
numero_inteiro=int( numero_string )
subtracao = numero_inteiro - 30

casting de int para string

numero_um = input()
numero_dois = input()
resultado_soma = numero_um + numero_dois
resultado_soma_texto= str( resultado_soma
mensagem = "O resultado da soma é: "+resultado_soma_texto)

cmd:

numero=int(input("insira um número: "))
valor = numero - 2
print(valor)

Insira um número: 9
R: 7
"""
# Escopo: Limite determinado em que se deseja atingir
# um objetivo que se pretende atingir; limite ou abrangêsncia de uma operação
#LOCAL (Dentro da função)
#GLOBAL (Fora da função)
"""
numero=3 #Global

def apresentar_numero():
    numero = 2  #Local
    print(numero)
apresentar_numero()
print(numero)
"""
numero=3

def apresentar_numero():
    global numero
    print(numero)
    numero=2
    print(numero)
apresentar_numero()
print(numero)