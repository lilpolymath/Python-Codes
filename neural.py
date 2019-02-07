from numpy import exp, array, random,dot

class neural_network:
    def __init__(self):
        random.seed(1)
        #We model a single neuron, with 3 input and 1 output and assign a rondom weight
        self.weights = 2 * random.random((2,1)) -1

    def train(self, inputs, outputs, num):
        for iteratioin in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01 * dot(inputs.T,error)
            self.weights += adjustment

    def think(self, inputs):
        return(dot(inputs, self.weights))


neural = neural_network()

inputs = array([[2,3], [1,1], [5,2], [12,3]])
outputs = array([[10, 4, 14, 30]]).T

neural.train(inputs, outputs, 10000)
print(neural.think(array([15,2])))
