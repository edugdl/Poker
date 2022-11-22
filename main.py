from baralho import Baralho
from jogador import *
from poker import Poker

jogadores = []

# print(baralho)

# qntd_jogadores = int(input("Insira a quantidade de jogadores que desejam jogar: "))
# for i in range(qntd_jogadores):
#     nome = input("Insira o nome do jogador: ")
#     saldo = float(input("Insira o saldo que o jogador iniciará: "))
#     jogadores.append(Jogador(nome, saldo))

run = True

jogadores.append(Jogador('a', 1500))
jogadores.append(Jogador('b', 2000))
jogadores.append(Jogador('c', 2000))
jogadores.append(Jogador('d', 3000))

while run:
    jogadores = jogadores[:]
    baralho = Baralho()
    baralho.recolher_e_embaralhar()
    baralho.distribuir_cartas(jogadores)

    poker = Poker(jogadores[:], baralho)
    poker.pre_flop()
    poker.nova_rodada("Flop")
    poker.nova_rodada("Turn")
    poker.nova_rodada("River")
    ganhador, valor = poker.verificar_ganhador()
    print(f"{ganhador.getNome()} venceu !")
    ganhador.receber(valor)

    for jogador in jogadores[:]:
        print(f"Olá {jogador.getNome()}")
        continuar = input("Deseja continuar jogando [S/N]? ").upper()
        if continuar == "N":
            jogadores.remove(jogador)
    
    if len(jogadores) < 2:
        run = False

print("Obrigado por jogar")
