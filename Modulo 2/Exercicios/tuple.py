"""tuple=("29/xx/20xx", "Opnião sobre o Lázaro", "4xxxx7x1xx8-xx")"""

# enumerate() "|Gera uma tupla em
# que o primeiro valor é o índice e o
# segundo é o elemento da lista sendo enumerada"

"""L=[0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
for x, e in enumerate(L):
    print("[%d] x %d = %d" % (x,e, x*e))""" #multiplicar

"""L=[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
for x, e in enumerate(L):
    print("[%d] + %d = %d" % (x,e, x+e))""" #soma

"""L=[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
for x, e in enumerate(L):
    print("%d - %d = %d" % (e,x, e-x))""" #menos

"""L=[0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
for x, e in enumerate(L):
    print("[%d] / %d = %f" % (x, e x/e))""" #divisão


"""L=[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
try:
    for x, e in enumerate(L):
        print("%d ÷ %d = %d" % (e,x, e/x))
except ZeroDivisionError:
    print("Por favor, não use zeros!")
else:
   for x, e in enumerate(L):
       print("%d ÷ %d = %d" % (e, x, e/x))
finally:
    for x, e in enumerate(L):
       print("%d ÷ %d = %d" % (e, x, e/x))"""