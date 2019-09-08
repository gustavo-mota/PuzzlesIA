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


# dicionário
# o índice é o vetor da matriz
# o volum é o nó
# converte o vetor para string

#   a lista é um dicionário; uma função hash
class Lista_Aberta:
    # cria lista
    def __init__(self):
        self.dictNos = {}
        # self.listaHeuristicas = []
        self.menorHeuristica = 10000
        self.chaveMenorHeuristica = ''

    # adiciona elemento
    def __add__(self, Noh):  # tinha None
        # indice é a matriz em forma numerica
        # a função retorna em int e a atribuição converte para o dict

        '''
        tudo errado
        tem que atualizar os dados do menor a cada adição
        acho que agora tualiza
        testar favor
        '''
        indice = str(Noh.__matrizArmazenada__().__matrizVetor__())
        # observe que o no já deve ser inserido aqui dentro com a heurística calculada
        # problema de não atualizar desde a raiz: raiz vem com heuristica
        # heuristica padrão é alta demais
        # potencial problema aqui: mante rvalor d enó que não eixste
        # prevenção com atualização correta ao remover nó
        if (self.menorHeuristica >= Noh.heuristica):  # precisa ser igual ou nem inicia se colocar raiz
            print("Liosta Aberta, linha 47", "\n", "Vai atualizar as heuristicas")
            # print("Lista Aberta, linha 47", "\n", "atualizada heurstica e menor No para ", Noh.heuristica, " ", Noh.__matrizArmazenada__()).__matrizVetor__()
            self.menorHeuristica = Noh.heuristica
            self.chaveMenorHeuristica = Noh.__matrizArmazenada__().__matrizVetor__()
            print("schjdflsdajklwdjkldjkldjlksdjklç", self.chaveMenorHeuristica)
        else:
            print("Lista Aberta, __add__, não atualiza heurística\n")

        self.dictNos[indice] = Noh
        print("Heurstica armazenada: ", self.menorHeuristica, "\n", "Heuristica do no ", Noh.heuristica)
        print("no adicionado pai ", Noh.pai)
        if (self.dictNos[indice] != None):
            print("existe no")

    # remove um elemento
    def __remove__(self, chave):
        del (self.dictNos[chave])
        print("Houve um no removido d elista aberta")
        # atualiza dados de chav e de menor
        # atualiza menor valor variavel
        # atualiza menor chave variavel
        # atualiza caso ainda existam elementos
        if (len(self.dictNos) != 0):
            self.menorHeuristica = self.__buscaMenorHeuristica__().heuristica
            self.chaveMenorHeuristica = self.__buscaMenorHeuristica__().__matrizArmazenada__().__matrizVetor__()
        else:
            self.menorHeuristica = 10000
            self.chaveMenorHeuristica = ''

    def __verifica__(self, chave):  # chave deve vir já como string
        # verifica se retornou objeto no
        if (type(self.__retornaNohEspecifico__(chave)) != int):
            return 1  # no existe
        # retornou inteiro
        else:
            return 0  # no não existe

    def __printListaAberta__(self):
        for i in self.dictNos:
            print(self.dictNos[i])

    # retorna um no
    def __retornaNohEspecifico__(self, chave):  # manda a chave já em forma de string
        # retorna o objeto
        try:
            print("Lista_Aberta, linha 84, vai retornar no de chave ", chave)
            return self.dictNos[chave]
        # retorna inteiro
        except:
            return 0

    '''
    def __retornaMenorNoh__(self):
        self.__retornaNohEspecifico__()'''

    # retorna o no com menor heurística com base na variavel armazenada
    def __retornaNohMenorHeuristica__(self):
        print("Lista Aberta, linha 90 ", "\n", "vai retornar um nó", "\n", "lista antes: ", self.dictNos)
        print("Lista Aberta, linha 91 ", "\n", "Nó retornado será: ",
              self.__retornaNohEspecifico__(self.chaveMenorHeuristica))
        print("Lista Aberta, linha 92", "\n", "Nos dentro de lista aberta são ", self.dictNos)
        return self.__retornaNohEspecifico__(self.chaveMenorHeuristica)

    # retorna o valor da menor heurística armazenada com base na variavel armazenada
    def __retornaValorMenorHeuristica__(self):
        return self.menorHeuristica

    # atualiza os dados da menor com base em uma entrada específica
    def __atualizaHeuristica__(self, Noh):
        self.chaveMenorHeuristica = Noh.__matrizArmazenada__().__matrizVetor__()
        self.menorHeuristica = Heuristica(Noh)

    # retorna o no de menor heuristica
    def __buscaMenorHeuristica__(self):
        heuristica = 10000
        chave = ''
        # caso dict tenha elementos:
        for i in self.dictNos:
            print("Lista Aberta, linha 107", "\n", "vai procurar a menor heuristica")
            if (heuristica >= self.dictNos[i].heuristica):
                heuristica = self.dictNos[i].heuristica
                chave = self.dictNos[i].__matrizArmazenada__().__matrizVetor__()
        if (len(self.dictNos) != 0):
            return self.dictNos[chave]
        return 0
