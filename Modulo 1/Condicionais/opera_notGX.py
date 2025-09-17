"""5 Operações Aritméticas
5 Operações Relacionais
5 Operações Lógicas
1 Função

Operações Aritméticas
soma = A + B
subtracao = D - C
multiplicacao = A * C
divisao = D / B
modulo = D % C

Operações Relacionais
maior = D > C
menor = A < B
igual = A == C
diferente = B != D
maior_igual = D >= A

Operações Lógicas
logico_and = (A < D) and (B < C)
logico_or = (A > D) or (B < C)
logico_not = not (A == B)
logico_and2 = (A == 3) and (C == 4)
logico_or2 = (B == 2) or (D == 5)"""

def aritimeticas(Num1, Num2, operacao):
    if operacao=='+':
        return Num1+Num2
    elif operacao=='-':
        return Num2-Num1
    elif operacao=='*':
        return Num1*Num2
    elif operacao=='/':
        return Num1/Num2
    elif operacao=='%':
        return Num1%Num2
    else:
        return "operação invalida"
def relacionais(Num1, Num2, operacao):
    if operacao=='>':
        return Num2>Num1
    elif operacao=='<':
        return Num1<Num2
    elif operacao=='==':
        return Num1==Num2
    elif operacao=='!=':
        return Num1!=Num2
    elif operacao=='>=':
        return Num2>=Num1
    else:
        return "operação invalida"
    
def logicos(num1, num2, operacao):
    if operacao=='and':
        return num1 and num2
    elif operacao=='or':
        return num1 or num2
    elif operacao=='not':
        return not num1
    else:
        return "operação invalida"

funcao=input("Qual função irá usar? (aritimeticas, relacionais, logicos)")
if funcao=='aritimeticas':
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))
    operacao=input("Digite a operação desejada (+, -, *, /, %): ")
    print(aritimeticas(num1, num2, operacao))
elif funcao=='relacionais':
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))
    operacao=input("Digite a operação desejada (>, <, ==, !=, >=): ")
    print(relacionais(num1, num2, operacao))
elif funcao=='logicos':
    num1=bool(input("Digite o primeiro valor booleano (True/False): "))
    num2=bool(input("Digite o segundo valor booleano (True/False): "))
    operacao=input("Digite a operação desejada (and, or, not): ")
    print(logicos(num1, num2, operacao))
else:
    print("Função inválida")