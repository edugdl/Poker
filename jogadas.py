from baralho import Baralho

class Jogadas:
        
    naipes = ["PAUS","COPAS","ESPADA","OUROS"]
    numeros = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    def royal_flush(self, cartas_jogador, cartas_mesa):
        cartas = cartas_jogador + cartas_mesa

        for naipe in self.naipes:
            dez = {'numero':'10', 'naipe':naipe} in cartas
            j = {'numero':'J', 'naipe':naipe} in cartas
            q = {'numero':'Q', 'naipe':naipe} in cartas
            k = {'numero':'K', 'naipe':naipe} in cartas
            a = {'numero':'A', 'naipe':naipe} in cartas
            if dez and j and q and k and a : 
                return True
        return False

    def straight_flush(self, cartas_jogador, cartas_mesa):
        a = self.flush(cartas_jogador, cartas_mesa)
        b = self.straight(cartas_jogador, cartas_mesa)
        if a and b:
            return True
        return False
    
    def quadra(self, cartas_jogador, cartas_mesa):
        cartas = cartas_jogador + cartas_mesa

        for numero in self.numeros:
            a = {'numero':numero, 'naipe':'PAUS'} in cartas
            b = {'numero':numero, 'naipe':'COPAS'} in cartas
            c = {'numero':numero, 'naipe':'ESPADA'} in cartas
            d = {'numero':numero, 'naipe':'OUROS'} in cartas

            if a and b and c and d:
                return True
        return False
    
    def full_house(self, cartas_jogador, cartas_mesa):
        a = self.dupla(cartas_jogador, cartas_mesa)
        b = self.trinca(cartas_jogador, cartas_mesa)
        
        if a and b:
            return True
        return False
    
    def flush(self, cartas_jogador, cartas_mesa):
        cartas = cartas_jogador + cartas_mesa
        naipe = cartas[0]['naipe']
        count = 0
        for carta in cartas:
            if carta['naipe'] == naipe:
                count += 1
        if count >= 5:
            return True
        return False
    
    def straight(self, cartas_jogador, cartas_mesa):
        cartas = cartas_jogador + cartas_mesa
        n = []

        for carta in cartas:
            n.append(carta['numero'])
        
        l = self.numeros[:]
        l.append("A")

        for i in range(0,10):
            a = l[i] in n
            b = l[i+1] in n
            c = l[i+2] in n
            d = l[i+3] in n
            e = l[i+4] in n
            if a and b and c and d and e:
                return True
        return False

    def trinca(self, cartas_jogador, cartas_mesa):
        cartas = cartas_jogador + cartas_mesa

        for numero in self.numeros:
            a = {'numero':numero, 'naipe':'PAUS'} in cartas
            b = {'numero':numero, 'naipe':'COPAS'} in cartas
            c = {'numero':numero, 'naipe':'ESPADA'} in cartas
            d = {'numero':numero, 'naipe':'OUROS'} in cartas

            if [a,b,c,d].count(True) == 3:
                return True
        return False
    
    def duas_duplas(self, cartas_jogador, cartas_mesa):
        cartas = cartas_jogador + cartas_mesa
        n = self.dupla(cartas_jogador, cartas_mesa)
        
        if not n:
            return False
        for carta in cartas:
            if carta['numero'] == n:
                cartas.remove(carta)
        if self.dupla([cartas[0], cartas[1]], [cartas[2]]):
            return True
        return False
    
    def dupla(self, cartas_jogador, cartas_mesa):
        cartas = cartas_jogador + cartas_mesa

        for numero in self.numeros:
            a = {'numero':numero, 'naipe':'PAUS'} in cartas
            b = {'numero':numero, 'naipe':'COPAS'} in cartas
            c = {'numero':numero, 'naipe':'ESPADA'} in cartas
            d = {'numero':numero, 'naipe':'OUROS'} in cartas

            if [a,b,c,d].count(True) == 2:
                return numero
        return False
    
    def verificar_ganhador(self, jogadores, cartas_mesa):
        resultados = []
        for jogador in jogadores:
            if self.royal_flush(jogador.getCartasList(), cartas_mesa):
                resultados.append({'Jogada':'Royal Flush', 'Valor': 9})
            elif self.straight_flush(jogador.getCartasList(), cartas_mesa):
                resultados.append({'Jogada':'Straight Flush', 'Valor': 8})    
            elif self.quadra(jogador.getCartasList(), cartas_mesa):
                resultados.append({'Jogada':'Quadra', 'Valor': 7})
            elif self.full_house(jogador.getCartasList(), cartas_mesa):
                resultados.append({'Jogada':'Full House', 'Valor': 6})    
            elif self.flush(jogador.getCartasList(), cartas_mesa):
                resultados.append({'Jogada':'Flush', 'Valor': 5})
            elif self.straight(jogador.getCartasList(), cartas_mesa):
                resultados.append({'Jogada':'Straight', 'Valor': 4})
            elif self.trinca(jogador.getCartasList(), cartas_mesa):
                resultados.append({'Jogada':'Trinca', 'Valor': 3})
            elif self.duas_duplas(jogador.getCartasList(), cartas_mesa):
                resultados.append({'Jogada':'Duas Duplas', 'Valor': 2})    
            elif self.dupla(jogador.getCartasList(), cartas_mesa):
                resultados.append({'Jogada':'Dupla', 'Valor': 1})
            else:
                resultados.append({'Jogada':'Carta Mais Alta', 'Valor': 0})
        return resultados
# baralho = Baralho()
# rf = False
# sf = False
# q = False
# fh = False
# fl = False
# s = False
# t = False
# dd = False
# d = False

# i = 1
# while not(rf or sf or q or fh or fl or s or t or dd or d):
#     baralho.recolher_e_embaralhar()
#     cartasMesa=[]
#     cartasJogador=[]
#     cartasMesa.append(baralho.virar_uma_carta())
#     cartasMesa.append(baralho.virar_uma_carta())
#     cartasMesa.append(baralho.virar_uma_carta())
#     cartasMesa.append(baralho.virar_uma_carta())
#     cartasMesa.append(baralho.virar_uma_carta())
#     cartasJogador.append(baralho.virar_uma_carta())
#     cartasJogador.append(baralho.virar_uma_carta())
#     # rf = Jogadas().royal_flush(cartasJogador, cartasMesa)
#     # sf = Jogadas().straight_flush(cartasJogador, cartasMesa)
#     # q = Jogadas().quadra(cartasJogador, cartasMesa)
#     # fh = Jogadas().full_house(cartasJogador, cartasMesa)
#     # fl = Jogadas().flush(cartasJogador, cartasMesa)
#     # s = Jogadas().straight(cartasJogador, cartasMesa)
#     # t = Jogadas().trinca(cartasJogador, cartasMesa)
#     # dd = Jogadas().duas_duplas(cartasJogador, cartasMesa)
#     # d = Jogadas().dupla(cartasJogador, cartasMesa)

#     print(i)
#     i+=1

# print(cartasJogador)
# print(cartasMesa)
# # print("rf",rf)
# # print("sf",sf)
# # print("q",q)
# # print("fh",fh)
# # print("fl",fl)
# # print("s",s)
# # print("t",t)
# # print("dd",dd)
# # print("d",d)