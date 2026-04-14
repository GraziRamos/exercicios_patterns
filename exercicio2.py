class TarefaRepository: #Cria uma classe para gerenciar tarefas tipo um mini banco de dados em memoria
    def __init__(self): #Sempre que cria 1 objeto: Nasce uma lista vazia, no caso aqui chamada: tarefas
        self.tarefas = []

    def adicionar(self, titulo): #Recebe o nome da tarefa
        tarefa = {
            "titulo": titulo,  #Aqui criou um pacote de tarefas:
            "concluida": False #Titulo e status (começa como não concluída)
        }
        self.tarefas.append(tarefa) #Guarda na lista

    def concluir(self, titulo): #Recebe o título da tarefa que quero concluir
        for tarefa in self.tarefas: #Percorre todas as tarefas
            if tarefa["titulo"] == titulo: #Se encontrar a tarefa com esse nome (no caso título)
                tarefa["concluida"] = True #Marca como concluída

    def listar_pendentes(self): #Busca só as tarefas em aberto
        pendentes = [] #Cria uma lista vazia
        for tarefa in self.tarefas: #Percorre todas
            if not tarefa["concluida"]: #Se não estiver concluída
                pendentes.append(tarefa["titulo"]) #Adiciona só o título na lista
        return pendentes


# Testando

repo = TarefaRepository() #Cria o repositório

#As tarefas
repo.adicionar("Estudar bastante Python") 
repo.adicionar("Fazer muitos exercícios")
repo.adicionar("Revisar todos os códigos")

repo.concluir("Fazer exercícios") #Marca como concluída

print(repo.listar_pendentes()) #Mostra só as abertas