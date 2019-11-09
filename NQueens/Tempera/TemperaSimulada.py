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
    column_one = random.randint(0, matriz.size - 1)
    column_two = random.randint(0, matriz.size - 1)
    # alteração das colunas
    var = matriz[column_one]
    matriz[column_one] = matriz[column_two]
    matriz[column_two] = var
    return matriz


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
    current = initial_generate(size)
    for i in range(50000):
        new = sort_change(current)
        current_collision = cost_collision(current, size)
        newest_collision = cost_collision(new, size)
        print(current_collision, newest_collision)
        if newest_collision == 0:
            solution(new)
            break
        elif newest_collision < current_collision:
            current = new.copy()
        else:
            probability = math.exp(current_collision - newest_collision)
            rand = random.uniform(0, 1)
            if rand <= probability:
                current = new.copy()
    print(newest_collision)
    solution(new)

explorer(size)
