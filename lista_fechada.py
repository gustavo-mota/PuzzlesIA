#dicionário
#o índice é o vetor da matriz
#o volum é o nó
#converte o vetor para string

#a lista é um dicionário; uma função hash
class Lista_Fechada :
    #cria lista
    def __init__(self):
        self.dict={}
    #adiciona elemento
    def __add__(self, Noh=None):
        indice = Noh.__matrVetor__()
