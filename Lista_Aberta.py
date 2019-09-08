from noh import *
from Matriz import Matriz
from Heuristica import *
import copy

class Lista_Aberta:
    def __init__(self, Noh):
        self.pai = None
        self.dir = None
        self.esq = None
        self.no = Noh
        self.custo = Heuristica(Noh) + 1 #refatorar para Funcaocusto
        self.raiz = Noh
        self.menor = None
    def __add__(self,Noh):
        if(self.menor.custo <= Heuristica(Noh) + 1):
            NoAntigo = copy.deepcopy(self.menor)
            self.menor = Noh
            self.menor.pai = NoAntigo
        else:
            NoAntigo = copy.deepcopy(self.menor)
            self.menor.dir = Noh
    def __menor__(self):
        return self.menor
    def __remove__(self):
        NoMenor = copy.deepcopy(self.menor)
        if(self.menor.__Pai__() != None):
            self.menor = self.menor.pai
        else:
            self.menor = self.menor.__Dir__()
        return NoMenor
    def __Pai__(self):
        return self.pai
    def __Dir__(self):
        return self.dir