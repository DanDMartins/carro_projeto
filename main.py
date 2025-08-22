from carro import Carro

def main():
    carro = Carro()
    
    while True:
        print("\n--- MENU ---")
        print("1. Ligar carro")
        print("2. Desligar carro")
        print("3. Acelerar")
        print("4. Frear")
        print("5. Virar")
        print("6. Trocar marcha")
        print("7. Status")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                carro.ligar()
            case "2":
                carro.desligar()
            case "3":
                carro.acelerar()
            case "4":
                carro.frear()
            case "5":
                direcao = input("Digite a direção (esquerda/direita): ")
                carro.virar(direcao)
            case "6":
                try:
                    nova_marcha = int(input("Digite a nova marcha (0 a 6): "))
                    carro.trocar_marcha(nova_marcha)
                except ValueError:
                    print("Digite um número válido de marcha.")
            case "7":
                print(carro.status())
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
