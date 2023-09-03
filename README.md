# Dwave-knapsack-solver




#### This package is mainly for solving the knapsack problem using dwave quantum annealer.

install the package by using pip

``` pip install dwave-knapsack-solver ```

### You have to pass the token, and the name of the solver("Advantage-sys", "hybrid_solver" or any other solver provided by Dwave.)


### then you have to pass the items and it's associated weights, as a dictionary, {'item1': 10, ... } and num_generations & population_size in integer form. run the code, and wait for the solution to get printed.

```

  from dwave_knapsack_solver.knapsack_genetic import QuantumGeneticKnapsackSolver

  items = {'item1': 10, 'item2': 8, ...}
  max_weight = 12
  num_geneations = 100
  population_size = 50
  dwave_token = 'your_dwave_token' # pass your dwave API token here
  dwave_solver = 'Hybrid_solver'

  solver = QuantumGeneticKnapsackSolver(items, max_weight, num_generations, population_size, dwave_token, dwave_solver)

  # call the solver method like this ->
  best_solution, fitness_value = solver.solve()
  print(best_solution)
  print(fitness_value)

```

### and your optimal results get printed.


### Sometimes, the solver fails to generate the exact optimal result.


### Features

- full customization
- Give as long a list of items as you want
- use any dwave solver and perform results with it.
- quantum genetic algorithm supported
