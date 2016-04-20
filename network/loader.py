# Load data from inputData.json

from numpyEncoder import *
import math

def load_data():
	f = open("audiobook_toFeed.json", "r")
	data = json.load(f, object_hook=json_numpy_obj_hook)
	f.close()
	length = len(data)
	# for two artists
	slice1 = int(math.floor(length/4))
	slice2 = int(math.floor(length*2/4))
	slice3 = int(math.floor(length*3/4))
	print slice1,slice2,slice3

	trainingData = data[0:slice1] + data[slice2:slice3]
	testData = data[slice1:slice2] + data[slice3:length]

	# # for three artists
	# slice1 = int(math.floor(length/6))
	# trainingData = data[0:slice1] + data[slice1 * 2:slice1 * 3] + data[slice1 * 4:slice1 * 5]
	# testData = data[slice1:slice1*2] + data[slice1*3:slice1*4] + data[slice1*5:length]

	return trainingData, testData
