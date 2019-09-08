from queue import Queue
from lista_fechada import Lista_Fechada
from Lista_Aberta import Lista_Aberta
from noh import *
from funcao_sucessor import Funcao_Sucessor
from Heuristica import Heuristica
from Matriz import Matriz
from A_Estrela import *

def Main():
    print("Main")
    #entrada = [[1,2,0],[4,5,3],[7,8,6]]
    '''
    vá analisar onde a GeraNoh é usada
    pois ela requer a matriz
    e se voicê não mandar a matriz, ela vai gerar um nó a menos
    e um objeto no no lugar de uma matriz
    '''
    entrada = [[4,1,3],[7,2,5],[0,8,6]]
    linha1 = entrada[0]
    linha2 = entrada[1]
    linha3 = entrada[2]
    matriz = Matriz()
    matriz.__matrizAtribuiLinhas__(linha1, linha2, linha3)
    No = Noh(matriz,0)
    No.heuristica = Heuristica(No)
    print("Main, a heuristica do no raiz é ", No.heuristica)
    ImprimeSolucao(A_Estrela(No))


Main()