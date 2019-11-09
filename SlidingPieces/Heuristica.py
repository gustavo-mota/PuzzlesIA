from Matriz import Matriz
import copy


def distancia(listaPosicaoAtual, listaPosicaoSolucao):
    if (
            int(str(listaPosicaoAtual[0]) + str(listaPosicaoAtual[1])) <
            int(str(listaPosicaoSolucao[0]) + str(listaPosicaoSolucao[1]))
    ):
        return (
                abs((listaPosicaoSolucao[0] - listaPosicaoAtual[0])) +
                abs((listaPosicaoSolucao[1] - listaPosicaoAtual[1]))
        )
    elif (
            int(str(listaPosicaoAtual[0]) + str(listaPosicaoAtual[1])) >
            int(str(listaPosicaoSolucao[0]) + str(listaPosicaoSolucao[1]))
    ):
        return (
                abs((listaPosicaoAtual[0] - listaPosicaoSolucao[0])) +
                abs((listaPosicaoAtual[1] - listaPosicaoSolucao[1]))
        )
    else:
        return 0


def Heuristica(Noh): # Manhattan
    Distancias = 0
    # comparador para calcular distância
    dictPosicoesValorSolucao = {0: [2, 2], 1: [0, 0], 2: [0, 1],
                                3: [0, 2], 4: [1, 0], 5: [1, 1],
                                6: [1, 2], 7: [2, 0], 8: [2, 1]}
    matriz2 = Matriz()
    matriz2.__copiaMatriz__(Noh.matr)
    matriz = copy.deepcopy(matriz2.__retornaMatriz__())
    # salva as posições
    listaTodosIndices = []
    listaTodosVal = []
    for i in range(0, 3):
        for j in range(0, 3):
            lista_indices = []  # lista temporária para cada posição
            listaTodosVal.append(matriz[i][j])  # salva o valor da posição
            # posições valor
            lista_indices.append(i)
            lista_indices.append(j)
            # salva as posições na lista
            listaTodosIndices.append(copy.deepcopy(lista_indices))
            # reseta a variável
            lista_indices.clear()
    # fim salva as posições

    # gera dicionario
    dictPosicoesValorAtual = dict(zip(listaTodosVal, listaTodosIndices))  # cada valor e sua posição

    # Calcula distancia somando de cada posicao
    for i in range(0, 9):
        if i == 0:
            Distancias += (distancia(
                dictPosicoesValorAtual[0],
                dictPosicoesValorSolucao[0]
            ))
        if i == 1:
            Distancias += (distancia(
                dictPosicoesValorAtual[1],
                dictPosicoesValorSolucao[1]
            ))
        if i == 2:
            Distancias += (distancia(
                dictPosicoesValorAtual[2],
                dictPosicoesValorSolucao[2]
            ))
        if i == 3:
            Distancias += (distancia(
                dictPosicoesValorAtual[3],
                dictPosicoesValorSolucao[3]
            ))
        if i == 4:
            Distancias += (distancia(
                dictPosicoesValorAtual[4],
                dictPosicoesValorSolucao[4]
            ))
        if i == 5:
            Distancias += (distancia(
                dictPosicoesValorAtual[5],
                dictPosicoesValorSolucao[5]
            ))
        if i == 6:
            Distancias += (distancia(
                dictPosicoesValorAtual[6],
                dictPosicoesValorSolucao[6]
            ))
        if i == 7:
            Distancias += (distancia(
                dictPosicoesValorAtual[7],
                dictPosicoesValorSolucao[7]
            ))
        if i == 8:
            Distancias += (distancia(
                dictPosicoesValorAtual[8],
                dictPosicoesValorSolucao[8]
            ))

    return Distancias
