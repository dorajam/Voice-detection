import loader

# take half of Dora + half of Sean -> rest should be reserved for validation
trainingData, testData = loader.load_data()
print len(trainingData), len(testData)

import network

eta = 1.5
NUM_EPOCHS = 30
# for CQT
INPUT_NEURONS = 84 * 44
# for mel spectogram
# INPUT_NEURONS = 128 * 44

HIDDEN_LAYER1 = 100

HIDDEN_LAYER2 = 50
HIDDEN_LAYER3 = 30

OUTPUT_NEURONS = 2
BATCH_SIZE = 10
lmbda = 0	

net = network.Network([INPUT_NEURONS,HIDDEN_LAYER1, OUTPUT_NEURONS])
# the arguments are the following: training data, batch size, learning rate and number of epochs
net.gradientDescent(trainingData, BATCH_SIZE, eta, NUM_EPOCHS, lmbda,
                    test_data=testData)
