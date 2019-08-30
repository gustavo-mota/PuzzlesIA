from noh import Noh
from Matriz import Matriz #toda operação d ematriz deve cincuir copy
import copy
#from funcao_sucessor import *

def Funcao_Sucessor(Noh, Lista_Fechada):
    #você sabe que só existe um só 0 nele
    #necessário usar o copy para modificar sem alterar o original
    matr = copy.deepcopy(Noh.__matrizArmazenada__())
    lista = []
    lista.append(
        {
            matr.__moveCima__() == 1 : matr.__deslocaZeroCima__(),
            matr.__moveBaixo__() == 1: matr.__deslocaZeroBaixo__() ,
            matr.__moveDir__() == 1 : matr.__deslocaZeroDireita__() ,
            matr.__moveEsq__() == 1 : matr.__deslocaZeroEsquerda__()
        }[matr]
    )
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