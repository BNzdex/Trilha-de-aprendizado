import random

def abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def desenhar_dado(valor):
    faces = {
        1: (
            "+-------+",
            "|       |",
            "|   *   |",
            "|       |",
            "+-------+"
        ),
        2: (
            "+-------+",
            "| *     |",
            "|       |",
            "|     * |",
            "+-------+"
        ),
        3: (
            "+-------+",
            "| *     |",
            "|   *   |",
            "|     * |",
            "+-------+"
        ),
        4: (
            "+-------+",
            "| *   * |",
            "|       |",
            "| *   * |",
            "+-------+"
        ),
        5: (
            "+-------+",
            "| *   * |",
            "|   *   |",
            "| *   * |",
            "+-------+"
        ),
        6: (
            "+-------+",
            "| *   * |",
            "| *   * |",
            "| *   * |",
            "+-------+"
        )
    }
    for linha in faces[valor]:
        print(linha)
    
def jogar_dado():
    return random.randint(1, 6)

def jogar():
    pontuacao_1 = 0
    pontuacao_2 = 0
    rodada = 1

    while True:
        print(f"\n--- Rodada {rodada} ---")

        # Jogador 1
        print(f"\nJogador 1, deseja jogar o dado?\nSua pontuação atual é {pontuacao_1}")
        print("1 - Sim")
        print("2 - Não")
        opcao1 = input("Escolha: ").strip().upper()

        if opcao1 in ["1", "SIM"]:
            valor = jogar_dado()
            pontuacao_1 += valor
            print(f"Você tirou {valor}! Nova pontuação: {pontuacao_1}")
            desenhar_dado(valor)
        
        elif opcao1 in ["2", "NAO", "NÃO"]:
            print(f"Jogador 1 desistiu. Jogador 2 venceu com {pontuacao_2} pontos!")
            break
        
        else:
            print("Opção inválida. Pulando rodada.")

        if pontuacao_1 >= 37:
            print("Jogador 1 venceu!!!")
            break

        # Jogador 2
        print(f"\nJogador 2, deseja jogar o dado?\nSua pontuação atual é {pontuacao_2}")
        print("1 - Sim")
        print("2 - Não")
        escolha_2 = input("Escolha: ").strip().upper()

        if escolha_2 in ["1", "SIM"]:
            valor = jogar_dado()
            pontuacao_2 += valor
            print(f"Você tirou {valor}! Nova pontuação: {pontuacao_2}")
            desenhar_dado(valor)
        
        elif escolha_2 in ["2", "NAO", "NÃO"]:
            print(f"Jogador 2 desistiu. Jogador 1 venceu com {pontuacao_1} pontos!")
            break
        
        else:
            print("Opção inválida. Pulando rodada.")

        if pontuacao_2 >= 37:
            print("Jogador 2 venceu!!!")
            break

        rodada += 1

def main():
    abertura()
    jogar()

main()
