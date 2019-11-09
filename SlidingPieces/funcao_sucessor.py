import copy
# recebe lista fechada e o noh


def Funcao_Sucessor(Noh): # testa repetição apenas para o pai
    matr = copy.deepcopy(Noh.matr)
    lista = []
    # Gera matrizes de movimentos possíveis
    if matr.__moveCima__() == 1:
        lista.append(copy.deepcopy(matr.__deslocaZeroCima__()))

    if matr.__moveBaixo__() == 1:
        lista.append(copy.deepcopy(matr.__deslocaZeroBaixo__()))

    if matr.__moveDir__() == 1:
        lista.append(copy.deepcopy(matr.__deslocaZeroDireita__()))

    if matr.__moveEsq__() == 1:
        lista.append(copy.deepcopy(matr.__deslocaZeroEsquerda__()))
    # fim da geração de matrizes de movimentos
    for i in lista:
        if(
            Noh.pai is not None and
            i.__matrizVetor__() == Noh.pai.matr.__matrizVetor__()
        ):
            lista.remove(i)

    return lista
