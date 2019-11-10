import random
import numpy
import math
import copy


size = 40

def solution(matriz):
    for i in matriz:
        print(list(i))


def sort_change(matriz):  # array
	matriz_change = matriz.copy()
    numbers = list(range(0, len(matriz)))
    column_one = random.choice(numbers)
    numbers.remove(column_one)
    column_two = random.choice(numbers)
    # alteração das colunas
    var = numpy.copy(matriz_change[:, column_one])
    matriz_change[:, column_one] = matriz_change[:, column_two]
    matriz_change[:, column_two] = var
    return matriz_change


def cost_collision(matriz, size):  # array
    atack = 0
    for i in range(size):
        line_atcolumn = list(matriz[:, i]).index(1)
        for j in range(i+1, size):
            if abs(i - j) == abs(line_atcolumn - list(matriz[:,j ]).index(1)):
                atack += 1
    return atack


def initial_generate(size):  # array
    return numpy.identity(size)


def explorer(size):
    current = initial_generate(size)
    while True:
        current_collision = cost_collision(current, size)
        new = sort_change(current)
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

explorer(size)
