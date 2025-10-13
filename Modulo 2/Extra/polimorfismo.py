from classe_animal import Animal
from classe_passaro import Pássaro
from animais_marinhos import AnimaisMarinhos

animal1=Animal(23_000_000, "Megalodonte", 18.00, "Rei dos Mares")
animal2=AnimaisMarinhos(22,"Peixe-Palhaço", 0.03, "Nemo")
animal3=Pássaro('Coruja', 'Edwiges')

def comunicar (qualquer_animal):
    print(f"Tentando comunicação com {qualquer_animal.espécie}")
    qualquer_animal.fazer_som()
print("\n")
print("="*50)
comunicar(animal1)

print("-"*50)
comunicar(animal2)

print("-"*50)
comunicar(animal3)
print("="*50)
print("\n")

