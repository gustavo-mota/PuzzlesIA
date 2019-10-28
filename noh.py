from Matriz import Matriz
import copy
from functools import total_ordering


# teste solução
def testeSolucao(Noh):
    if Noh.matr.__testaMatrizSolucao__():
        return 1
    return 0


# recebe uma matriz
def GeraNoh(lista, heuristica, pai=None, filho1=None, filho2=None, filho3=None, filho4=None):
    linha1 = copy.deepcopy(lista.__linha1__())
    linha2 = copy.deepcopy(lista.__linha2__())
    linha3 = copy.deepcopy(lista.__linha3__())
    matriz = Matriz()
    matriz.__matrizAtribuiLinhas__(linha1, linha2, linha3)
    no = Noh(matriz, heuristica, pai, filho1, filho2, filho3, filho4)  # deve ter  aheurística ajustada depois
    return no


def CustoAcesso(Noh):
    return 1


def CustoAcessoRaiz(Noh):
    return Noh.custoAcesso


# no
@total_ordering
class Noh:
    def __init__(self, matr, heuristica, pai=None, um=None, dois=None, tres=None, quatro=None):
        self.matr = Matriz()
        self.matr.__copiaMatriz__(matr)
        self.heuristica = heuristica  # A heurística pode ser calculada depois
        if (pai == None):
            self.custoAcesso = 0
        elif (pai != None):
            self.custoAcesso = pai.custoAcesso + 1
        self.pai = pai
        self.um = um
        self.dois = dois
        self.tres = tres
        self.quatro = quatro

    def __printMatrizArmazenada__(self):
        self.matr.__printMatriz__()

    # retorna a matriz em forma de string
    def __matrizVetor__(self):
        return self.matr.__matrizVetor__()

    def __alteraNohIterativo__(self, noAlterar, no):  # a diferença é que não receb o objeto matriz
        if noAlterar == 1:
            self.um = no
        elif noAlterar == 2:
            self.dois = no
        elif noAlterar == 3:
            self.tres = no
        elif noAlterar == 4:
            self.quatro = no

    # numero de filhos
    def __numFilhos__(self):
        if (
            self.um is not None and
            self.dois is None and
            self.tres is None and
            self.quatro is None
        ):
            return 1
        elif (
            self.um is not None and
            self.dois is not None and
            self.tres is None and
            self.quatro is None
        ):
            return 2
        elif (
            self.um is not None and
            self.dois is not None and
            self.tres is not None and
            self.quatro is None
        ):
            return 3
        elif (
            self.um is not None and
            self.dois is not None and
            self.tres is not None and
            self.quatro is not None
        ):
            return 4
        return 0

    def __movimentosNumero__(self):
        if self.pai is None:
            return (self.matr.__moveBaixo__() +
                    self.matr.__moveCima__() +
                    self.matr.__moveDir__() +
                    self.matr.__moveEsq__())
        return (self.matr.__moveBaixo__() +
                self.matr.__moveCima__() +
                self.matr.__moveDir__() +
                self.matr.__moveEsq__() - 1)

    def __filhoEspecifico__(self, numeroFilho):
        if numeroFilho == 1:
            return self.um
        elif numeroFilho == 2:
            return self.dois
        elif numeroFilho == 3:
            return self.tres
        elif numeroFilho == 4:
            return self.quatro
        else:
            print("noh, __filhoEspecifico__() \n "
                  "O numero passado não corresponde a  um filho existente")
            return -1

    def __eq__(self, other):
        if other is not None:
            if (self.custoAcesso + self.heuristica) == (other.custoAcesso + other.heuristica):
                return 1
            return 0
        return 0

    def __lt__(self, other):
        if other is not None:
            if (self.custoAcesso + self.heuristica) < (other.custoAcesso + other.heuristica):
                return 1
            return 0
        return 0
    # no
