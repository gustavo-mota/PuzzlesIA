from queue import Queue
from lista_fechada import Lista_Fechada
from Lista_Aberta import Lista_Aberta
from noh import *
from funcao_sucessor import Funcao_Sucessor
from Heuristica import Heuristica
from Matriz import Matriz
from A_Estrela import *
import copy

'''
BuscaEmLargura
   escolha uma raiz s de G
   marque s
   insira s em F
   enquanto F não está vazia faça
      seja v o primeiro vértice de F
      para cada w ∈ listaDeAdjacência de v faça
         se w não está marcado então
            visite aresta entre v e w
            marque w
            insira w em F
         senao se w ∈ F entao
            visite aresta entre v e w
         fim se
      fim para
      retira v de F
   fim enquanto
'''
def BuscaLargura(Noh):
    Fila = Queue()
    Fila.__add__(copy.deepcopy(Noh))
    Fila.__print__()
    print("fila pirnt")
    ListaFechada = Lista_Fechada()
    ListaFechada.__add__(Noh)
    conjuntoSolucao = []
    No_Filhos = Funcao_Sucessor(Noh)
    for i in range(0, len(No_Filhos)):
        numeroFilho = i
        numeroFilho += 1
        Noh.__alteraNohIterativo__(numeroFilho, copy.deepcopy(GeraNoh(No_Filhos[i], 0, Noh))) #problema maior
        Fila.__add__(copy.deepcopy(GeraNoh(No_Filhos[i], 0, Noh))) #resetar lá dentro
    Fila.__print__()
    print("Fila impressa \n")
    #gera nós de raiz
    #salva esses nós
    #salva número em variável para o for
    iteracao = 0
    while(Fila.is_empty()==1):
        print("Busca em largura, iteração :", iteracao)
        Break = 0
        No = Fila.Remove() #exatrai no de fila e remove
        print("Nó extraído da fila\n", No)
        Fila.__print__()
        No_Filhos.clear()
        Fila.__print__()
        #for i in range(0, No.__numFilhos__()): #para cada filho de nó

        #como vai estar definido na proxma iteração
        #para cada filho de nó:
        if(No.__numFilhos__()==1): #caso 1 filho
            if(testeSolucao(No.um)):
                conjuntoSolucao.append(copy.deepcopy(No.um))
                Break = 1
            else:
                # gera os filhos dos quatro
                # salva os filhos na fila
                No_Filhos = Funcao_Sucessor(No)
                for j in range(0, len(No_Filhos)):  # esse loop deve ter 1 itera
                    numeroFilho = j
                    numeroFilho += 1
                    No.__alteraNohIterativo__(numeroFilho, GeraNoh(No_Filhos[j], 0, No))
                    Fila.__add__(GeraNoh(No_Filhos[j], 0, No))  # isso pode dar problemas

            ListaFechada.__add__(No.um)
        if (No.__numFilhos__() == 2):  #caso 2 filhos
            if (testeSolucao(No.um)):
                conjuntoSolucao.append(copy.deepcopy(No.um))
                Break = 1
            elif(testeSolucao(No.dois)):
                conjuntoSolucao.append(copy.deepcopy(No.dois))
                Break = 1
            else:
                # gera os filhos dos quatro
                # salva os filhos na fila
                No_Filhos = Funcao_Sucessor(No)
                for k in range(0, len(No_Filhos)):  # esse loop deve ter 2 itera
                    numeroFilho = k
                    numeroFilho += 1
                    No.__alteraNohIterativo__(numeroFilho, GeraNoh(No_Filhos[k], 0, No))
                    Fila.__add__(GeraNoh(No_Filhos[k], 0, No))  # isso pode dar problemas
            ListaFechada.__add__(No.um)
            ListaFechada.__add__(No.dois)

        if (No.__numFilhos__() == 3):  #caso 3 filhos
            if (testeSolucao(No.um)):
                conjuntoSolucao.append(copy.deepcopy(No.um))
                Break = 1
            elif(testeSolucao(No.dois)):
                conjuntoSolucao.append(copy.deepcopy(No.dois))
                Break = 1

            elif(testeSolucao(No.tres)):
                conjuntoSolucao.append(copy.deepcopy(No.tres))
                Break = 1
            else:
                # gera os filhos dos quatro
                # salva os filhos na fila
                No_Filhos = Funcao_Sucessor(No)
                for l in range(0, len(No_Filhos)):  # esse loop deve ter 3 itera
                    numeroFilho = l
                    numeroFilho += 1
                    No.__alteraNohIterativo__(numeroFilho, GeraNoh(No_Filhos[l], 0, No))
                    Fila.__add__(GeraNoh(No_Filhos[l], 0, No))  # isso pode dar problemas
            ListaFechada.__add__(No.um)
            ListaFechada.__add__(No.dois)
            ListaFechada.__add__(No.tres)

        if (No.__numFilhos__() == 4):  # caso 4 filhos
            if (testeSolucao(No.um)):
                conjuntoSolucao.append(copy.deepcopy(No.um))
                Break = 1
            elif (testeSolucao(No.dois)):
                conjuntoSolucao.append(copy.deepcopy(No.dois))
                Break = 1

            elif (testeSolucao(No.tres)):
                conjuntoSolucao.append(copy.deepcopy(No.tres))
                Break = 1
            elif (testeSolucao(No.quatro)):
                conjuntoSolucao.append(copy.deepcopy(No.quatro))
                Break = 1
            else:
                # gera os filhos dos quatro
                # salva os filhos na fila
                No_Filhos = Funcao_Sucessor(No)
                for m in range(0,len(No_Filhos)): #esse loop deve ter 4 itera
                    numeroFilho = m
                    numeroFilho += 1
                    No.__alteraNohIterativo__(numeroFilho, GeraNoh(No_Filhos[m], 0, No))
                    Fila.__add__(GeraNoh(No_Filhos[m], 0, No)) #isso pode dar problemas
            ListaFechada.__add__(No.um)
            ListaFechada.__add__(No.dois)
            ListaFechada.__add__(No.tres)
            ListaFechada.__add__(No.quatro)


            #se não for, gera os filhos e salva cada um na fila
            #salva também na lista
            #se continuar, então passa para o próximo filho, ou melhor, salva a variável de filhos dele
        if(Break):
            break


    print("Vai mandar a solução, conjunto \n", conjuntoSolucao)
    return Solucao(copy.deepcopy(conjuntoSolucao))