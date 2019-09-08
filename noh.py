from Matriz import Matriz
import copy

#teste solução
def testeSolucao(Noh):
    if(Noh.__matrizArmazenada__().__testaMatrizSolucao__()):
        return 1
    return 0

#recebe uma matriz
def GeraNoh(lista, heuristica, pai=None, filho1=None, filho2=None, filho3=None, filho4=None): #a diferença é que não receb o objeto matriz
    linha1 = copy.deepcopy(lista.__linha1__())
    linha2 = copy.deepcopy(lista.__linha2__())
    linha3 = copy.deepcopy(lista.__linha3__())
    matriz = Matriz()
    matriz.__matrizAtribuiLinhas__(linha1, linha2, linha3)
    no = Noh(matriz, heuristica, pai, filho1, filho2, filho3, filho4) #deve ter  aheurística ajustada depois
    return no

#no
class Noh :
    #o no deve receber uma heurística; como são calculadas após sua criação
    #as heurísticas podem ser passadas com valor zero e depois ajustadas
    def __init__(self, matr, heuristica, pai=None, um=None, dois=None, tres=None, quatro=None):
        #eu não sei o que tou fazendo aqui
        #agora sim
        self.matr = Matriz()
        self.matr.__copiaMatriz__(matr)  # estou desconfiado
        self.heuristica = heuristica
        self.custoAcesso = 1
        self.pai = pai
        self.um = um
        self.dois = dois
        self.tres = tres
        self.quatro = quatro
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
    #altera filhos; a função requer pelo menos um filho novo para ser chamada
    def __alteraFilhos__(self, filho1, filho2=None, filho3=None, filho4=None):
        self.um = filho1
        self.dois = filho2
        self.tres = filho3
        self.quatro = filho4
    #retorna o objeto matriz desses caras, mas tem forma alternativa e noa tem utilidade para eles
    #retorno da matriz
    def __matrizArmazenada__(self):
        #print(self.matr)
        return self.matr
    #print matriz
    def __printMatrizArmazenada__(self):
        self.matr.__printMatriz__()
    #retorna a matriz em forma de inteiro
    def __matrizVetor__(self):
        #usa a conversão da matriz capturando a própria
        #joga no método próprio de matriz
        return self.__matrizArmazenada__().__matrizVetor__()

    def __alteraNohIterativo__(self, noAlterar, no):  # a diferença é que não receb o objeto matriz
        if(noAlterar==1):
            self.um = no
        elif(noAlterar == 2):
            self.dois = no
        elif(noAlterar == 3):
            self.tres = no
        elif (noAlterar == 4):
            self.quatro = no

    def __retornaNohIterativo__(self, noRetornar):
        if(noRetornar==1):
            return self.um
        elif(noRetornar==2):
            return self.dois
        elif(noRetornar==3):
            return self.tres
        elif(noRetornar==4):
            return self.quatro
    #numero de filhos
    def __numFilhos__(self):
        if( self.um !=  None and
            self.dois == None and
            self.tres == None and
            self.quatro == None):
            return 1
        elif(   self.um !=  None and
                self.dois != None and
                self.tres == None and
                self.quatro == None):
            return 2
        elif(   self.um !=  None and
                self.dois != None and
                self.tres != None and
                self.quatro == None):
            return 3
        elif(   self.um !=  None and
                self.dois != None and
                self.tres != None and
                self.quatro != None):
            return 4
        return 0

    def __movimentosNumero__(self):
        if(self.pai == None):
            return (self.matr.__moveBaixo__() +
                    self.matr.__moveCima__() +
                    self.matr.__moveDir__() +
                    self.matr.__moveEsq__())
        return (self.matr.__moveBaixo__() +
                self.matr.__moveCima__() +
                self.matr.__moveDir__() +
                self.matr.__moveEsq__() - 1)

    def __filhoEspecifico__(self, numeroFilho):
        if(numeroFilho==1):
            return self.um
        elif(numeroFilho==2):
            return self.dois
        elif(numeroFilho==3):
            return self.tres
        elif(numeroFilho==4):
            return self.quatro
        else:
            print("noh, __filhoEspecifico__() \n "
                  "O numero passado não corresponde a  um filho existente")
            return -1
    #no

#dois = Noh(3)
#esq = Noh(1)
#noh = Noh(2, esq, dire)
#print(noh.__esq__())