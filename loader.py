# Load data from inputData.json

from numpyEncoder import *

def load_data():
	f = open("inputData.json", "r")
	data = json.load(f, object_hook=json_numpy_obj_hook)
	f.close()
	trainingData = data[0:60] + data[90:150]
	testData = data[60:90] + data[150:180]
	return trainingData, testData
