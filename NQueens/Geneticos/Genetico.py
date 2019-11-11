import random
import numpy as np


class Population:
    def __init__(self, size, number):
        self.population = []
        self.number = number
        self.size = size

    def elitist_selection(self):
        point = list(map(lambda x: cost_collision(x), self.population))
        foremost_one = max(point)
        point.pop(point.index(max(point)))
        foremost_two = max(point)
        return [foremost_one, foremost_two]

    def sorted_selection(self):
        costs = list(map(lambda x: invert(cost_collision(x)), self.population))
        sum_costs = sum(costs)
        sort = random.uniform(0, sum_costs)
        choice_position = -1
        while sort > 0:
            choice_position += 1
            sort -= costs[choice_position]
        return [self.population[choice_position], self.population[choice_position - 1]]

    def crossing(self, individual_one=None, individual_two=None):
        index = random.randint(0, self.size)
        if individual_one and individual_two is not None:
            son_one = Individual(self.size, individual_one.chromosome[:index] + individual_two.chromosome[index:])
            son_two = Individual(self.size, individual_two.chromosome[:index] + individual_one.chromosome[index:])
        else:
            individual_one = self.population[0]
            individual_two = self.population[1]
            son_one = Individual(self.size, individual_one.chromosome[:index] + individual_two.chromosome[index:])
            son_two = Individual(self.size, individual_two.chromosome[:index] + individual_one.chromosome[index:])
        self.population = [son_one, son_two]


class Individual:
    def __init__(self, size, chromosome):
        self.chromosome = chromosome
        self.size = size

    def print_chromosome(self):
        print(self.chromosome)

    def mutation(self):
        pieces = tuple(random.sample(range(0, self.size), 2))
        piece = self.chromosome[pieces[0]]
        self.chromosome[pieces[0]] = self.chromosome[pieces[1]]
        self.chromosome[pieces[1]] = piece


def test(population):
    test = 1
    if cost_collision(population.population[0]) == 0:
        print("Solução 1")
        solution(population.population[0].chromosome, population.population[0])
        test = 0
    elif cost_collision(population.population[1]) == 0:
        print("Solução 2")
        solution(population.population[1].chromosome, population.population[1])
        test = 0
    return test


def solution(chromosome, individual):
    solution = []
    for i in range(len(chromosome)):
        solution.append([0] * len(chromosome))
    for j in range(len(chromosome)):
        solution[chromosome[j]][j] = 1
    for k in range(len(chromosome)):
        print(solution[k])
    individual.print_chromosome()
    print(cost_collision(individual))


def invert(number):
    if number > 0:
        return 1/number
    else:
        return 1


def cost_collision(individual):
    collision = 0
    dimension = individual.size
    for i in range(dimension):
        for j in range(i + 1, dimension):
            ind_i = np.array([i, individual.chromosome[i]])
            ind_j = np.array([j, individual.chromosome[j]])
            difference = abs(ind_i - ind_j)
            if difference[0] == difference[1] or ind_i[0] == ind_j[0] or ind_i[1] == ind_j[1]:
                collision += 1
    return collision


def sort_chromosome(size):
    return random.sample(range(0, size), size)


def queens_generate(number, population):
    for i in range(population.size):
        population.population.append(Individual(population.size, sort_chromosome(population.size)))


'''populacao = Population(4, 4)
queens_generate(4, populacao)
for i in range(populacao.size):
    populacao.population[i].print_chromossome()
    print(cost_collision(populacao.population[i]))'''


def explore(number, size, iterations):
    population = Population(size, number)
    queens_generate(number, population)
    individuals = (population.sorted_selection()[0], population.sorted_selection()[1])
    population.crossing(individuals[0], individuals[1])
    reproduction = test(population)
    if reproduction:
        if random.randint(0, 2) > 1:
            population.population[0].mutation()
            population.population[1].mutation()
        for i in range(iterations):
            population.crossing()
            continuation = test(population)
            if not continuation:
                break
            if random.randint(0, 2) > 1:
                population.population[0].mutation()
                population.population[1].mutation()

        if cost_collision(population.population[0]) >= cost_collision(population.population[1]):
            print("Melhor solução 5")
            solution(population.population[0].chromosome, population.population[0])

        else:
            print("Melhor solução")
            solution(population.population[1].chromosome, population.population[1])


def main():
    number = 4
    size = 4
    iterations = 1000
    explore(number, size, iterations)


main()
