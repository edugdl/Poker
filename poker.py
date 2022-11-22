from jogadas import Jogadas

class Poker:
    def __init__(self, jogadores, baralho):
        self.jogadores = jogadores
        self.cartas_mesa = []
        self.pot = 0
        self.valor_rodada = 0
        self.baralho = baralho
    
    def pre_flop(self):
        self.pot = 0
        self.valor_rodada = 100
        continuar = True
        for jogador in self.jogadores:
            jogador.allWin = False
        while continuar:
            jogadores = self.jogadores[:]
            for jogador in jogadores:
                if jogador.getAposta_atual() == self.valor_rodada:
                    continuar = False
                    break
                elif not jogador.isAllIn():
                    self.apostar(jogador)
                    print("="*45)
        self.pot += self.valor_rodada
        print("Pre flop concluído com sucesso")
        print("="*45)

    def nova_rodada(self, nome):
        if nome == "Flop":
            self.cartas_mesa.append(self.baralho.virar_uma_carta())
            self.cartas_mesa.append(self.baralho.virar_uma_carta())    
        self.redefinir_valor_aposta_jogadores()
        self.cartas_mesa.append(self.baralho.virar_uma_carta())
        continuar = True
        i = 0
        while continuar:
            jogadores = self.jogadores[:]
            for jogador in jogadores:
                if (jogador.getAposta_atual() == self.valor_rodada) and (i != 0 or [jogador.isAllIn() == True for jogador in self.jogadores].count(False) == 1):
                    continuar = False
                    break
                elif not jogador.isAllIn():
                    self.apostar(jogador)
                print("="*45)
            i += 1
        self.pot += self.valor_rodada
        print(f"{nome} concluído com sucesso")
        print("="*45)

    def redefinir_valor_aposta_jogadores(self):
        for jogador in self.jogadores:
            jogador.setAposta_atual(0)
        self.valor_rodada = 0

    def getCartasMesa(self):
        cartas = ""
        if not self.cartas_mesa:
            return "Ainda não há cartas viradas"
        for carta in self.cartas_mesa:
            cartas += f"{carta['numero']} de {carta['naipe']}, "
        return cartas

    def apostar(self, jogador):
        resultado = False
        while resultado == False:
            print(f"1- Call                     Saldo atual: R$ {jogador.getSaldo():.2f}")
            print(f"2- Raise                    Aposta atual: R$ {jogador.getAposta_atual():.2f}")
            print(f"3- Fold                     Pot total: R$ {self.pot:.2f}")
            print(f"4- Check                    Valor rodada atual: R$ {self.valor_rodada:.2f}\n")
            print(f"Suas cartas: {jogador.getCartas()}")
            print(f"Cartas da mesa: {self.getCartasMesa()}")
            acao = int(input(f"Oque deseja fazer, {jogador.getNome()}? "))
            while acao not in [1,2,3,4]:
                acao = int(input(f"\n1-Call\n2-Raise\n3-Fold\n4-Check\nInsira uma ação válida {jogador.getNome()}: "))
            if acao == 1:
                resultado = jogador.call(self.valor_rodada)
                if resultado:
                    jogador.setAposta_atual(self.valor_rodada)
                    print(f"Voce deu call no valor de R$ {self.valor_rodada:.2f} com sucesso")
                    print(f"Seu saldo atual é de R$ {jogador.getSaldo():.2f}")
                else:
                    print("Não é possível dar call com nenhuma aposta")
            elif acao == 2:
                resultado = jogador.raise_(self.valor_rodada)
                if resultado:
                    self.valor_rodada = resultado
                    jogador.setAposta_atual(resultado)
                    print(f"Voce deu raise no valor de R$ {self.valor_rodada:.2f} com sucesso")
                    print(f"Seu saldo atual é de R$ {jogador.getSaldo():.2f}")
                else:
                    print("Seu saldo não é suficiente")
            elif acao == 3:
                resultado = True
                print("Voce saiu do jogo com sucesso")
                self.jogadores.remove(jogador)
            elif acao == 4:
                resultado = jogador.check(self.valor_rodada)
                if not resultado:
                    print("Não é possível dar check nessa situção")
                else:
                    print("Voce deu check com sucesso")
    
    def verificar_ganhador(self):
        jogadas = Jogadas()
        resultados = jogadas.verificar_ganhador(self.jogadores, self.cartas_mesa)
        indice = 0
        valor = 0
        for i in range(0,len(self.jogadores)):
            if resultados[i]['Valor'] > valor:
                valor =  resultados[i]['Valor']
                indice = i

        for j, jogador in enumerate(self.jogadores):
            print("="*45)
            print(jogador.getNome())
            print(jogador.getCartas())
            print(resultados[j]['Jogada'])
            print("="*45+"\n")
        print("="*45)
        print("Cartas da mesa")
        print(self.getCartasMesa())
        print("="*45)
        return self.jogadores[indice], self.pot
