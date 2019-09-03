from lista_fechada import Lista_Fechada
from Lista_Aberta import Lista_Aberta
from queue import Queue
from noh import *
from funcao_sucessor import Funcao_Sucessor
from Heuristica import Heuristica
from Matriz import Matriz

def Solucao(conjunto):
    No = conjunto[0]
    while(No!=None):
        conjunto.append(No.pai)
        No = copy.deepcopy(No.pai)
    return conjunto


def ImprimeSolucao(conjuntoSolucao):
    for i in conjuntoSolucao:
        i.__matrizArmazenada__().__printMatriz__()

def A_Estrela(NoRaiz):
    #lista fechada a própria cria
    ListaFechada = Lista_Fechada()
    #fila a própria cria
    Fila = Queue()
    #conjunto solução a própria cria
    ConjuntoSolucao = []
    #lista aberta a própria cria
    ListaAberta = Lista_Aberta()
    #o conjunto sução é retornado após outra função pegar

    #Fila.add(NoRaiz)
    #ListaFechada.__add__(NoRaiz) #acho deve ser aberta
    ListaAberta.__add__(NoRaiz)
    while(True):
        #deve ser trocada pela lista aberta
        No = ListaAberta.__retornaNohMenorHeuristica__()
        ListaAberta.__remove__(No.__matrizArmazenada__().__matrizVetor__())
        ListaFechada.__add__(No)
        #gera os filhos
        #Lista com filhos em matriz
        No_Filhos = Funcao_Sucessor(No, ListaFechada)
        #define quantos filhos tem
        #as heuristicas são geradas depois
        if(len(No_Filhos)==4):
            #gera os quatro filhos
            No01 = GeraNoh(No_Filhos[0], 0, No)
            No02 = GeraNoh(No_Filhos[1], 0, No)
            No03 = GeraNoh(No_Filhos[2], 0, No)
            No04 = GeraNoh(No_Filhos[3], 0, No)
            #adciona filhos ao no
            No.__alteraFilhos__(No01, No02, No03, No04)
            #adiciona na lista aberta depois
        elif(len(No_Filhos)==3):
            #gera os tres filhos
            No01 = GeraNoh(No_Filhos[0], 0, No)
            No02 = GeraNoh(No_Filhos[1], 0, No)
            No03 = GeraNoh(No_Filhos[2], 0, No)
            #adciona filhos ao no
            No.__alteraFilhos__(No01, No02, No03)
        elif(len(No_Filhos)==2):
            #gera os dois fihos
            No01 = GeraNoh(No_Filhos[0], 0, No)
            No02 = GeraNoh(No_Filhos[1], 0, No)
            #adciona filhos ao no
            No.__alteraFilhos__(No01, No02)
        elif(len(No_Filhos)==1):
            #gera o único filho
            No01 = GeraNoh(No_Filhos[0], 0, No)
            #adciona filhos ao no
            No.__alteraFilhos__(No01)
        else:
            print("deu ruim")
            break
            #não tem filhos
        #fim gera os filhos
        #Calcula heurísticas e adiciona filhos na lista aberta e testa se é a solução
        if(No.um != None):
            No.um.heuristica = Heuristica(No.um)
            if(testeSolucao(No.um)):
                ConjuntoSolucao.append(No.um) #verificar
            ListaAberta.__add__(No.um) #pode ser melhor copy.deepcopy()
        if(No.dois != None):
            No.dois.heuristica = Heuristica(No.dois)
            if (testeSolucao(No.dois)):
                ConjuntoSolucao.append(No.dois)  # verificar
            ListaAberta.__add__(No.dois)
        if(No.tres != None):
            No.tres.heuristica = Heuristica(No.tres)
            if (testeSolucao(No.tres)):
                ConjuntoSolucao.append(No.tres)  # verificar
            ListaAberta.__add__(No.tres)
        if(No.quatro != None):
            No.quatro.heuristica = Heuristica(No.quatro)
            if (testeSolucao(No.quatro)):
                ConjuntoSolucao.append(No.quatro)  # verificar
            ListaAberta.__add__(No.quatro)
    #manda o conjunto para uma função
    #a função retorna um novo conjunto
    #esse conjunto é retornado
    return Solucao(ConjuntoSolucao)
    #após o retorno a main impri