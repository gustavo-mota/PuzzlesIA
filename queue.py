from noh import *
import copy
#fila
#honestamente, queria usar a biblioteca do python, mas hoive problema e peguei esse codigo da net
class Queue:
    #cria fila
    def __init__(self):
        self.__queue = []
    #tamanho
    def __len__(self):
        return len(self.__queue)
    #testa se vazia
    def is_empty(self):
        if(len(self.__queue)==0):
            return 0
        return 1
    #adiciona
    def __add__(self,Noh):
        print("Queue, adição de nó \n", Noh)
        self.__queue.append(Noh)
    #elimina e retorna
    def Remove(self):
        print("Que, Remove chamado \n", "removerá \n", self.__queue[0])
        if(self.is_empty()==0):
            #raise(Empty('Queue is empty'))
            return None
        else:
            #pega primeiro elemento
            No = copy.deepcopy(self.__queue[0])
            #deleta
            self.__queue.remove(self.__queue[0])
            return No # problema self.__queue.pop(0)
    #imprime por questões de teste
    def __print__(self):
        print(self.__queue)
        for i in self.__queue:
            print(i,"\n")
    #primeiro apenas
    def first(self):
        if(self.is_empty()):
            #raise(Empty('Queue is empty'))
            return None
        else:
            return self.__queue[0]
#fila