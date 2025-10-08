from classe_animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca=raca

    def fazer_som(self):
        print(f"{self.nome} está latindo: Au au!")

    def abanar_rabo(self):
        print(f"{self.nome} está abanando o rabo.")

Doguinho=Cachorro(input("Nome do dog: "), input("Raça do dog: "))
Doguinho.fazer_som()