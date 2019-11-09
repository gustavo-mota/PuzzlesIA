from queue import Queue
from A_Estrela import *
import copy


def BuscaLargura(Noh):

    conjuntoSolucao = []
    if testeSolucao(Noh):
        conjuntoSolucao.append(Noh)
        return Solucao(copy.deepcopy(conjuntoSolucao))

    Borda = Queue()
    Borda.__add__(copy.deepcopy(Noh))
    while Borda.is_empty()==1: #1 para cheia 0 vazia
        Break = 0
        No = Borda.Remove() #exatrai no de fila e remove

        Nos_Filhos = Funcao_Sucessor(No)
        for i in range(0, No.__movimentosNumero__()):
            numeroFilho = i
            numeroFilho += 1

            No.__alteraNohIterativo__(numeroFilho,
                                      GeraNoh(copy.deepcopy(Nos_Filhos[i]),
                                              0, No))

            if testeSolucao(No.__filhoEspecifico__(numeroFilho)):
                conjuntoSolucao.append(No.__filhoEspecifico__(numeroFilho))
                Break = 1
                break
            Borda.__add__(No.__filhoEspecifico__(numeroFilho))

        Nos_Filhos.clear()
        if Break:
            break
    return Solucao(copy.deepcopy(conjuntoSolucao))

