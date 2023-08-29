from dwave.system import DWaveSampler, EmbeddingComposite
import random

class QuantumGeneticKnapsackSolver:
    def __init__(self, items, max_weight, num_generations, population_size, dwave_token, dwave_solver):
        self.items = items
        self.max_weight = max_weight
        self.num_generations = num_generations
        self.population_size = population_size
        # self.sampler = EmbeddingComposite(DWaveSampler())
        self.sampler = EmbeddingComposite(DWaveSampler(solver= dwave_solver , token = dwave_token))


    def fitness(self, solution):
        total_value = sum(solution[i] * item['value'] for i, item in enumerate(self.items))
        total_weight = sum(solution[i] * item['weight'] for i, item in enumerate(self.items))
        if total_weight > self.max_weight:
            return 0
        return total_value

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            solution = [random.choice([0, 1]) for _ in range(len(self.items))]
            population.append(solution)
        return population

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def create_qubo(self, population):
        qubo = {}
        for i in range(len(self.items)):
            qubo[(i, i)] = -1  # Penalize selecting the same item multiple times
            for j in range(i + 1, len(self.items)):
                qubo[(i, j)] = 2  # Reward selecting different items
        for solution in population:
            for i, gene in enumerate(solution):
                if gene == 1:
                    qubo[(i, i)] += self.items[i]['value']  # Increase reward for selecting items
        return qubo

    def solve(self):
        population = self.initialize_population()
        for _ in range(self.num_generations):
            qubo = self.create_qubo(population)
            sampleset = self.sampler.sample_qubo(qubo, num_reads=self.population_size)
            next_generation = []
            for sample in sampleset:
                solution = [sample[key] for key in sorted(sample)]
                next_generation.append(solution)
            population = sorted(next_generation, key=lambda x: self.fitness(x), reverse=True)[:self.population_size]
        best_solution = max(population, key=lambda x: self.fitness(x))
        
        return best_solution, self.fitness(best_solution)
    
        # print("Best solution:", best_solution)
        # print("Best fitness:", self.fitness(best_solution))