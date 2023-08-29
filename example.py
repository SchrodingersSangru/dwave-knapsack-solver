from dwave_knapsack_solver.knapsack_genetic import QuantumGeneticKnapsackSolver


# Example usage
items = [
    {'weight': 2, 'value': 5},
    {'weight': 3, 'value': 8},
    {'weight': 4, 'value': 10},
    {'weight': 5, 'value': 13},
]
max_weight = 8
num_generations = 100
population_size = 100

dwave_token = 'DEV-3092b857364ad14474b6cca827ed602eda60252d'
dwave_solver = 'Advantage_system4.1'

solver = QuantumGeneticKnapsackSolver(items, max_weight, num_generations, population_size, dwave_token, dwave_solver)
solution, fitness_value  = solver.solve()

print("Best solution:", solution)
print("Best fitness:", fitness_value)