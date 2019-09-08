from queue import Queue
from lista_fechada import Lista_Fechada
from Lista_Aberta import Lista_Aberta
from noh import *
from funcao_sucessor import Funcao_Sucessor
from Heuristica import Heuristica
from Matriz import Matriz
from A_Estrela import *
from BuscaLargura import *
import copy

'''
    problemas que podem acontecer:
    1 Matrizes copiadas ficam associadas
'''

def main():
    '''
    matPai = Matriz()
    matPai.__matrizAtribuiLinhas__([1,1,1],[2,3,4],[5,3,3])
    matFilho = Matriz()
    matFilho.__matrizAtribuiLinhas__([1,2,3],[4,0,6],[7,8,9])
    pai = Noh(matPai)
    no = Noh(matFilho, pai)
    '''
    '''
    #print(type(no))
    #no.__printMatrizArmazenada__()
    listaFechada = Lista_Fechada()
    listaFechada.__add__(no)
    #listaFechada.__retornaNoh__(str(no.__matrizVetor__())).__printMatrizArmazenada__()
    #matr = copy.deepcopy(pai.__matrizArmazenada__())
    print(matPai.__matrizPosicaoValor__(1,2))
    
    matPai = Matriz()
    matPai.__matrizAtribuiLinhas__([1, 1, 1], [2, 3, 4], [5, 3, 3])
    matIrm = Matriz()
    matIrm.__matrizAtribuiLinhas__([1, 2, 3], [0, 4, 6], [7, 8, 9])
    matFilho = Matriz()
    matFilho.__matrizAtribuiLinhas__([1, 2, 6], [4, 0, 3], [7, 8, 5])
    pai = Noh(matPai, 0)
    no = Noh(matFilho, 0, pai)

    #print(Heuristica(no))
    #no.__printMatrizArmazenada__()
    #matr = copy.deepcopy(matPai.__retornaMatriz__())
    #print(type(matr))
    #print(type(no.__matrizArmazenada__().__matrizPosicaoValor__(1,2)))
    '''
    #entrada = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
    entrada = [[4, 1, 3], [7, 2, 5], [0, 8, 6]] #sete passos
    #entrada = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]

    linha1 = entrada[0]
    linha2 = entrada[1]
    linha3 = entrada[2]
    matriz = Matriz()
    matriz.__matrizAtribuiLinhas__(linha1, linha2, linha3)
    No = Noh(matriz, 0)
    No.heuristica = Heuristica(No)
    print("Main, a heuristica do no raiz é ", No.heuristica)
    lista = Funcao_Sucessor(No)
    ImprimeSolucao(BuscaLargura(No))
main()