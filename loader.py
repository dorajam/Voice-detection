# Load data from inputData.json

from numpyEncoder import *

def load_data():
	f = open("inputData.json", "r")
	data = json.load(f, object_hook=json_numpy_obj_hook)
	f.close()
	trainingData = data[0:30] + data[60:90]
	testData = data[30:60] + data[90:120]
	return trainingData, testData
