def quadrado(area):
    resultado = area * area
    return resultado
print(quadrado(4))
print('\n')
def salario(valor):
    resultado = valor + valor * 0.15
    return resultado
print(salario(1600))
print('\n')
def triangulo(base, altura):
    resultado = base * altura / 2
    return resultado
print(triangulo(4, 6))
print('\n')
def fahrenheit(celsius):
    resultado = (9 * celsius + 160) / 5
    return resultado
print(fahrenheit(100))
print('\n')
def conta(x, y):
    z=x
    x=y
    y=z
    print(x, y)
print(conta(5, 9))
print('\n')
def paralelepipedo(base, altura, largura):
    resultado=base*altura*largura
    return resultado
print(paralelepipedo(6, 7, 4))