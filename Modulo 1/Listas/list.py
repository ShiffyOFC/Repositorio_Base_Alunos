"""números=[1, 4, 7, 11, 47, 271]
coordenadas=[1.5694, 9.9991]
criaturas_mitológicas=['Unicornio', 'vampiro', 'minotauro', 'dragões', 'chupacabra']

print(números[3]) #11 (3°Posição)
print(criaturas_mitológicas[1]) #Vampiro
print(coordenadas[-1]) #9.9991

Concatenando Listas (junção de listas)

print(números+coordenadas)

números;insert(4,5)
print(números)

números.pop(4) #.pop "remover indíce"
print(números)
# [1, 4, 7, 11, 271]

Módulos
Todo os arquivos no caminho do interpretador com um código válido Python será um módulo.
Como o próprio arquivo salvo na pasta 'documentos' com arquivos ".py"

Path
Como o próprio nome diz, ele é um caminho
Como o caminho que os modulos constroem.

Módulo Random

import random

numero_aleatorio=random.random() #float
print(numero_aleatorio)
numero_aleatorio=random.randint(0,10) #int de 0 à 10

import random

jogos = ['NarutoStorm4', 'DragonBall Budokai 3', 'Fifa2018','Minecraft', 'Roblox', 'Devil May Cry 5', 'CS Go', 'Call of Duty: Modern Warfare', 'Fortnite', 'Silent Hill', 'Resident Evil: Requien']
print(random.choice(jogos))

import time

print (time.asctime()) #exibe o tempo atual, no horário do seu windows/ou outros

import turtle
turtle.circle(500)
turtle.getscreen()._root.mainloop()

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""