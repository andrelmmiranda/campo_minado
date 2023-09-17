from random import randint

class Campo_minado:
    n=0 
    fim_de_jogo = False
    nova_partida = True

    def __init__(self) -> None:
        pass

    def iniciar_jogo(self) -> None:
        self.jogada()
        
    # funcao de jogada - 
    # controla a acao de envio de coordenadas do jogador
    # controla as rodadas em que o jogador joga
    def jogada(self) -> None:
        
        while self.nova_partida == True:
            mapa = []
            minas = []

            self.entrada()
            print()
            self.cria_mapa(mapa)
            self.cria_minas(minas)

            n_jogadas = 0
            jogadas = []

            while self.fim_de_jogo == False:
                teste = True
                while teste == True:
                    print()
                    entrada = input('Digite a coordenada do ponto a ser revelado [x, y]. ex: 2,1: ')

                    if entrada not in jogadas:
                        teste = False
                        jogadas.append(entrada)
                        n_jogadas+=1

                existe = self.verifica_minas(entrada, minas)
                        
                if existe == True:
                    print()
                    print('DEU RUIM... A mina explodiu!!')
                    self.fim_de_jogo = True
                    self.revela_minas(minas, mapa)
                    self.printa_mapa(mapa)
                    break
                else:
                    [x, y] = entrada.split(',')
                    mapa[int(y) + 1][int(x) + 1] = 'X'
                    self.printa_mapa(mapa)

                if n_jogadas == (self.n**2)-self.n:
                    print('você venceu!!')
                    self.fim_de_jogo = True
                    break

            print()
            resposta = input("Gostaria de jogar uma nova partida [s/n]? ")

            if resposta == 's':
                self.fim_de_jogo = False
                print('Bom jogo!')
                print()
            elif resposta == 'n':
                self.nova_partida = False
                print("Até a próxima partida!")
                return 0


    #funcao para revelar a posicao das minas no final do jogo
    def revela_minas(self, minas:list, mapa:list) -> None:
        for mina_coordenadas in minas:
            [x, y] = mina_coordenadas.split(',')
            mapa[int(y) +1][int(x) +1] = '*'

    # funcao para verificar se as coordenadas enviadas pelo jogador 
    # sao diferentes de onde tem mina
    def verifica_minas(self, entrada:str, minas:list) -> bool:
        for mina_coordenadas in minas:
            [a, b] = mina_coordenadas.split(',')
            [x, y] = entrada.split(',')

            existe = (f"{int(a)} {int(b)}" == f"{int(x)} {int(y)}")

            if existe == True:
                return True
            
        return False
    
    # input inicial para o jogador definir o tamanho da matriz
    def entrada(self) -> None:
        self.n = int(input("Digite um numero maior igual a 2 para iniciar o jogo: "))

    # funcao de criacao do mapa de acordo com o input inicial
    def cria_mapa(self, mapa:list) -> None:
        for i in range(self.n + 1):
            linha = []
            for j in range(self.n + 1):
                if j == 0 and i == 0:
                    linha.append(self.formatar_caracter('+'))
                elif j > 0 and i > 0:
                    linha.append(self.formatar_caracter(''))
                else:
                    linha.append(self.formatar_caracter(j + i - 1))
            mapa.append(linha)

        
        self.printa_mapa(mapa)
    
    #formata os caracteres para evitar que a aparencia da matriz fique quebrada
    def formatar_caracter(self, caracter) -> str:
        return str(caracter).rjust(len(str(self.n)))

    # funcao de impressão do mapa
    def printa_mapa(self, mapa:list) -> None:
        print()
        print('Campo Minado')
        for linha in mapa:
            print(linha)

    # funcao de criacao das coordenadas das minas
    def cria_minas(self, minas:list) -> None:
        i = 0
        while i < self.n:
            mina = f"{randint(0, self.n -1)}, {randint(0, self.n -1)}"
            if mina not in minas:
                minas.append(str(mina))
                i+=1

if __name__ == '__main__':
    Campo_minado().iniciar_jogo()