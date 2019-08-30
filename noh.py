from Matriz import Matriz
#no
class Noh :
    def __init__(self, matr, pai=None, esq=None, dire=None):
        #eu não sei o que tou fazendo aqui
        #agora sim
        self.pai = pai
        self.esq = esq
        self.dire = dire
        self.matr = Matriz()

    def __pai__(self):
        print("Esse e o valor do pai")
        return self.pai.matr

    def __dire__(self):
        print("Esse e o valor do direito")
        #print(self.dire.val)
        return self.dire.matr

    def __esq__(self):
        print("Esse e o valor do esquerdo")
        #print(self.esq.val)
        return self.esq.matr

    def __val__(self):
        print(self.matr)
        return self.matr
    #retorna a matriz em forma de inteiro
    def __matrVetor__(self):
        #usa a conversão da matriz capturando a própria
        #joga no método próprio de matriz
        return self.__val__().matrizVetor()
#no

#dire = Noh(3)
#esq = Noh(1)
#noh = Noh(2, esq, dire)
#print(noh.__esq__())