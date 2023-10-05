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


def main(dimension=8, population_s=50, gerations=200, best=0.5, mutation_p=0.01, test=False):
    """
    Função principal para executar o almoritmo genético e plota o cromossomo com a possível solução para o problema
    das N-Rainhas.
    :param dimension: int  - Dimensão do tabuleiro e número de rainhas
    :param population_s: int - Tamanho da população de indivíduos
    :param gerations: int - Número de gerações
    :param best: float - Taxa de seleção em %
    :param mutation_p: float - Taxa de mutação em %
    :param test: bool - Parâmetro para a execução de testes(ignorar)
    """
    population = population_generate(dimension, population_s)
    population_selected = selection(population, best)

    resultados = [[0, population_selected[0].fitness]]
    best_cromossomo = population_selected[0].fitness

    for _ in range(1, gerations):
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

        resultados.append([_, best_cromossomo])
        population_selected = selection(population_selected, best)
    if not test:
        print(f'{population_selected[0]}')
        plot_cromossomo(population_selected[0])
        plot_resultados(resultados)
    return [resultados, population_selected[0].fitness]


def tests(dimension: int = 8, population_s: int = 50, gerations: int = 200, best=0.5, mutation_p=0.01, n_tests: int = 10):
    results_tests = []
    testes = []
    geracoes = []
    geracoes_m = 0
    bests_fitness = []
    for test in range(n_tests):
        teste = main(dimension, population_s, gerations,
                     best, mutation_p, test=True)
        best_fitness = teste[1]
        resultados = teste[0]
        i = 0
        best_generation = i
        for _ in resultados:
            if resultados[i][1] == best_fitness:
                best_generation = i
                break
            i += 1
        testes.append(test+1)
        geracoes.append(best_generation)
        geracoes_m += best_generation
        bests_fitness.append(best_fitness)
        results_tests.append([test+1, best_fitness, best_generation])
    plt.plot(geracoes, label="Número de Geração")
    plt.plot(bests_fitness, label="Melhor Fitness das Gerações")
    media = int(geracoes_m/len(geracoes))
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig(f'tests_n_{dimension}')
    print(f'Media de gerações: {media}')
    return media


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
