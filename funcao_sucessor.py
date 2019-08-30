from noh import Noh
from Matriz import Matriz #toda operação d ematriz deve cincuir copy
import copy
#from funcao_sucessor import *

def Funcao_Sucessor(Noh):
    #você sabe que só existe um só 0 nele
    #necessário usar o copy para modificar sem alterar o original
    matr = copy.deepcopy(Noh.__matrizArmazenada__())
    lista = []
    #ifs testados
    #saída testada
    if(matr.__moveCima__() == 1):
        lista.append(matr.__deslocaZeroCima__())
        print("moveu cima")
    if(matr.__moveBaixo__() == 1):
        lista.append(matr.__deslocaZeroBaixo__())
        print("moveu baixo")
    if(matr.__moveDir__() == 1):
        lista.append(matr.__deslocaZeroDireita__())
        print("moveu direita")
    if(matr.__moveEsq__() == 1):
        lista.append(matr.__deslocaZeroEsquerda__())
        print("moveu esquerda")

    for i in lista:
        if(
            #deve receber lista fechada
            #supõe que a função retorna em int
            #testa se i vale como matriz
            Lista_Fechada.__verifica__(str(i.__matrizVetor__()))
        ):
            lista.remove(i)
        else:
            None
    return lista