import loader

# take half of Dora + half of Sean -> rest should be reserved for validation
trainingData, testData = loader.load_data()
print len(trainingData), len(testData)

import network

eta = 1.5
NUM_EPOCHS = 100
INPUT_NEURONS = 12 * 44
HIDDEN_NEURONS = 30
OUTPUT_NEURONS = 2
BATCH_SIZE = 10
lmbda = 0.1

net = network.Network([INPUT_NEURONS,HIDDEN_NEURONS,OUTPUT_NEURONS])
# the arguments are the following: training data, batch size, learning rate and number of epochs
net.gradientDescent(trainingData, BATCH_SIZE, eta, NUM_EPOCHS, lmbda,
                    test_data=testData)
