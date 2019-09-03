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
        if(len(self.__queue)==0):
            return 0
        return 1
    #adiciona
    def add(self,element):
        self.__queue.append(element)
    #elimina e retorna
    def Remove(self):
        if(self.is_empty()):
            #raise(Empty('Queue is empty'))
            return None
        else:
            return self.__queue.pop(0)
    #imprime por questões de teste
    def __print__(self):
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