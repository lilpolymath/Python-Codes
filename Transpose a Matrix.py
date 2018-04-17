from numpy import exp, array, random, dot

class neural_network:
    def __init__(self):
        random.seed(1)
        # We model a single neuron, with 3 inputs and 1 output and assign random weight.
        self.weights = 2 * random.random((3, 1)) - 1
        
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = dot(inputs.T, error * output*(1-output))
            self.weights += adjustment

    def think(self, inputs):
        result = self.__sigmoid(dot(inputs, self.weights))
        return result


network = neural_network()

# The training set
inputs = array([[1, 1, 1], [1, 0, 1], [0, 1, 1]])
outputs = array([[1, 1, 0]]).T

# Training the neural network using the training set.
network.train(inputs, outputs, 10000)

# Ask the neural network the output
print(network.think(array([1, 0, 0])))
