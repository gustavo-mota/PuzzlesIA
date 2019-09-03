from noh import *
from Matriz import Matriz
from Heuristica import *

'''
    vai armazenar dicionario
    contem os nomes
    as chaves são os custos até o caractere separador
    o restante é a matriz do no armazenado no valor
    
    vai ter de percorrer o dicionario
    
    ou pode ter o dicionario contendo chaves de matriz
    e o valor é a heuristica
    a menor é a que a chave é aplicada no outro dict
    e retorna o menor no
'''
from noh import Noh
from Matriz import Matriz
#dicionário
#o índice é o vetor da matriz
#o volum é o nó
#converte o vetor para string

#   a lista é um dicionário; uma função hash
class Lista_Aberta :
    #cria lista
    def __init__(self):
        self.dictNos = {}
        #self.listaHeuristicas = []
        self.menorHeuristica = 0
        self.chaveMenorHeuristica = ''
    #adiciona elemento
    def __add__(self, Noh): #tinha None
        #indice é a matriz em forma numerica
        #a função retorna em int e a atribuição converte para o dict

        '''
        tudo errado
        tem que atualizar os dados do menor a cada adição
        acho que agora tualiza
        testar favor
        '''
        indice = str(Noh.__matrizVetor__())
        #observe que o no já deve ser inserido aqui dentro com a heurística calculada
        if(self.menorHeuristica > Noh.heuristica):
            self.menorHeuristica = Noh.heuristica
            self.chaveMenorHeuristica = Noh.__matrizArmazenada__().__matrizVetor__()
        self.dictNos[indice] = Noh
    #remove um elemento
    def __remove__(self, chave):
        del(dict[chave])
        #atualiza dados de chav e de menor
        #atualiza menor valor variavel
        #atualiza menor chave variavel
        self.menorHeuristica = self.__buscaMenorHeuristica__().heuristica
        self.chaveMenorHeuristica = self.__buscaMenorHeuristica__().__matrizArmazenada__().__matrizVetor__()
    def __verifica__(self, chave): #chave deve vir já como string
        #verifica se retornou objeto no
        if(type(self.__retornaNohEspecifico__(chave))!=int):
            return 1 #no existe
        #retornou inteiro
        else:
            return 0 #no não existe
    def __printListaAberta__(self):
        for i in self.dictNos:
            print(self.dictNos[i])
    #retorna um no
    def __retornaNohEspecifico__(self, chave): #manda a chave já em forma de string
        #retorna o objeto
        try:
            return self.dictNos[chave]
        #retorna inteiro
        except :
            return 0
    '''
    def __retornaMenorNoh__(self):
        self.__retornaNohEspecifico__()'''
    #retorna o no com menor heurística com base na variavel armazenada
    def __retornaNohMenorHeuristica__(self):
        return self.__retornaNohEspecifico__(self.chaveMenorHeuristica)
    #retorna o valor da menor heurística armazenada com base na variavel armazenada
    def __retornaValorMenorHeuristica__(self):
        return self.menorHeuristica
    #atualiza os dados da menor com base em uma entrada específica
    def __atualizaHeuristica__(self, Noh):
        self.chaveMenorHeuristica = Noh.__matrizArmazenada__().__matrizVetor__()
        self.menorHeuristica = Heuristica(Noh)
    #retorna o no de menor heuristica
    def __buscaMenorHeuristica__(self):
        heuristica = 0
        chave = ''
        for i in self.dictNos:
            if(dict[i].heuristica > heuristica):
                heuristica = dict[i].heuristica
                chave = dict[i].__matrizArmazenada__().__matrizVetor__()
        return dict[chave]
