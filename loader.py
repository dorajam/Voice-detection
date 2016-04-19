# Load data from inputData.json

from numpyEncoder import *
import math

def load_data():
	f = open("input_to_feed.json", "r")
	data = json.load(f, object_hook=json_numpy_obj_hook)
	f.close()
	length = len(data)
	slice1 = int(math.floor(length/4))
	slice2 = int(math.floor(length*2/4))
	slice3 = int(math.floor(length*3/4))
	print slice1,slice2,slice3

	trainingData = data[0:slice1] + data[slice2:slice3]
	testData = data[slice1:slice2] + data[slice3:length]
	return trainingData, testData
