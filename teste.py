from queue import Queue
from noh import Noh
import hashlib
from Matriz import Matriz
def Main():
    '''esq = Noh(5)
    dire = Noh(3)
    noh = Noh(2, None, esq, dire)
    h = {'0823032':noh, '391931':esq,'3892893289':dire}
    #print(noh.__dire__())
    print(h['0823032'].__esq__())

    A = geraInstantaneo(3, 3, 0)
    B = [ [1,2,3], [4,5,6] ,[7,8,0]]

    A[1][1] = 2
    printMatriz(A)
    printMatriz(B)
    matrizAtribuiLinha(A,B)
    printMatriz(A)'''
    lista = [1,2,3]
    string1 = str(lista).strip('[]')
    for i in range(len(string1)):
        string1 = string1.replace(', ','')
    string1.strip(',')
    print(string1)


Main() #31-9-1931