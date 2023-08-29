

## this package is mainly for solving the knapsack problem using dwave quantum annelaer. 
## you have to pass the token, and thr name of the solver("Advantage-sys", "hybrid_solver" or any other solver provided by dwave.)
## then you have to pass the items and it's associated weights, as a dictionary, {'item1': 10, ... } and num_generations & population_size in integer form. 
## run the code, and wait for the solution to get printed. 



### solver = QuantumGeneticKnapsackSolver(items, max_weight, num_generations, population_size, dwave_token, dwave_solver)
### call the solver method like this 
### solution, fitness_value  = solver.solve()
### and your optimal results get printed. 


### sometimes, the solver fails to generate exact optimal result.


