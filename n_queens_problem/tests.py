from n_queens import tests

tests(dimension=4, population_s=50, gerations=300,
      best=0.5, mutation_p=0.01, n_tests=100)
tests(dimension=8, population_s=50, gerations=300,
      best=0.5, mutation_p=0.01, n_tests=100)
tests(dimension=16, population_s=50, gerations=300,
      best=0.5, mutation_p=0.01, n_tests=100)
tests(dimension=32, population_s=50, gerations=300,
      best=0.5, mutation_p=0.01, n_tests=100)
tests(dimension=64, population_s=50, gerations=300,
      best=0.5, mutation_p=0.01, n_tests=100)
