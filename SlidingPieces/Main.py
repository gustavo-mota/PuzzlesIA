from BuscaLargura import *


def Main():
    Decisao = int(input("Deseja A* ou Busca em Largura? 1 ou 2, respectivamente: "))
    if Decisao == 1:
        print("A* selecionado")
        # entrada = [[4,1,3],[7,2,5],[0,8,6]] #fácil
        # entrada  = [ [2,8,3],[5,7,1],[6,0,4]] #médio
        # entrada = [[0,5,1],[3,8,2],[6,4,7]] #21 passos
        # entrada = [[7,3,0],[2,1,6],[8,5,4]] #22
        entrada = [[3, 0, 2], [7, 8, 6], [1, 4, 5]]  # 20

        linha1 = entrada[0]
        linha2 = entrada[1]
        linha3 = entrada[2]
        matriz = Matriz()
        matriz.__matrizAtribuiLinhas__(linha1, linha2, linha3)
        No = Noh(matriz, 0)
        No.heuristica = Heuristica(No)
        print("Main, a heuristica do no raiz é ", No.heuristica)
        ImprimeSolucao(A_Estrela(No))
    elif Decisao == 2:
        print("Busca em Largura selecionado")

        entrada = [[4, 1, 3], [7, 2, 5], [0, 8, 6]]  # sete passos
        # entrada = [ [2,8,3],[5,7,1],[6,0,4]]
        # entrada = [[0,5,1],[3,8,2],[6,4,7]]
        # entrada = [[3,0,2],[7,8,6],[1,4,5]] #20

        linha1 = entrada[0]
        linha2 = entrada[1]
        linha3 = entrada[2]
        matriz = Matriz()
        matriz.__matrizAtribuiLinhas__(linha1, linha2, linha3)
        No = Noh(matriz, 0)
        ImprimeSolucao(BuscaLargura(No))
    else:
        print("digite um valido")


Main()
