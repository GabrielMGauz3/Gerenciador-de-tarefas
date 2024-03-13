class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def __str__(self):
        status = "[X]" if self.concluida else "[ ]"
        return f"{status} {self.descricao}"

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        tarefa = Tarefa(descricao)
        self.tarefas.append(tarefa)

    def remover_tarefa(self, indice):
        del self.tarefas[indice]

    def marcar_como_concluida(self, indice):
        self.tarefas[indice].concluida = True

    def mostrar_tarefas_pendentes(self):
        tarefas_pendentes = [tarefa for tarefa in self.tarefas if not tarefa.concluida]
        if tarefas_pendentes:
            print("Tarefas Pendentes:")
            for indice, tarefa in enumerate(tarefas_pendentes, start=1):
                print(f"{indice}. {tarefa}")
        else:
            print("Não há tarefas pendentes.")

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Marcar Tarefa como Concluída")
    print("4. Visualizar Tarefas Pendentes")
    print("5. Sair")

def main():
    gerenciador_tarefas = GerenciadorTarefas()

    while True:
        exibir_menu()
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            descricao = input("Digite a descrição da tarefa: ")
            gerenciador_tarefas.adicionar_tarefa(descricao)
            print("Tarefa adicionada com sucesso!")
        elif escolha == "2":
            indice = int(input("Digite o índice da tarefa a ser removida: ")) - 1
            gerenciador_tarefas.remover_tarefa(indice)
            print("Tarefa removida com sucesso!")
        elif escolha == "3":
            gerenciador_tarefas.mostrar_tarefas_pendentes()
            if gerenciador_tarefas.tarefas:
                indice = int(input("Digite o índice da tarefa concluída: ")) - 1
                gerenciador_tarefas.marcar_como_concluida(indice)
                print("Tarefa marcada como concluída com sucesso!")
        elif escolha == "4":
            gerenciador_tarefas.mostrar_tarefas_pendentes()
        elif escolha == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()