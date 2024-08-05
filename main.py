# biblioteca
import os


# Lista de tarefas
tarefas = []

while True:
    print('\n MENU\n')
    print('1- Exibir lista de tarefas.')
    print('2- Adicionar tarefa.')
    print('3- Exibir em ordem alfabética')
    print('4- Sair')
    # opção do usuário
    opcao = input('Opção: ')

    #limpa tela
    os.system('cls')

    match opcao:
        case '1':
         print('\nLISTA DE TAREFAS\n')
         for tarefa in tarefas:
           print(tarefa)
         continue     
        case '2':
            nova_tarefa = input('Nova tarefa: ')
            tarefas.append(nova_tarefa)
            print(f'{nova_tarefa} foi adicionada na lista.')
            continue 
        case '3':
            tarefas.sort()
            for tarefa in tarefas:
                print(tarefa)
            print('Ordenada.')
            continue
        case '4':
            print('Encerrado')
            break

    # limpa tela
    os.system('cls')

        

