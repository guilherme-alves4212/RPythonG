from random import choice

def player():
    while True:
        jogada_player = input("Qual o seu movimento? (pedra, papel, tesoura, lagarto ou Spock)? ").strip().lower()
        if jogada_player in ["pedra", "papel", "tesoura", "lagarto", "spock"]:
            return jogada_player
        else:
            print("Jogada inválida. Tente novamente.")

def cpu():
    return choice(["pedra", "papel", "tesoura", "lagarto", "spock"])

def mecanica():
    vencedor = {
        "pedra": {"pedra": "Empate", "papel": "CPU", "tesoura": "Player", "lagarto": "CPU", "spock": "Player"},
        "papel": {"pedra": "Player", "papel": "Empate", "tesoura": "CPU", "lagarto": "Player", "spock": "CPU"},
        "tesoura": {"pedra": "CPU", "papel": "Player", "tesoura": "Empate", "lagarto": "CPU", "spock": "Player"},
        "lagarto": {"pedra": "CPU", "papel": "Player", "tesoura": "CPU", "lagarto": "Empate", "spock": "Player"},
        "spock": {"pedra": "Player", "papel": "CPU", "tesoura": "Player", "lagarto": "CPU", "spock": "Empate"}
    }
    
    pontos_player = 0
    pontos_cpu = 0
    
    while pontos_player < 2 and pontos_cpu < 2:
        jogada_player = player()
        jogada_cpu = cpu()
        
        print(f"Você jogou {jogada_player}.")
        print(f"O computador jogou {jogada_cpu}.")
        
        resultado = vencedor[jogada_player][jogada_cpu]
        if resultado == "Empate":
            print("O jogo empatou, tente novamente!")
        elif resultado == "Player":
            pontos_player += 1
            print("Você venceu esta rodada!")
        else:
            pontos_cpu += 1
            print("O computador venceu esta rodada!")
        
        print(f"Placar: Você {pontos_player} x {pontos_cpu} Computador\n")
    
    if pontos_player == 2:
        print("Parabéns! Você venceu a melhor de 3!")
    else:
        print("O computador venceu a melhor de 3. Tente novamente!")

mecanica()
