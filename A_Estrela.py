from lista_fechada import Lista_Fechada
from Lista_Aberta import Lista_Aberta
from queue import Queue
from noh import *
from funcao_sucessor import Funcao_Sucessor
from Heuristica import Heuristica
from Matriz import Matriz

def Solucao(conjunto):
    No = conjunto[0]
    while(No!=None and No.pai !=None):
        conjunto.append(No.pai)
        No = copy.deepcopy(No.pai)
    return conjunto


def ImprimeSolucao(conjuntoSolucao):
    print("A_Estrela, ImprimeSolucao, vai imprimir solução de tamanho ", len(conjuntoSolucao))
    for i in conjuntoSolucao:
        if(i!=None):
            i.__matrizArmazenada__().__printMatriz__()
            print("\n")

def A_Estrela(NoRaiz):
    #lista fechada a própria cria
    ListaFechada = Lista_Fechada()
    #fila a própria cria
    #Fila = Queue()
    #conjunto solução a própria cria
    ConjuntoSolucao = []
    #lista aberta a própria cria
    ListaAberta = Lista_Aberta()
    #o conjunto sução é retornado após outra função pegar

    #Fila.add(NoRaiz)
    #ListaFechada.__add__(NoRaiz) #acho deve ser aberta
    ListaAberta.__add__(NoRaiz)
    cont = 0

    if(testeSolucao(NoRaiz)):
        ConjuntoSolucao.append(NoRaiz)
        return Solucao(copy.deepcopy(ConjuntoSolucao))
    while(True):
        print("entrou aqui ", cont)
        #deve ser trocada pela lista aberta
        No = ListaAberta.__retornaNohMenorHeuristica__()
        print("A_Estrela, linha 40 ","\n","imprime lista aberta")
        ListaAberta.__printListaAberta__()
        print("A_Estrela, linha 42 ","\n","recebeu dados de lista aberta")
        if(No!=None):
            print("A_Estrela, linha 44 ","\n", "Nó recebido não é none")
        if(type(No)!=int):
            ListaAberta.__remove__(No.__matrizArmazenada__().__matrizVetor__())
            ListaFechada.__add__(No)
        else:
            print("A_Estrela, linha 49 ","\n", "No se trata de inteiro","\n","vai dar break")
            break
        #gera os filhos
        #Lista com filhos em matriz
        #No_Filhos = Funcao_Sucessor(No, ListaFechada)
        No_Filhos = Funcao_Sucessor(No)
        print("tamanho No_filhos ", len(No_Filhos))
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
            No.um.heuristica = Heuristica(No.um) + 1 #heuristica e custo favor ajeita +1
            print("no um não vazio pai do no um ", No.um.pai)
            #estava acontecendo loop e sem revelar onde
            #espero que a interrupção funcione ao achar solução
            if(testeSolucao(No.um)):
                print("no um SOLUCAO")
                ConjuntoSolucao.append(No.um) #verificar
                break
            ListaAberta.__add__(No.um) #pode ser melhor copy.deepcopy()
        if(No.dois != None):
            No.dois.heuristica = Heuristica(No.dois) +1
            print("no dois não vazio pai do no dois: ", No.dois.pai)
            if (testeSolucao(No.dois)):
                ConjuntoSolucao.append(No.dois)  # verificar
                break
            ListaAberta.__add__(No.dois)
        if(No.tres != None):
            No.tres.heuristica = Heuristica(No.tres) +1
            print("no tres não vazio")
            if (testeSolucao(No.tres)):
                ConjuntoSolucao.append(No.tres)  # verificar
                break
            ListaAberta.__add__(No.tres)
        if(No.quatro != None):
            No.quatro.heuristica = Heuristica(No.quatro) +1
            print("no quatro não vazio")
            if (testeSolucao(No.quatro)):
                ConjuntoSolucao.append(No.quatro)  # verificar
                break
            ListaAberta.__add__(No.quatro)
    #manda o conjunto para uma função
    #a função retorna um novo conjunto
    #esse conjunto é retornado
        cont+=1
    print(type(ConjuntoSolucao), len(ConjuntoSolucao))
    print(ConjuntoSolucao)
    return Solucao(copy.deepcopy(ConjuntoSolucao))
    print("Nao tem solucao, nao sei pq continua iterando")
    #após o retorno a main impri