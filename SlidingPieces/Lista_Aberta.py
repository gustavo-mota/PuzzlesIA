import heapq


class Lista_Aberta:

    def __init__(self):
        self.heap = []

    def __add__(self, No):
        tupleadd = (No.custoAcesso + No.heuristica, No)
        heapq.heappush(self.heap, tupleadd)

    def __pop__(self):
        return heapq.heappop(self.heap)

    def __showSmall__(self):
        return self.heap[0]

    def __retornaRemoveMenorNo__(self):
        tuplesmall = self.__pop__()
        return tuplesmall[1]

    def __retornaLista__(self):
        return self.heap

