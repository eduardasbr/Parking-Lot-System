import os
os.system("cls")

# Controle de vagas do estacionamento

vagas = [0,0,0,0,0,0,0,0,0,0]

opcao = 0
while opcao != 4:
    print("""\n----------- MENU -----------
1 - Mostrar estado das vagas
2 - Ocupar uma vaga
3 - Liberar uma vaga
4 - Encerrar o programa
----------------------------""")
    opcao = int(input("\nEscolha: "))

    if opcao == 1:
        print("""\nEstado das vagas:
""")
        for v in range(10):
            if vagas[v] == 0:
                print(f"Vaga {v+1}: Livre")
            else:
                print(f"Vaga {v+1}: Ocupada")

    elif opcao == 2:
        num = int(input("Digite o número da vaga que deseja ocupar (1 a 10): "))
        if num < 1 or num > 10:
            print("Número de vaga inválido. Digite um valor entre 1 e 10.")
        elif vagas[num - 1] == 1:
            print("\nEssa vaga já está ocupada.")
        else:
            vagas[num - 1] = 1
            print("\nVaga ocupada com sucesso!")

    elif opcao == 3:
        num = int(input("Digite o número da vaga que deseja liberar (1 a 10): "))
        if num < 1 or num > 10:
            print("Número de vaga inválido. Digite um valor entre 1 e 10.")
        elif vagas[num - 1] == 0:
            print("\nEssa vaga já está livre.")
        else:
            vagas[num - 1] = 0
            print("\nVaga liberada com sucesso!")

    elif opcao == 4:
        print("\nEncerrando o programa...")

    else:
        print("Opção inválida, digite um valor entre 1 e 4.")
