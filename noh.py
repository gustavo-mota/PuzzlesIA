from Matriz import Matriz
#no
class Noh :
    def __init__(self, matr, pai=None, um=None, dois=None, tres=None, quatro=None):
        #eu não sei o que tou fazendo aqui
        #agora sim
        self.pai = pai
        self.um = um
        self.dois = dois
        self.tres = tres
        self.quatro = quatro
        self.matr = Matriz()
        self.matr.__copiaMatriz__(matr) #estou desconfiado
        '''
        if(self.matr == matr):
            self.matr = matr
        else:
            self.matr = Matriz()
        '''
    #esses aqui devem retornar os nós e não o conteúdo
    #não se conhece o motivo deles existirem
    def __pai__(self):
        #print("Esse e o valor do pai")
        return self.pai.__matrizArmazenada__()

    def __um__(self):
        #print("Esse e o valor do um")
        #print(self.esq.val)
        return self.um.__matrizArmazenada__()

    def __dois__(self):
        #print("Esse e o valor do dois")
        #print(self.dois.val)
        return self.dois.__matrizArmazenada__()

    def __tres__(self):
        #print("Esse e o valor do um")
        #print(self.esq.val)
        return self.tres.__matrizArmazenada__()

    def __quatro__(self):
        #print("Esse e o valor do um")
        #print(self.esq.val)
        return self.quatro.__matrizArmazenada__()
    #eu honestamente não entendo o que ele retorna acima
    #retorna o objeto matriz desses caras, mas tem forma alternativa e noa tem utilidade para eles
    #retorno da matriz
    def __matrizArmazenada__(self):
        #print(self.matr)
        return self.matr
    #print matriz
    def __printMatrizArmazenada__(self):
        self.matr.__printMatriz__()
    #retorna a matriz em forma de inteiro
    #retorna a matriz em forma de inteiro
    def __matrizVetor__(self):
        #usa a conversão da matriz capturando a própria
        #joga no método próprio de matriz
        return self.__matrizArmazenada__().__matrizVetor__()
#no

#dois = Noh(3)
#esq = Noh(1)
#noh = Noh(2, esq, dire)
#print(noh.__esq__())