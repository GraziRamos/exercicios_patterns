class ContadorVisitas:
    _instancia = None

    def __init__(self):
        self._contador = 0

    @classmethod
    def get(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def visitar(self):
        self._contador += 1

    def total(self):
        return self._contador

# 🧪 Testando em dois "lugares diferentes"

# Lugar 1
contador1 = ContadorVisitas.get()
contador1.visitar()
contador1.visitar()

# Lugar 2
contador2 = ContadorVisitas.get()
contador2.visitar()

# Resultado
print(contador1.total())  # 3
print(contador2.total())  # 3

print(contador1 is contador2)  # True