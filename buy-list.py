
import os

buy_list = []  # Lista base do programa.

while True:

    # Usuário escolhe se quer adicionar, remover ou verificar itens da buy_list.
    user_options = input(
    "Deseja adicionar, remover ou verificar os itens da lista? Selecione a, r ou v: "   
    ).lower()

    # Caso queira adicionar 
    if user_options == "a":
        os.system("cls")  # Limpa o terminal.
        item_add = input(
            "O que deseja adicionar na lista de compras? "
        )  # Input para adicionar algum item.
        buy_list.append(item_add)  # Adiciona o item escrito no input a buy_list.

    elif user_options == "r":
        os.system("cls")  # Limpa o terminal.
        item_delete = input(
            "Selecione o índice do item que deseja remover: "
        ).isdigit()  # Input para selecionar o index com verificação se é dígito ou não. 
        
        try:
            del_index = int(item_delete)  # Transforma o input anterior em número int. 
            del buy_list[del_index]  # Deleta o item da buy_list com base no index selecionado.

        except ValueError:  # Erro se o usuário digitar algo que não seja um número inteiro.
            print("Por favor, digite um número inteiro.")

        except IndexError:  # Erro se o usuário digitar um índice que não existe na lista.
            print("O índice não existe na lista.")
        
        except:  # Erro genérico.
            print("Erro de causa desconhecida.")

    elif user_options == "v":
        os.system("cls")  # Limpa o terminal. 
        
        if len(buy_list) == 0:  # Se o número de itens na lista for igual a 0.
            print(
                "Não há nada na lista."
            )

        # Para cada index e item existentes para cada índice da lista.
        # enumerate serve para identificar o número de iterações no loop.
        for index, item in enumerate(buy_list):
            print(index, item)
    else:  # Se o usuário não selecionar uma das letras válidas.
        print("Escolha a, r ou v para continuar.")

    program_leave = input(
        "Quer sair do programa? s/n: "
    )  # Input para sair do programa

    # Se a resposta para o input anterior for s 
    if program_leave == "s":
        os.system("cls")  # Limpa o terminal.
        print(
            "Você escolheu sair do programa."
        )
        break  # O loop do programa será quebrado.