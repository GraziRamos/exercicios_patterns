class ConfigApp:
    _instancia = None

    def __init__(self):
        self.debug = True
        self.banco = "postgresql://localhost/meuapp"

    @classmethod
    def get(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia
    
#Testando
config1 = ConfigApp.get()
config2 = ConfigApp.get()

print(config1 is config2) #TRUE mesma instancia
print(config1.banco) #postgresql://localhost/meuapp

class ProdutoRepository:
    def __init__(self):
        self._produtos = []
    
    def salvar(self, produto):
        self._produtos.append(produto)
    
    def buscar_por_nome(self, nome):
        for p in self._produtos:
            if p["nome"] == nome:
                return p
        return None

    def listar_todos(self):
        return self._produtos

#Testando
repo = ProdutoRepository()
repo.salvar({"nome": "Notebook", "preco": 3500})
repo.salvar({"nome": "Mouse", "preco": 120})

print(repo.buscar_por_nome("Mouse"))
{'nome': 'Mouse', 'preco': 120}

class NotificacaoEmail:
    def enviar (self, mensagem):
        print (f"Email enviado:
{mensagem}"),

class NotificacaoSMS:
    def enviar(self, mensagem):
        print (f"SMS enviado:
{mensagem}"),

def criar_notificacao(tipo):
    tipos = {"email": NotificacaoEmail, "sms": NotificacaoSMS}
    classe = tipos.get(tipo)
    if not classe:
        raise ValueError(f"Tipo {tipo} invalido")

return classe()

#TESTANDOO
n1 = criar_notificacao("email"),
n1.enviar("Bem-Vindo ao Sistema!"),

n2= criar_notificacao("sms"),
n2.enviar("Seu código é 1234"),