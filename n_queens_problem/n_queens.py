from random import randint


class Cromossomo():
    def __init__(self, dimension):
        self.genes = []
        self.dimension = dimension

    # Falta corrigir
    def get_fit(self):
        fitness = 0

        dimension = self.dimension
        for i in range(0, dimension):
            for j in range(i+1, dimension):
                if self.genes[i] == self.genes[j]:
                    fitness += 1

                if self.genes[i] - self.genes[j] == abs(i-j):
                    fitness += 1
        self.fitness = fitness
        return fitness

    def autogenerate(self):
        for _ in range(0, self.dimension):
            self.genes.append(randint(1, self.dimension))

        return True

    def __repr__(self) -> str:
        return f'cromossomo: {self.genes}\nfitness: {self.fitness}'


def iniciate(dimension, n_population):
    population = []

    for _ in range(1, n_population+1):
        cromossomo = Cromossomo(dimension)
        cromossomo.autogenerate()
        cromossomo.get_fit()
        population.append(cromossomo)

    return population


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


def teste():
    # d = int(input('Dimension: '))
    # p = int(input('Population: '))
    d = 4
    p = 1
    individuos = iniciate(d, p)
    print(individuos[0])
    plot_cromossomo(individuos[0])


teste()
