# Dwave-knapsack-solver


#### This package is mainly for solving the knapsack problem using dwave quantum annealer.

install the package by using pip

```
pip install dwave-knapsack-solver

```

### You have to pass the token, and the name of the solver("Advantage-sys", "hybrid_solver" or any other solver provided by Dwave.)


### then you have to pass the items in the format of a list of dictionaries, where each dictionary needs to have such weights and values {'weight': 3, 'value': 18} 

### num_generations & population_size in integer form. Run the code, and get the solution. 

```

  from dwave_knapsack_solver.knapsack_genetic import QuantumGeneticKnapsackSolver

  items = [ {'weight': 2, 'value': 5}, {'weight': 3, 'value': 8}, ...]    # items should be passed as list of dictionaries

  max_weight = 12
  num_geneations = 100
  population_size = 50
  dwave_token = 'your_dwave_token' # pass your dwave API token here
  dwave_solver = 'Hybrid_solver' # pass the name of any solver you want to test.

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


### Any publication of results obtained using this package must include proper citations or seek prior authorization from the author.
