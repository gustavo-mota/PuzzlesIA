from noh import Noh
from Matriz import Matriz
#dicionário
#o índice é o vetor da matriz
#o volum é o nó
#converte o vetor para string

#   a lista é um dicionário; uma função hash
class Lista_Fechada :
    #cria lista
    def __init__(self):
        self.dict={}
    #adiciona elemento
    def __add__(self, Noh=None):
        #indice é a matriz em forma numerica
        #a função retorna em int e a atribuição converte para o dict
        indice = str(Noh.__matrizVetor__())
        self.dict[indice] = Noh
    def __verifica__(self, chave): #chave deve vir já como string
        #verifica se retornou objeto no
        if(type(self.__retornaNoh__(chave))!=int):
            return 1 #no existe
        #retornou inteiro
        else:
            return 0 #no não existe
    def __printListaFechada__(self):
        for i in self.dict:
            print(i)
#   retorno de nó

    def __retornaNoh__(self, chave): #manda a chave já em forma de string
        #retorna o objeto
        try:
            return self.dict[chave]
        #retorna inteiro
        except :
            return 0


