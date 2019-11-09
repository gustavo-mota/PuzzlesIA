import random
import numpy
import math
import copy


size = 40

def solution(matriz):
    lines = []
    for i in range(len(matriz)):
        lines.append([0] * len(matriz))
    for j in range(len(matriz)):
        lines[matriz[j]][j] = 1
    for k in range(len(matriz)):
        print(lines[k])


def sort_change(matriz):  # array
    # matriz_change = matriz.copy()
    # sorteio das colunas diferentes
    #numpy.random.shuffle(matriz)
    column_one = random.randint(0, matriz.size - 1)
    column_two = random.randint(0, matriz.size - 1)
    # alteração das colunas
    var = matriz[column_one]
    matriz[column_one] = matriz[column_two]
    matriz[column_two] = var
    '''numbers = list(range(0, len(matriz)))
    column_one = random.choice(numbers)
    numbers.remove(column_one)
    column_two = random.choice(numbers)
    # alteração das colunas
    var = matriz[column_one]
    matriz[column_one] = matriz[column_two]
    matriz[column_two] = var'''
    return matriz

    '''matriz_change = matriz.copy()
    numbers = list(range(0, len(matriz)))
    column_one = random.choice(numbers)
    numbers.remove(column_one)
    column_two = random.choice(numbers)
    var = numpy.copy(matriz_change[:, column_one])
    matriz_change[:, column_one] = matriz_change[:, column_two]
    matriz_change[:, column_two] = var
    return matriz_change'''


def cost_collision(matriz, size):  # array
    atack = 0
    copia = numpy.copy(matriz)
    for i in range(0, matriz.size):
        for j in range(i + 1, copia.size):
            if abs(i - j) == abs(matriz[i] - copia[j]):
                atack += 1
    return atack


def initial_generate(size):  # array
    return numpy.array(range(0, size))


def explorer(size):
    lista = [initial_generate(size)]
    solved = False
    for j in range(1000):
        for i in range(len(lista)):
            current = lista[i]
            current_collision = cost_collision(current, size)
            new = sort_change(current)
            newest_collision = cost_collision(new, size)
            if newest_collision == 0:
                solution(new)
                solved = True
                break
            elif newest_collision < current_collision:
                print("nao")
                lista[i] = new.copy()
            else:
                probability = math.e**(current_collision - newest_collision)
                rand = random.uniform(0, 1)
                if rand <= probability:
                    print("aqui")
                    lista.append(new)
        if solved:
            break
    print(newest_collision)
    solution(new)


explorer(size)
#FormigasSolucao(sort_change(initial_generate(4)))
#print(cost_collision(initial_generate(4), 4))
#print(sort_change(initial_generate(size)))
