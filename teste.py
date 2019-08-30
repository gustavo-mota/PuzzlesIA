from noh import Noh
from Matriz import Matriz
from lista_fechada import Lista_Fechada
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
    matFilho.__matrizAtribuiLinhas__([1,2,3],[4,5,6],[7,8,9])
    pai = Noh(matPai)
    no = Noh(matFilho, pai)
    #print(type(no))
    #no.__printMatrizArmazenada__()
    listaFechada = Lista_Fechada()
    listaFechada.__add__(no)
    #listaFechada.__retornaNoh__(str(no.__matrizVetor__())).__printMatrizArmazenada__()
    #matr = copy.deepcopy(pai.__matrizArmazenada__())
    print(matPai.__matrizPosicaoValor__(1,2))
    '''

main()