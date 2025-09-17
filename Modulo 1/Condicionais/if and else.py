valor_parte=float(input("Insira o valor parte: "))
porcentagem=float(input("Insira o valor da porcentagem: "))
valor_total=valor_parte*(porcentagem/100)

if valor_total > 0.0:
    print("\nSeu novo valor é:", valor_total)
else:
    print("\nSeu valor permanesce:", valor_parte, "\nInsira um número maior que 0.")

"""
 If = SE
 Else = SENÃO
 Elif = SENÃO, SE

Pre-Terminal

nome=input("Digite o nome de aluno: ")
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))
nota4=float(input("Digite a quarta nota: "))
media=(nota1+nota2+nota3+nota4)/4

if media >= 6 and media <= 7:
    print(nome,"Foi aprovado(a).\nSua nota final é de: ",media)
elif media >= 8:
    print(nome,"Foi aprovado(a) com louvor!\nSua nota final é de: ", media)
else:
    print(nome,"Foi reprovado.\nSua nota final é de: ",media)

Terminal:
Digite o nome de aluno: Anthony Gabriel
Digite a primeira nota: 8
Digite a segunda nota: 8
Digite a terceira nota: 8
Digite a quarta nota: 8
Anthony Gabriel Foi aprovado(a) com louvor!
Sua nota final é de:  8.0

Digite o nome de aluno: Anthony Gabriel
Digite a primeira nota: 6
Digite a segunda nota: 6
Digite a terceira nota: 6
Digite a quarta nota: 6
Anthony Gabriel foi aprovado(a).
Sua nota final é de:  6.0

Digite o nome de aluno: Anthony Gabriel
Digite a primeira nota: 2
Digite a segunda nota: 2
Digite a terceira nota: 2
Digite a quarta nota: 2
Anthony Gabriel Foi reprovado.
Sua nota final é de:  2.0

Other 

saldo=int(input("Digite seu saldo bancário: "))
saque=int(input("Digite o valor de saque: "))
if saldo>=saque:
    saldo-=saque
    print("Você realizou um saque com sucesso! agora você possuí: ",saldo)
else:
    print("Você não possui saldo suficiente para realizar essa operação. Seu saldo é de:",saldo)

Ex (If) : Saldo/Saque/Banco - Se ter tal valor de saldo igual ou maior que o saque
seu saque é bem sucedido

Nota/Aluno - Se o aluno ter uma média maior ou igual a 6 e menor ou igual a 7
ele é aprovado(a)

Ex (Else) : Saldo/Saque/Banco - Se Não, caso o valor for menor
seu saque não é bem sucedido

Nota/Aluno - Se não, Se o aluno ter uma nota menor que 6
ele é reprovado

Ex (ElIf) : Nota/Aluno - Se o aluno ter uma nota maior que 8
Ele é aprovado(a) com louvor"""