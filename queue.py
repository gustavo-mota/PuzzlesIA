import copy


# fila
class Queue:

    def __init__(self):
        self.__queue = []

    def __len__(self):
        return len(self.__queue)

    def is_empty(self):
        if (len(self.__queue) == 0):
            return 0
        return 1

    def __add__(self, Noh):
        self.__queue.append(Noh)

    # elimina e retorna
    def Remove(self):
        if (self.is_empty() == 0):
            return None
        else:
            # pega primeiro elemento
            No = copy.deepcopy(self.__queue[0])
            # deleta
            self.__queue.remove(self.__queue[0])
            return No

    def __print__(self):
        print(self.__queue)
        for i in self.__queue:
            print(i, "\n")

    # primeiro apenas
    def first(self):
        if (self.is_empty()):
            return None
        else:
            return self.__queue[0]
# fila
