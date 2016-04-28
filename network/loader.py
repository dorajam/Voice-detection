# Load data for training & testing

from numpyEncoder import *
import math
import librosa
import json

def load_data():
	f = open("audiobook_toFeed.json", "r")
	data = json.load(f, object_hook=json_numpy_obj_hook)
	f.close()
	length = len(data)

	# for two artists
	slice1 = int(math.floor(length/4))
	slice2 = int(math.floor(length*2/4))
	slice3 = int(math.floor(length*3/4))

	# this is for the two sample version
	# trainingData = data[0:slice1] + data[slice2:slice3]
	# testData = data[slice1:slice2] + data[slice3:length]

	# this is for the longer audio file
	# trainingData = data[0:(length/18)*6] + data[length/2:length/18*15] # 2/3 of data is for testing -> female + male
	# testData = data[length/18*6:length/2] + data[length/18*15:]  # 1/3 is reserved for testing

	# if using the function below, take full training set!
	trainingData = data
	return trainingData

	# else
	# return trainingData, testData


'''only use this to validate results with the same (training) people, 
but different samples! -> 83 percent accuracy'''

def alternative_testData():
	audio_path = 'second_half_forTest.wav'
	seconds_to_get = 2152 # length of the file in seconds
	inp = []

	# for i in range(seconds_to_get):
	# 	y, sr = librosa.load(audio_path, duration=1.0, offset=i)
	# 	inp.append(y)

	# d = open("second_audioHalf.json", "w")
	# json.dump(inp, d, cls=NumpyEncoder)
	# d.close()

	d = open("second_audioHalf.json", "r")
	data = json.load(d, object_hook=json_numpy_obj_hook)
	d.close()

	S = []
	labelled = []

	for i in range(seconds_to_get):
	    sample = data[i]
	    if sample.shape == (22050,): # sample rate of 22050 --> 20580 for sample[235] and 0s after-> messes up

	        # C = np.abs(librosa.cqt(y=sample, sr=sample.shape[0], real=False))
	        C = librosa.feature.melspectrogram(y=sample, sr=sample.shape[0], S=None, n_fft=512)

	        S.append(C)

	        # S[i] = S[i].reshape((128*44,1)) # for the melspegcogram
	        S[i] = S[i].reshape((128*44,1)) # for CQT

	        if i < math.floor(seconds_to_get/2): # female
	            labelled.append((S[i], np.array([[1],[0]])))
	        else: 								 # male
	            labelled.append((S[i], np.array([[0],[1]])))

	    else:
	        print "Sample rate is messy"

	return labelled



