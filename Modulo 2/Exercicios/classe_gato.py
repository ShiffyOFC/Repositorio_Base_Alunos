from classe_animal import Animal

class gato(Animal):
# Não presamos do __init__ aqui 
# se não tivermos novos atrubutos.
# O __init__ da classe Animal será 
# usado automaticamente.
# Sobrescrevendo o método da classe pai.
    def fazer_som(self):
        print(f"{self.nome} está miando: Miau!")

Gatin=gato("Amy")
Gatin.fazer_som()