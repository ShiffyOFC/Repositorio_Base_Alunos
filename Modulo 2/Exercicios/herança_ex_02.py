from herança_ex_01 import Personagem

class Heroi(Personagem):

    def heroi(self):
        return print(f"{self.Nome} está salvando pessoas pela cidade! 🦸")

print("\n")
Albert=Heroi("Albert", 16, 1.75, "Masculino", "Super Força")
Albert.descansar(), print("\n")
Julia=Personagem("Julia", 23,1.60,"Feminino","Nenhum")
Julia.trabalho(), print("\n")
Barry=Heroi("Barry", 22, 1.78, "Masculino", "Super Velocidade")
Barry.heroi(), print("\n")
Bruce=Heroi("Bruce", 37, 1.86, "Masculino", "Nenhum")
Bruce.patrulhar(), print("\n")
Peter=Heroi("Peter", 19, 1.75, "Masculino", "Poderes de Aranha")
Peter.poder(), print("\n")
