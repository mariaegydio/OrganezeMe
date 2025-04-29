# gerenciador de tarefas

import os
import json

def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
        return []
    
    
# exibe todas as tarefas
def listar_tarefas(tarefas):
    print("Tarefas:")
    for tarefa in tarefas:
         status = "Concluida" if tarefa['concluida'] else "Pendente"
         print(f"ID: {tarefa['id']},Titulo: {tarefa['titulo']}, Status: {status}")

# escreve no arquivo e salva as tarefas
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# gerar id
def gerar_id(tarefas):
    if tarefas:
        return tarefas[-1]['id'] + 1

# adicionar tarefas
def adicionar_tarefa(tarefas):
    print("Adicionar nova tarefa")
    titulo = input("Titulo:")
    descricao = input("Descrição:")

    tarefa = {
        'id': gerar_id(tarefas),
        'titulo': titulo,
        'descricao': descricao,
        'status': False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa inserida com sucesso!")

# concluir tarefa
def concluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser concluída: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                if tarefa['concluida']:
                    print("A tarefa já foi concluída!")
                else:
                    tarefa['concluida'] = True
                    salvar_tarefas(tarefas)
                    print("Tarefa concluída com sucesso!")
                return  # Encerra a função após encontrar a tarefa
        print("Tarefa não encontrada!")
    except ValueError:
        print("ID inválido!")

# remover tarefa
def excluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser removida: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                tarefas.remove(tarefa)
                salvar_tarefas(tarefas)
                print("Tarefa removida com sucesso!")
                return  # Encerra a função após encontrar a tarefa
        print("Tarefa não encontrada!")
    except ValueError:
        print("ID inválido!")

# menu principal
def menu():
    print("=== Gerenciador de tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefa")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")
    return input("Escolha uma opção:")
# loop
def main():
    tarefas = carregar_tarefas()
    while True:
        opcao = menu()

        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':    
            excluir_tarefa(tarefas)
        elif opcao == '5':
            print('Saindo...')
            break
        else: 
            print('Opção inválida')
if __name__ == "__main__":
    main()

