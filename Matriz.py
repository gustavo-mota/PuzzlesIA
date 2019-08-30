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
    #atribui a matriz
    def __atr__(self, linha1,linha2,linha3):
        #cria matriz nova
        #essa recebe os elementos
        #usa método copiaMatri
    #cria método que modifica uma posição específica da matriz
    #cria método qu ealetar uma linha apenas da matriz

    #imprime a matriz
    def __printMatriz__(self):
        printMatriz(self.__matriz)
    #clona a matriz
    def __copiaMatriz(self, Matriz):
        matrizClone(self.__matriz, Matriz)
    #faz uma matriz virar um vetor numérico
    def _matrizVetor(self):
        linha1 = self.__matriz[0]
        linha2 = self.__matriz[1]
        linha3 = self.__matriz[2]
        #transforma cada linha em uma string
        return int(listatoString(linha1) + listatoString(linha2) + listatoString(linha3))