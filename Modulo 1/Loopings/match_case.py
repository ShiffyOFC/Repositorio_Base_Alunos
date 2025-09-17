"""Ex: if e elif"""

"""Me lembrando que posso
usar 'import random' 
na hora que eu quiser ;-;"""
import random
value=random.randint(0,6)
match value:
    case 0:
        print("ZERO!")
    case 1:
        print("UM!")
    case 2:
        print("DOIS!")
    case 3:
        print("TRÊS!")
    case 4:
        print("QUATRO!")
    case 5:
        print("VOCÊ ESTOUROU!")
    case _:
        print("HOMEM DE SORTE!")