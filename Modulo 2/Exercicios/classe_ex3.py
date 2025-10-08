class Pessoa():
    def __init__(self, nome, altura, idade, nacionalidade, etnia, cpf, telefone, cor_olhos, tom_pele, gênero):
        self._nome=nome
        self._altura=altura
        self._idade=idade
        self._nacionalidade=nacionalidade
        self._etnia=etnia
        self.__cpf=cpf
        self.__telefone=telefone
        self.olhos=cor_olhos
        self.tom_pele=tom_pele
        self.gênero=gênero
    
#    @property
    def nome(self):
        return self._nome

#    @property
    def altura(self):
        return self._altura

#    @property
    def idade(self):
        return self._idade

#    @property
    def nacionalidade(self):
        return self._nacionalidade

#    @property
    def etnia(self):
        return self._etnia

#    @property
    def cpf(self):
        return self.__cpf

#    @property
    def telefone(self):
        return self.__telefone
    
#    @property
    def olhos(self):
        return self.olhos
    
#    @property
    def tom_pele(self):
        return self.tom_pele

#    @property
    def gênero(self):
        return self.gênero
    


    def passear(self):
        return print(f"{self._nome} está passeando... 🚶")
    def comer(self):
        return print(f"{self._nome} está comendo... 😋")
    def divertir(self):
        return print(f"{self._nome} está se divertindo! 🪀")
    def medir(self):
        return print(f"{self._nome} está medindo sua altura e vê que possui {self._altura}... 📏")
    def jogar(self):
        return print(f"{self._nome} começou a jogar um pouco... 🎮")
    def treinar(self):
        return print(f"{self._nome} está treinando seu esporte favorito! 🏀")
    def doente(self):
        return print(f"{self._nome} foi ao hospital, por estar doente. 🤒")
    def festejar(self):
        return print(f"{self._nome} foi à uma festa se divertir!! 🥳🎉")
    def estudar(self):
        return print(f"{self._nome} está estudando na escola. 🏫📖")
    def dormir(self):
        return print(f"{self._nome} está dormindo... 😴💤")

"""    @gênero.setter
    def gênero(self, valor):
        self.gênero=valor

    @tom_pele.setter
    def tom_pele(self, valor):
        self.tom_pele=valor

    @olhos.setter
    def olhos(self, valor):
        self.olhos=valor

    @telefone.setter
    def telefone(self, valor):
        self.__telefone=valor

    @cpf.setter
    def cpf(self, valor):
        self.__cpf=valor

    @etnia.setter
    def etnia(self, valor):
        self._etnia=valor

    @nacionalidade.setter
    def nacionalidade(self, valor):
        self._nacionalidade=valor

    @idade.setter
    def idade(self, valor):
        self._idade=valor

    @altura.setter
    def altura(self, valor):
        self._altura=valor"""

Marie=Pessoa("Marie", 1.56, 15, "Brasil", "Branca", "46###4##7#1-##", "11-x73xx-9xx0", "Azuis", "Branco", "Fêminino")
Marie.medir()
#(self, nome, altura, idade, nacionalidade,
#  etnia, cpf, telefone, olhos, tom_pele, gênero):