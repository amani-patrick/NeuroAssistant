import random,copy
from core.brain import NeuralNetwork

class Evolution:
    def __init__(self,population_size, mutation_rate=0.1,mutation_range=0.1):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population =[]
        self.fitness_scores =[]

    def Initialize_population(self, input_size, hidden_size, output_size):
        self.population=[
            NeuralNetwork(input_size,hidden_size,output_size)
            for _ in range(self.population_size)
        ]
        self.fitness_scores = [0.0  for _ in range(self.population_size)]
    def evaluate_population(self, fitness_function):
        for i,nn, in enumerate(self.population):
            self.fitness_scores[i] = fitness_function(nn)
    def select_parents(self):
        sorted_indices =sorted(range(len(self.fitness_scores)), key=lambda i: self.fitness_scores[i], reverse=True)
        top_half=sorted_indices[:len(sorted_indices)//2]
        return [self.population[i] for i in top_half]
    def crossover(self, parent1, parent2):
        child=copy.deepcopy(parent1)
        for l in range(len(parent1.layers)):
            for n in range(len(parent1.layers[l].neurons)):
                for w in range(len(parent1.layers[l].neurons[n].weights)):
                    if random.random() < 0.5:
                        child.layers[l].neurons[n].weights[w] = parent2.layers[l].neurons[n].weights[w]
                if random.random() < 0.5:
                    child.layers[l].neurons[n].bias = parent2.layers[l].neurons[n].bias
        return child
    def mutate(self,nn):
        for layer in nn.layers:
            for neuron in layer.neurons:
                for i in range(len(neuron.weights)):
                    if random.random() < self.mutation_rate:
                        neuron.weights[i] += random.uniform(-self.mtuation_range, self.mutation_range)
                if random.random() < self.mutation_rate:
                    neuron.bias += random.uniform(-self.mutation_range, self.mutation_range)
    def evolve(self):
        parents = self.select_parents()
        next_generation = parents[:2]  # keep top 2 elite
        while len(next_generation) < self.population_size:
            p1, p2 = random.sample(parents, 2)
            child = self.crossover(p1, p2)
            self.mutate(child)
            next_generation.append(child)
        self.population = next_generation
        self.fitness_scores = [0.0 for _ in range(self.population_size)]

    def get_best(self):
        best_index = max(range(len(self.fitness_scores)), key=lambda i: self.fitness_scores[i])
        return self.population[best_index], self.fitness_scores[best_index]
        