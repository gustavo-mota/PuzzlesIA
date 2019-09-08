from queue import Queue
from lista_fechada import Lista_Fechada
from Lista_Aberta import Lista_Aberta
from noh import *
from funcao_sucessor import Funcao_Sucessor
from Heuristica import Heuristica
from Matriz import Matriz
from A_Estrela import *
import copy

def BuscaLargura(Noh):

    conjuntoSolucao = []
    if(testeSolucao(Noh)):
        conjuntoSolucao.append(Noh)
        return Solucao(copy.deepcopy(conjuntoSolucao)) #conjunto solução deve ser enviado como lista contendo nó solução

    Borda = Queue()
    Borda.__add__(copy.deepcopy(Noh))
    '''
    Borda.__print__() #testes
    print("fila pirnt") #testes
    print("Borda impressa \n") #testes
    iteracao = 0
    '''
    while(Borda.is_empty()==1): #1 para cheia 0 vazia
        #print("Busca em largura, iteração :", iteracao) #testes
        Break = 0
        No = Borda.Remove() #exatrai no de fila e remove
        #print("Nó extraído da fila\n", No) #testes
        #Borda.__print__() #testes
        #No_Filhos.clear()
        #Borda.__print__() #testes
        #para número movimento permitido:
        Nos_Filhos = Funcao_Sucessor(No) #função sucessor corta a repetição de pai no filho
        for i  in range(0, No.__movimentosNumero__()): #dependendo do uso some um e comece do 1
            numeroFilho = i
            numeroFilho += 1
            #desconheço se esse trecho funciona

            #gera filhos

            #falta testar __filhoEspecifico__()

            #experimenta não mandar uma lista e sim a matriz de verdade em GeraNoh
            #No.__alteraNohIterativo__(numeroFilho, GeraNoh(copy.deepcopy(Nos_Filhos[i]).__retornaMatriz__(), 0, No))
            No.__alteraNohIterativo__(numeroFilho, GeraNoh(copy.deepcopy(Nos_Filhos[i]), 0, No))

            #Borda.__add__(GeraNoh(Nos_Filhos[i].__retornaMatriz__(), 0, No))

            #fim do trecho desconhecido se funciona

            if(testeSolucao(No.__filhoEspecifico__(numeroFilho))):
                conjuntoSolucao.append(No.__filhoEspecifico__(numeroFilho))
                Break = 1
                break
            Borda.__add__(No.__filhoEspecifico__(numeroFilho))
            #gera filho
            #testa se o filho é solução
                #se for retorna
            #insere na borda
        Nos_Filhos.clear()
        if(Break):
            break
    #print("Vai mandar a solução, conjunto \n", conjuntoSolucao)
    return Solucao(copy.deepcopy(conjuntoSolucao))

'''
função BUSCA-EM-LARGURA(problema) retorna uma solução ou falha
nó ← um nó com ESTADO = problema.ESTADO-INICIAL, CUSTO-DE-CAMINHO = 0
se problema.TESTE-DE-OBJETIVO(nó.ESTADO) senão retorne SOLUÇÃO(nó),
borda ← uma fila FIFO com nó como elemento único
explorado ← conjunto vazio
repita
    se VAZIO?(borda), então retorne falha
    nó ← POP(borda) / * escolhe o nó mais raso na borda */
    adicione nó.ESTADO para explorado
    para cada ação em problema.AÇÕES(nó.ESTADO) faça
        filho ← NÓ-FILHO(problema, nó, ação),se (filho.ESTADO)não está em explorado ou borda então
        se problema.TESTE-DE-OBJETIVO(filho.ESTADO) então retorne SOLUÇÃO(filho)
        borda ← INSIRA(filho, borda)
'''