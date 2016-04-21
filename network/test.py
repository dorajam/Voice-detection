import loader

# take half of Dora + half of Sean -> rest should be reserved for validation
trainingData, testData = loader.load_data()
print len(trainingData), len(testData)

import network

eta = 1.5
NUM_EPOCHS = 30
INPUT_NEURONS = 128 * 22
HIDDEN_LAYER1 = 30
HIDDEN_LAYER2 = 100
HIDDEN_LAYER3 = 100
OUTPUT_NEURONS = 2
BATCH_SIZE = 10
lmbda = 0

net = network.Network([INPUT_NEURONS,HIDDEN_LAYER1, OUTPUT_NEURONS])
# the arguments are the following: training data, batch size, learning rate and number of epochs
net.gradientDescent(trainingData, BATCH_SIZE, eta, NUM_EPOCHS, lmbda,
                    test_data=testData)
