from random import shuffle


class Baralho:
    def __init__(self):
        self.cartas = []
    
    def recolher_e_embaralhar(self):
        self.cartas = []
        for i in range(1,14):
            if i == 1:
                numero = "A"
            elif i == 11:
                numero = "J"
            elif i == 12:
                numero = "Q"
            elif i == 13:
                numero = "K"
            else:
                numero = str(i)
            for naipe in ["PAUS","COPAS","ESPADA","OUROS"]:
                self.cartas.append({'numero':numero, 'naipe':naipe})
        self.embaralhar()

    def embaralhar(self):
        baralho_atual = self.cartas[:]
        shuffle(baralho_atual)
        self.cartas = baralho_atual

    def distribuir_cartas(self, jogadores):
        for jogador in jogadores:
            jogador.receber_mao(self.cartas[0], self.cartas[1])
            self.cartas.pop(0)
            self.cartas.pop(0)

    def virar_uma_carta(self):
        self.embaralhar()
        return self.cartas.pop(0)

    def __str__(self):
        baralho = ""
        for i in range(52):
            baralho += str(self.cartas[i])+"\n"
        return baralho