import librosa
import json
from numpyEncoder import *

import loader

# take half of Dora + half of Sean -> rest should be reserved for validation
trainingData, testData = loader.load_data()
print len(trainingData), len(testData)

import network

eta = 1.5
NUM_EPOCHS = 2
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
# # the arguments are the following: training data, batch size, learning rate and number of epochs
# net.gradientDescent(trainingData, BATCH_SIZE, eta, NUM_EPOCHS, lmbda,
#                     test_data=testData)

# ------------------------------------ TEST WITH RECORDED FILES ----------------------------------------
audio_test = 'testAudio.wav'
seconds = 206
data = []
for i in xrange(seconds):
    y, sr = librosa.load(audio_test, duration=1.0, offset=i)

    C = np.abs(librosa.cqt(y=y, sr=sr, real=False))    
    C = C.reshape(INPUT_NEURONS, 1)
    if i < 85:
        L = (C, np.array([[1],[0]]))
    else:
        L = (C, np.array([[0],[1]]))
    data.append(L)

# print len(data), data[0].shape

# ------------------------------------ LOAD WEIGHTS AND BIASES ----------------------------------------
f = open("weights.json", "r")
weights = json.load(f, object_hook=json_numpy_obj_hook)
h = open("biases.json", "r")
biases = json.load(h, object_hook=json_numpy_obj_hook)

# ------------------------------------ FORWARDPROPAGATE ----------------------------------------
# print biases.shape, weights.shape
# for i in xrange(data):
res = net.bingo(data[0][0], biases, weights)
test_results = [(np.argmax(net.bingo(x,biases,weights)),np.argmax(y)) for x, y in data] 
# res = softmax(res)
print sum(int(x == y) for x, y in test_results)

