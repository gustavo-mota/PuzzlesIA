import copy

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
    #captura a slinhas dos dois e clona
    #cria variavel queu recebe copia
    lista1 = copy.deepcopy(MatrizCopiada.__linha1__())
    lista2 = copy.deepcopy(MatrizCopiada.__linha2__())
    lista3 = copy.deepcopy(MatrizCopiada.__linha3__())

    MatrizOriginal.__matrizAtribuiLinhas__( copy.deepcopy(MatrizCopiada.__linha1__()),
                                            copy.deepcopy(MatrizCopiada.__linha2__()),
                                            copy.deepcopy(MatrizCopiada.__linha3__()))

    # var = copy.deepcopy(matriz)
    '''for i in range(len(MatrizOriginal)):
        MatrizOriginal[i - 1] = MatrizCopiada[i - 1]'''
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
            self.__matriz[0] = copy.deepcopy(linha1)
        if(linha2!=None):
            self.__matriz[1] = copy.deepcopy(linha2)
        if(linha3!=None):
            self.__matriz[2] = copy.deepcopy(linha3)
    #cria matriz nova
    #usa método copiaMatri
    #cria método qu ealetar uma linha apenas da matriz

    #imprime a matriz
    def __printMatriz__(self):
        printMatriz(self.__matriz)
    #clona a matriz
    def __copiaMatriz__(self, Matriz):
        matrizClone(self, Matriz)
    #faz uma matriz virar um vetor numérico
    #retorna uma linha especícifca
    def __linha1__ (self):
        return self.__matriz[0]
    def __linha2__ (self):
        return self.__matriz[1]
    def __linha3__ (self):
        return self.__matriz[2]
    #fim das funções de retorno de linha
    #retorna o valor d euma posição específica
    def __matrizPosicaoValor__(self, linha, coluna):
        return self.__matriz[linha][coluna]
    #testa os movimentos
    #o teste é por contra-exemplo
    def __moveCima__(self):
        if(
            matr.__matrizPosicaoValor__(0,0) == 0 or
            matr.__matrizPosicaoValor__(0,1) == 0 or
            matr.__matrizPosicaoValor__(0,2) == 0
        ):
            return 0
        else:
            return 1
    def __moveBaixo__(self):
        if(
            matr.__matrizPosicaoValor__(2,0) == 0 or
            matr.__matrizPosicaoValor__(2,1) == 0 or
            matr.__matrizPosicaoValor__(2,2) == 0
        ):
            return 0
        else:
            return 1
    def __moveDir__(self):
        if(
            matr.__matrizPosicaoValor__(0,2) == 0 or
            matr.__matrizPosicaoValor__(1,2) == 0 or
            matr.__matrizPosicaoValor__(2,2) == 0
        ):
            return 0
        else:
            return 1
    def __moveEsq__(self):
        if(
            matr.__matrizPosicaoValor__(0,0) == 0 or
            matr.__matrizPosicaoValor__(1,0) == 0 or
            matr.__matrizPosicaoValor__(2,0) == 0
        ):
            return 0
        else:
            return 1
    #fim das funções de teste de movimento
    #move
    def __deslocaZeroCima__(self):
        matrizTemporaria = copy.deepcopy(self.__matriz)
        linha = -1
        coluna = -1
        #procura
        for i in (1,2):
            for j in (0,2):
                if(matrizTemporaria.__matrizPosicaoValor__(i,j) == 0):
                    linha = i
                    coluna = j
        #coleta variável no lugar onde zero se deloca
        var = matrizTemporaria.__matrizPosicaoValor(linha-1,coluna)
        #modifica
        matrizTemporaria.__matrizEditaPosicao__(linha-1,coluna,0)
        matrizTemporaria.__matrizEditaPosicao__(linha, coluna, var)
        return copy.deepcopy(matrizTemporaria)
    def __deslocaZeroBaixo__(self):
        matrizTemporaria = copy.deepcopy(self.__matriz)
        linha = -1
        coluna = -1
        #procura
        for i in (0,1):
            for j in (0,2):
                if(matrizTemporaria.__matrizPosicaoValor__(i,j) == 0):
                    linha = i
                    coluna = j
        #coleta variável no lugar onde zero se deloca
        var = matrizTemporaria.__matrizPosicaoValor(linha+1,coluna)
        #modifica
        matrizTemporaria.__matrizEditaPosicao__(linha+1,coluna,0)
        matrizTemporaria.__matrizEditaPosicao__(linha, coluna, var)
        return copy.deepcopy(matrizTemporaria)
    def __deslocaZeroDireita__(self):
        matrizTemporaria = copy.deepcopy(self.__matriz)
        linha = -1
        coluna = -1
        #procura
        for i in (0,2):
            for j in (0,1):
                if(matrizTemporaria.__matrizPosicaoValor__(i,j) == 0):
                    linha = i
                    coluna = j
        #coleta variável no lugar onde zero se deloca
        var = matrizTemporaria.__matrizPosicaoValor(linha,coluna+1)
        #modifica
        matrizTemporaria.__matrizEditaPosicao__(linha,coluna+1,0)
        matrizTemporaria.__matrizEditaPosicao__(linha, coluna, var)
        return copy.deepcopy(matrizTemporaria)
    def __deslocaZeroEsquerda__(self):
        matrizTemporaria = copy.deepcopy(self.__matriz)
        linha = -1
        coluna = -1
        #procura
        for i in (1,2):
            for j in (1,2):
                if(matrizTemporaria.__matrizPosicaoValor__(i,j) == 0):
                    linha = i
                    coluna = j
        #coleta variável no lugar onde zero se deloca
        var = matrizTemporaria.__matrizPosicaoValor(linha,coluna-1)
        #modifica
        matrizTemporaria.__matrizEditaPosicao__(linha,coluna-1,0)
        matrizTemporaria.__matrizEditaPosicao__(linha, coluna, var)
        return copy.deepcopy(matrizTemporaria)
    #fim das funções de deslocamento
    #retorna a matriz em vetor
    def __matrizVetor__(self):
        linha1 = self.__matriz[0]
        linha2 = self.__matriz[1]
        linha3 = self.__matriz[2]
        #transforma cada linha em uma string
        return int(listatoString(linha1) + listatoString(linha2) + listatoString(linha3))
        #experimente o retorn sem o int()