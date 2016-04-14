import loader

data = loader.load()
# take half of Dora + half of Sean -> rest should be reserver for validation
trainingData = data[0:30] + data[60:90]
testData = data[30:60] + data[90:120]

import network

eta = 1.5
NUM_EPOCHS = 30
INPUT_NEURONS = 1144
HIDDEN_NEURONS = 2
OUTPUT_NEURONS = 2
BATCH_SIZE = 10
lmbda = 0.1

net = network.Network([INPUT_NEURONS,HIDDEN_NEURONS,OUTPUT_NEURONS])
# the arguments are the following: training data, batch size, learning rate and number of epochs
net.gradientDescent(trainingData, BATCH_SIZE, eta, NUM_EPOCHS, lmbda,
                    testData=testData)


