class Jogador:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.cartas = []
        self.aposta_atual = 0
        self.allIn = False
    
    def receber_mao(self, carta1, carta2):
        self.cartas = [carta1, carta2]

    def receber(self, saldo):
        self.saldo += saldo
    
    def apostar(self, aposta):
        self.saldo -= aposta

    def getCartasList(self):
        return self.cartas

    def getCartas(self):
        cartas = self.cartas[:]
        return f"{cartas[0]['numero']} de {cartas[0]['naipe']}, {cartas[1]['numero']} de {cartas[1]['naipe']}"

    def check(self, valor_rodada):
        if self.aposta_atual == valor_rodada:
            return True
        return False

    def call(self, valor_rodada):
        valor_call = valor_rodada - self.aposta_atual
        if valor_call == 0:
            return False
        if valor_call >= self.saldo:
            self.allIn = True
            print("ALL IN")
            self.apostar(self.saldo)
        else:
            self.apostar(valor_call)
        return True

    def raise_(self, valor_rodada):
        valor_raise = float(input("Insira o valor que deseja acrescentar na rodada atual: "))
        while valor_raise <= 0:
            valor_raise = float(input("Insira um valor válido que deseja acrescentar na rodada atual: "))
        valor_a_apostar = (valor_rodada + valor_raise) - self.aposta_atual
        if self.saldo < valor_a_apostar:
            return False
        elif self.saldo == valor_a_apostar:
            self.allIn = True
            print("ALL IN")
        self.apostar(valor_a_apostar)
        return valor_raise + valor_rodada

    def setAposta_atual(self, aposta):
        self.aposta_atual = aposta

    def getAposta_atual(self):
        return self.aposta_atual

    def getSaldo(self):
        return self.saldo

    def getNome(self):
        return self.nome
    
    def isAllIn(self):
        return self.allIn