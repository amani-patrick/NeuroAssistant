import math
import random

class Neuron:
    def __init__(self, num_inputs):
        self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
        self.bias = random.uniform(-1, 1)
        self.output = 0.0

    def activate(self, inputs):
        total = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        self.output = self.tanh(total)
        return self.output

    @staticmethod
    def tanh(x):
        return math.tanh(x)

    def mutate(self, mutation_rate=0.1, mutation_strength=0.5):
        self.weights = [
            w + random.uniform(-mutation_strength, mutation_strength) if random.random() < mutation_rate else w
            for w in self.weights
        ]
        if random.random() < mutation_rate:
            self.bias += random.uniform(-mutation_strength, mutation_strength)

    def copy(self):
        copy_neuron = Neuron(len(self.weights))
        copy_neuron.weights = self.weights[:]
        copy_neuron.bias = self.bias
        return copy_neuron


class Layer:
    def __init__(self, num_neurons, num_inputs):
        self.neurons = [Neuron(num_inputs) for _ in range(num_neurons)]

    def forward(self, inputs):
        return [neuron.activate(inputs) for neuron in self.neurons]

    def mutate(self, mutation_rate=0.1, mutation_strength=0.5):
        for neuron in self.neurons:
            neuron.mutate(mutation_rate, mutation_strength)

    def copy(self):
        new_layer = Layer(0, 0)
        new_layer.neurons = [neuron.copy() for neuron in self.neurons]
        return new_layer


class NeuralNetwork:
    def __init__(self, layer_shape):
        self.layers = []
        for i in range(1, len(layer_shape)):
            self.layers.append(Layer(layer_shape[i], layer_shape[i - 1]))

    def forward(self, inputs):
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs

    def get_weights(self):
        weights = []
        for layer in self.layers:
            for neuron in layer.neurons:
                weights.append((neuron.weights[:], neuron.bias))
        return weights

    def set_weights(self, weights):
        index = 0
        for layer in self.layers:
            for neuron in layer.neurons:
                neuron.weights = weights[index][0]
                neuron.bias = weights[index][1]
                index += 1

    def mutate(self, mutation_rate=0.1, mutation_strength=0.5):
        for layer in self.layers:
            layer.mutate(mutation_rate, mutation_strength)

    def copy(self):
        new_net = NeuralNetwork([len(layer.neurons[0].weights) for layer in self.layers] + [len(self.layers[-1].neurons)])
        new_net.set_weights(self.get_weights())
        return new_net

    def __repr__(self):
        return f"<NeuralNetwork with {len(self.layers)} layers>"
