#from queue import Queue
#from noh import Noh
#import hashlib
#from Matriz import Matriz

#este trecho foi copiado
def matrizGera(n_linhas, n_colunas, valor):
    A = []
    for i in range(n_linhas):
        A.append([0] * n_colunas)
    return A
#trecho copiado terminado
def printMatriz(Matriz):
    for i in Matriz:
        print(i, '\n')

# o propósito é fazer atribuição de matrizes
def matrizClone(MatrizOriginal, MatrizCopiada):  # cada linha será substituida por outra
    for i in range(len(MatrizOriginal)):
        MatrizOriginal[i - 1] = MatrizCopiada[i - 1]
#transforma uma lista em uma string
def listatoString(lista):
    string1 = str(lista).strip('[]') #remove colchete
    #remove virgula e espaço
    for i in range(len(string1)):
        string1 = string1.replace(', ', '')
    return string1

class Matriz:
    #inicia matriz zero
    def __init__(self):
        self.__matriz = [[0,0,0],[0,0,0],[0,0,0]]
    def __retornaMatriz__(self):
        return self.__matriz
    #atribui a matriz
    #edita uma posição específica
    def __matrizEditaPosicao__(self, linha, coluna, valor):
        self.__matriz[linha][coluna] = valor
    #Atribui linhas
    def __matrizAtribuiLinhas__(self, linha1=None,linha2=None,linha3=None):
        if(linha1!=None):
            self.__matriz[0] = linha1
        if(linha2!=None):
            self.__matriz[1] = linha2
        if(linha3!=None):
            self.__matriz[2] = linha3
    #cria matriz nova
    #usa método copiaMatri
    #cria método qu ealetar uma linha apenas da matriz

    #imprime a matriz
    def __printMatriz__(self):
        printMatriz(self.__matriz)
    #clona a matriz
    def __copiaMatriz(self, Matriz):
        matrizClone(self.__matriz, Matriz)
    #faz uma matriz virar um vetor numérico
    def __matrizVetor__(self):
        linha1 = self.__matriz[0]
        linha2 = self.__matriz[1]
        linha3 = self.__matriz[2]
        #transforma cada linha em uma string
        return int(listatoString(linha1) + listatoString(linha2) + listatoString(linha3))

def Main():

    matr = Matriz()
    matr.__printMatriz__()
    linha = [1,1,10]
    matr.__matrizAtribuiLinhas__(linha)
    matr.__printMatriz__()
    intei = matr.__matrizVetor__()
    print(intei)
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
    printMatriz(A)
    lista = [1,2,3]
    string1 = str(lista).strip('[]')
    for i in range(len(string1)):
        string1 = string1.replace(', ','')
    string1.strip(',')
    print(string1)'''


Main() #31-9-1931

#teste 2
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
        self.matr.__copiaMatriz__(matr) #estou desconfiado

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
#no
def Main():
    matri = Matriz()
    print("deu certo 1")
    a = [[0,0,0],[0,0,0],[0,0,0]]
    #essa clonagem nao deu certo
    print("deu certo 2")
    matri.__copiaMatriz__(a)
    print("deu certo 3")
    matri.__printMatriz__()
    print("deu certo 4")
    no = Noh(matri.__retornaMatriz__())
    print("deu certo 5")
    no.__printMatrizArmazenada__()
    print("deu certo 6")
    num = no.__matrizVetor__()
    print("deu certo 7")
    print(num)

Main()
#dire = Noh(3)
#esq = Noh(1)
#noh = Noh(2, esq, dire)
#print(noh.__esq__())

#teste 3
matr1 = Matriz()
matr2 = Matriz()
print("matrizes criadas")
matr1.__printMatriz__()
matr2.__printMatriz__()
matr2.__matrizEditaPosicao__(1, 1, 10)
print("posicao matriz 2 modficiada")
matr2.__printMatriz__()
print("matriz 2 impressa")
matr1.__copiaMatriz__(matr2)
print("matriz 1 copiou a 2")
matr2.__matrizEditaPosicao__(1, 1, 20)
print("matriz 2 modificou a posição")
matr2.__printMatriz__()
print("matriz 2 impressa")

matr1.__printMatriz__()
print("matriz 1 impressa")

#teste 4
matri = Matriz()
matri.__matrizAtribuiLinhas__([0,1,2], [3,4,5],[6,7,8])
no = Noh(matri)
print(type(str(no.__matrizVetor__())))