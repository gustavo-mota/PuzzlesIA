import copy


def printMatriz(Matriz):
    for i in Matriz:
        print(i, '\n')


def matrizClone(MatrizOriginal, MatrizCopiada):
    MatrizOriginal.__matrizAtribuiLinhas__(copy.deepcopy(MatrizCopiada.__linha1__()),
                                           copy.deepcopy(MatrizCopiada.__linha2__()),
                                           copy.deepcopy(MatrizCopiada.__linha3__()))


# transforma uma lista em uma string
def listatoString(lista):
    # remove colchete
    string1 = str(lista).strip('[]')
    # remove virgula e espaço
    for i in range(len(string1)):
        string1 = string1.replace(', ', '')
    return string1


class Matriz:

    def __init__(self):
        self.__matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __retornaMatriz__(self):
        return self.__matriz

    def __matrizEditaPosicao__(self, linha, coluna, valor):
        self.__matriz[linha][coluna] = valor

    def __matrizAtribuiLinhas__(self, linha1=None, linha2=None, linha3=None):
        if linha1 != None:
            self.__matriz[0] = copy.deepcopy(linha1)
        if linha2 != None:
            self.__matriz[1] = copy.deepcopy(linha2)
        if linha3 != None:
            self.__matriz[2] = copy.deepcopy(linha3)

    def __printMatriz__(self):
        printMatriz(self.__matriz)

    def __copiaMatriz__(self, Matriz):  # uma matriz é repassada para ser copiada
        matrizClone(self, Matriz)

    # retorna uma linha especícifca
    def __linha1__(self):
        return self.__matriz[0]

    def __linha2__(self):
        return self.__matriz[1]

    def __linha3__(self):
        return self.__matriz[2]
    # fim das funções de retorno de linha

    def __matrizPosicaoValor__(self, linha, coluna):
        return self.__matriz[linha][coluna]

    # testa os movimentos
    # o teste é por contra-exemplo
    def __moveCima__(self):
        if (
            self.__matrizPosicaoValor__(0, 0) == 0 or
            self.__matrizPosicaoValor__(0, 1) == 0 or
            self.__matrizPosicaoValor__(0, 2) == 0
        ):
            return 0
        else:
            return 1

    def __moveBaixo__(self):
        if (
            self.__matrizPosicaoValor__(2, 0) == 0 or
            self.__matrizPosicaoValor__(2, 1) == 0 or
            self.__matrizPosicaoValor__(2, 2) == 0
        ):
            return 0
        else:
            return 1

    def __moveDir__(self):
        if (
            self.__matrizPosicaoValor__(0, 2) == 0 or
            self.__matrizPosicaoValor__(1, 2) == 0 or
            self.__matrizPosicaoValor__(2, 2) == 0
        ):
            return 0
        else:
            return 1

    def __moveEsq__(self):
        if (
            self.__matrizPosicaoValor__(0, 0) == 0 or
            self.__matrizPosicaoValor__(1, 0) == 0 or
            self.__matrizPosicaoValor__(2, 0) == 0
        ):
            return 0
        else:
            return 1
    # fim das funções de teste de movimento

    # move
    def __deslocaZeroCima__(self):
        # ta copiando em forma de lista
        matrizTemporaria = copy.deepcopy(self)
        linha = -1
        coluna = -1
        # procura
        for i in range(1, 3):
            for j in range(0, 3):
                if (matrizTemporaria.__matrizPosicaoValor__(i, j)) == 0:
                    linha = i
                    coluna = j
        # coleta variável no lugar onde zero se deloca
        var = matrizTemporaria.__matrizPosicaoValor__(linha - 1, coluna)
        # modifica
        matrizTemporaria.__matrizEditaPosicao__(linha - 1, coluna, 0)
        matrizTemporaria.__matrizEditaPosicao__(linha, coluna, var)
        return copy.deepcopy(matrizTemporaria)

    def __deslocaZeroBaixo__(self):
        matrizTemporaria = copy.deepcopy(self)
        linha = -1
        coluna = -1
        # procura
        for i in range(0, 2):
            for j in range(0, 3):
                if matrizTemporaria.__matrizPosicaoValor__(i, j) == 0:
                    linha = i
                    coluna = j
        # coleta variável no lugar onde zero se deloca
        var = matrizTemporaria.__matrizPosicaoValor__(linha + 1, coluna)
        # modifica
        matrizTemporaria.__matrizEditaPosicao__(linha + 1, coluna, 0)
        matrizTemporaria.__matrizEditaPosicao__(linha, coluna, var)
        return copy.deepcopy(matrizTemporaria)

    def __deslocaZeroDireita__(self):
        matrizTemporaria = copy.deepcopy(self)
        linha = -1
        coluna = -1
        # procura
        for i in range(0, 3):
            for j in range(0, 2):
                if matrizTemporaria.__matrizPosicaoValor__(i, j) == 0:
                    linha = i
                    coluna = j
        # coleta variável no lugar onde zero se deloca
        var = matrizTemporaria.__matrizPosicaoValor__(linha, coluna + 1)
        # modifica
        matrizTemporaria.__matrizEditaPosicao__(linha, coluna + 1, 0)
        matrizTemporaria.__matrizEditaPosicao__(linha, coluna, var)
        return copy.deepcopy(matrizTemporaria)

    def __deslocaZeroEsquerda__(self):
        matrizTemporaria = copy.deepcopy(self)
        linha = -1
        coluna = -1
        # procura
        for i in range(0, 3):
            for j in range(1, 3):
                if matrizTemporaria.__matrizPosicaoValor__(i, j) == 0:
                    linha = i
                    coluna = j

        var = matrizTemporaria.__matrizPosicaoValor__(linha, coluna - 1)
        # modifica
        matrizTemporaria.__matrizEditaPosicao__(linha, coluna - 1, 0)
        matrizTemporaria.__matrizEditaPosicao__(linha, coluna, var)
        return copy.deepcopy(matrizTemporaria)
    # fim das funções de deslocamento

    def __testaMatrizSolucao__(self):
        if(
            self.__matriz[0] == [1, 2, 3] and
            self.__matriz[1] == [4, 5, 6] and
            self.__matriz[2] == [7, 8, 0]
        ):
            return 1
        return 0

    def __matrizVetor__(self):
        linha1 = self.__matriz[0]
        linha2 = self.__matriz[1]
        linha3 = self.__matriz[2]
        # transforma cada linha em uma string
        return listatoString(linha1) + listatoString(linha2) + listatoString(linha3)
