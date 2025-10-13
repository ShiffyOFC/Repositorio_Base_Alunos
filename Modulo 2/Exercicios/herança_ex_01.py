class Personagem():
    def __init__(self, Nome, Idade, Altura, Sexo, Poder):
        self.Nome=Nome
        self.Idade=Idade
        self.Altura=Altura
        self.Sexo=Sexo
        self.Poder=Poder
    def patrulhar(self):
        return print(f"{self.Nome} está patrulhando a cidade... 🚔")
    def descansar(self):
        return print(f"{self.Nome} teve um dia cheio, resolveu descansar... 🛏️💤")
    def ajuda(self):
        return print(f"{self.Nome} ajudou um cego a atravessar a rua. 👨‍🦯‍➡️")
    def poder(self):
        return print(f"{self.Nome} descobre que tem uma habilidade, usando a/os sua/seus {self.Poder}! ♾️")
    def trabalho(self):
            return print(f"{self.Nome} está trabalhando em seu escritório... 🗄️🧾")

"""teste=Personagem("Ana", 16, 1.65, "Feminino", "Sorte")
teste.trabalho()"""