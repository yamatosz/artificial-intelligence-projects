from random import randint, choice, random
import matplotlib.pyplot as plt


class Cromossomo():
    def __init__(self, dimension):
        self.genes = []
        self.dimension = dimension

    def get_fit(self):
        fitness = 0

        for i in range(0, self.dimension - 1):
            for j in range(i+1, self.dimension):
                if self.genes[i] == self.genes[j] or abs(self.genes[i] - self.genes[j]) == abs(i-j):
                    fitness += 1

        self.fitness = fitness
        return fitness

    def set_gene(self, genes: list):
        self.genes = genes
        return True

    def autogenerate(self):
        for _ in range(0, self.dimension):
            self.genes.append(randint(1, self.dimension))

        return True

    def __repr__(self) -> str:
        return f'cromossomo: {self.genes}\nfitness: {self.fitness}'


def population_generate(dimension, n_population):
    population = []
    for _ in range(1, n_population+1):
        cromossomo = Cromossomo(dimension)
        cromossomo.autogenerate()
        cromossomo.get_fit()
        population.append(cromossomo)
    return population


def selection(population: list, best: float):
    population_sorted = sorted(population, key=lambda x: x.fitness)
    selected = population_sorted[:int(len(population_sorted)*best)]
    return selected


def mutation(cromossomo: Cromossomo, mutation_p: float = 0.001):
    for _ in range(cromossomo.dimension):
        if random() < mutation_p:
            cromossomo.genes[_] = randint(1, cromossomo.dimension)

    return cromossomo


def crossover(parent_1: Cromossomo, parent_2: Cromossomo, n_children: int = 1):
    childrens = []
    for i in range(n_children):
        crossover_point = randint(0, len(parent_1.genes) - 1)
        children_genes = parent_1.genes[crossover_point:] + \
            parent_2.genes[:crossover_point]
        children = Cromossomo(len(parent_1.genes))
        children.set_gene(children_genes)
        children.get_fit()
        childrens.append(children)
    return childrens


def main(dimesion=8, population_s=50, gerations=200, best=0.5, mutation_p=0.01):
    population = population_generate(dimesion, population_s)
    population_selected = selection(population, best)

    resultados = []
    best_cromossomo = population_selected[0].fitness

    for _ in range(gerations):
        new_population = []
        for parent_1 in population_selected:
            parent_2 = choice(population_selected)
            while (parent_1 == parent_2):
                parent_2 = choice(population_selected)

            childrens = crossover(parent_1, parent_2)
            for children in childrens:
                children = mutation(children, mutation_p)
                new_population.append(children)

        if new_population[0].fitness < best_cromossomo:
            best_cromossomo = new_population[0].fitness

        for cromossomo in new_population:
            population_selected.append(cromossomo)

        population_selected = selection(population_selected, best)

        resultados.append([_, best_cromossomo])

    print(f'{population_selected[0]}')
    plot_cromossomo(population_selected[0])
    plot_resultados(resultados)


def plot_resultados(resultados):
    gerations = []
    bests_cromossomos = []
    for geracao, melhor_fitness in resultados:
        gerations.append(geracao)
        bests_cromossomos.append(melhor_fitness)

    plt.plot(gerations, bests_cromossomos)
    plt.xlabel('Geracao')
    plt.ylabel('Melhor fitness')
    plt.grid(True)

    plt.savefig('graph_bests_fitness.png')
    plt.show()
    return True


def plot_cromossomo(cromossomo: Cromossomo):
    print("   ", end="")
    for i in range(1, cromossomo.dimension+1):
        print(" {}  ".format(i), end="")
    print("\n", end="")
    for i in range(0, cromossomo.dimension):
        print("   ", end="")
        for j in range(0, cromossomo.dimension):
            print("----", end="")
        print("\n", end="")
        print("{} |".format(i+1), end="")
        for j in range(1, cromossomo.dimension+1):
            if cromossomo.genes[i] == j:
                print(" R |", end="")
            else:
                print("   |", end="")
        print("\n", end="")
    print("   ", end="")
    for j in range(1, cromossomo.dimension+1):
        print("----", end="")
    print("\n", end="")


main()
