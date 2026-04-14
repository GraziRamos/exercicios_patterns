class Guerreiro:
    def __init__(self):
        self.ataque = 10
        self.defesa = 8

    def apresentar(self):
        print(f"Guerreiro -> Ataque: {self.ataque}, Defesa: {self.defesa}")

class Arqueiro:
    def __init__(self):
        self.ataque = 15
        self.defesa = 5

    def apresentar(self):
        print(f"Arqueiro -> Ataque: {self.ataque}, Defesa: {self.defesa}")

def criar_personagem(classe):
    if classe == "guerreiro":
        return Guerreiro()
    elif classe == "arqueiro":
        return Arqueiro()
    else:
        print("Classe inválida")
        return None

p1 = criar_personagem("guerreiro")
p2 = criar_personagem("arqueiro")

p1.apresentar()
p2.apresentar()