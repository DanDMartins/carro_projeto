class Carro:
    def __init__(self):
        self.ligado = False
        self.velocidade = 0
        self.marcha = 0
        self.limites = {
        1: (0, 20),
        2: (20, 40),
        3: (40, 60),
        4: (60, 80),
        5: (80, 100),
        6: (100, 120)
    }


    def status(self):
        return f"Carro {'ligado' if self.ligado else 'desligado'}, velocidade: {self.velocidade} km/h, marcha: {self.marcha}"
    
    def ligar(self):
        self.ligado = True
        print("Carro ligado.")

    def desligar(self):
        if self.velocidade == 0 and self.marcha == 0:
            self.ligado = False
            print("Carro desligado.")
        else:
            print("Não é possível desligar o carro enquanto ele está em movimento ou engatado em marcha.")

    def acelerar(self):
        if self.ligado:
            if self.marcha != 0:
                limite_max = self.limites[self.marcha][1]
            else:
                print("Por favor, engate uma marcha antes de acelerar.")
                return    
            if self.velocidade < limite_max:
                self.velocidade += 1
                print(f"Carro acelerado. Velocidade atual: {self.velocidade} km/h")
            else:
                print("Velocidade máxima atingida para a marcha atual.")      
        else:
            print("Carro desligado. Não é possível acelerar.")

    
    def frear(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 1
            print(f"Carro freado. Velocidade atual: {self.velocidade} km/h")
        else:
            print("Carro desligado ou já está parado. Não é possível frear.")

    def virar(self, direcao):
        if self.ligado:
            if self.velocidade > 0 and self.velocidade <= 40:
                print(f"Carro virando para a {direcao}.")
            else:
                print("Carro muito rápido para virar. Reduza a velocidade.")
        else:
            print("Carro desligado. Não é possível virar.")
    
    def trocar_marcha(self, nova_marcha):
        if not self.ligado:
            print("Carro desligado. Não é possível trocar de marcha.")
            return

        if nova_marcha < 0 or nova_marcha > 6:
            print("Marcha inválida.")
            return

        marcha_atual = self.marcha

    # Verifica se está pulando marcha
        if abs(marcha_atual - nova_marcha) != 1:
            print("Não é permitido pular marchas.")
            return

    # Verifica limites de velocidade
    # Marcha 0 só permite velocidade 0
        if nova_marcha == 0 and self.velocidade != 0:
            print("Não é possível engatar ponto morto com o carro em movimento.")
            return

        if nova_marcha != 0:
            limite_min, limite_max = self.limites[nova_marcha]
            if not (limite_min <= self.velocidade <= limite_max):
                print(f"Velocidade atual ({self.velocidade} km/h) não é adequada para a marcha {nova_marcha}.")
                return

        # Se passou por todas as verificações, troca a marcha
        self.marcha = nova_marcha
        print(f"Marcha trocada para {self.marcha}.")

