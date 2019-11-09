from Lista_Aberta import Lista_Aberta
from noh import *
from funcao_sucessor import Funcao_Sucessor
from Heuristica import Heuristica


def Solucao(conjunto):
    No = conjunto[0]
    while No is not None and No.pai is not None:
        conjunto.append(No.pai)
        No = copy.deepcopy(No.pai)
    return conjunto


def ImprimeSolucao(conjuntoSolucao):
    print("Solução de tamanho: ", len(conjuntoSolucao))
    for i in conjuntoSolucao:
        if i is not None:
            i.matr.__printMatriz__()
            print("\n")


def A_Estrela(NoRaiz):

    ConjuntoSolucao = []
    if testeSolucao(NoRaiz):
        ConjuntoSolucao.append(NoRaiz)
        return Solucao(copy.deepcopy(ConjuntoSolucao))

    ListaAberta = Lista_Aberta()
    ListaAberta.__add__(NoRaiz)
    Break = 0

    while(True):
        No = ListaAberta.__retornaRemoveMenorNo__()
        No_Filhos = Funcao_Sucessor(No)
        for i in range(0, No.__movimentosNumero__()):
            numeroFilho = i
            numeroFilho += 1
            No.__alteraNohIterativo__(numeroFilho,
                                      GeraNoh(copy.deepcopy(No_Filhos[i]),
                                              0, No))

            No.__filhoEspecifico__(numeroFilho).heuristica = Heuristica(
                No.__filhoEspecifico__(numeroFilho)
            )

            if testeSolucao(No.__filhoEspecifico__(numeroFilho)):
                ConjuntoSolucao.append(No.__filhoEspecifico__(numeroFilho))
                Break = 1
                break

            NoAdicionar = No.__filhoEspecifico__(numeroFilho)
            ListaAberta.__add__(NoAdicionar)
        No_Filhos.clear()

        if Break:
            break

    return Solucao(copy.deepcopy(ConjuntoSolucao))
