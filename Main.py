from queue import Empty

import deque

#fila
#honestamente, queria usar a biblioteca do python, mas hoive problema e peguei esse codigo da net
class Queue:
    #cria fila
    def __init__(self):
        self.__queue=[]
    #tamanho
    def __len__(self):
        return len(self.__queue)
    #testa se vazia
    def is_empty(self):
        return len(self.__queue)==0 #if embutido; deixou-me impressionado
    #adiciona
    def add(self,element):
        self.__queue.append(element)
    #elimina apenas
    def Remove(self):
        if(self.is_empty()):
            raise(Empty('Queue is empty'))
        else:
            return self.__queue.pop(0)
    #primeiro apenas
    def first(self):
        if(self.is_empty()):
            raise(Empty('Queue is empty'))
        else:
            return self.__queue[0]
#fila

#no
class Noh :
    def __init__(self, val, pai=None, esq=None, dire=None):
        #eu não sei o que tou fazendo aqui
        #agora sim
        self.pai = pai
        self.esq = esq
        self.dire = dire
        self.val = val

    def __pai__(self):
        print("Esse e o valor do pai")
        return self.pai.val

    def __dire__(self):
        print("Esse e o valor do direito")
        print(self.dire.val)
        return self.dire.val

    def __esq__(self):
        print("Esse e o valor do esquerdo")
        print(self.esq.val)
        print(self.esq.val)
        return self.esq.val

    def __val__(self):
        print(self.val)
#no

def Main():
    print("Hello wolrd")
    dire = Noh(2)
    esq = Noh(3)
    raiz = Noh(1, None, dire, esq)
    print(raiz.__esq__()) #retorna conforme o objeto
    print(raiz.esq) #retorna o valor guardado


Main()