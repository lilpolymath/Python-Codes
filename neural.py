from numpy import exp, array, random, dot

class neural_network:
    def __init__(self):
        random.seed(1)
        # We model a single neuron, with 3 inputs and 1 output and assign random weight.
        self.weights = 2 * random.random((2, 1)) - 1

    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01*dot(inputs.T, error)
            self.weights += adjustment

    def think(self, inputs):
        return (dot(inputs, self.weights))



neural_network = neural_network()

# The training set
inputs = array([[2, 3], [1, 1], [5, 2], [12, 3]])
outputs = array([[10, 4, 14, 30]]).T

# Training the neural network using the training set.
neural_network.train(inputs, outputs, 10000)

# Ask the neural network the output
print(neural_network.think(array([15, 2])))