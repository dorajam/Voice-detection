# Dora Jambor
# April 2016
'''
Takes each second of the raw .wav file, transforms it to a MEL scale, 
and puts it into a data array. This is then saved for the neural network as input_to_feed.json.
Note, the original slicing up of the .wav file will take a while, 
so make sure you write this into a json so that you can experiment with the transformations.
'''

# We'll need numpy for some mathematical operations
import numpy as np
import json

# Librosa for audio
import librosa

# matplotlib for displaying the output
import matplotlib.pyplot as plt
# get_ipython().magic(u'matplotlib inline')
# And seaborn to make it look nice
import seaborn
seaborn.set(style='ticks')

# and IPython.display for audio output
import IPython.display

# # 11.10 mins of each artist
# audio_path = './music/sound_input.wav'

input1 = []
seconds_to_get = 1221

# for i in range(seconds_to_get):
#     y, sr = librosa.load(audio_path, duration=1.0, offset=i)
#     input1.append(y)


# # ------------- store both samples in one ---------------
# inp = open("inputdata.json", "w")
# json.dump(input1, inp, cls=NumpyEncoder)
# inp.close()

# ------------- load merged audio from file ---------------
f = open("inputdata.json")
inputData = json.load(f, object_hook=json_numpy_obj_hook)
f.close()

# ------------- transform sound data + label ---------------
size = len(inputData)
print size
sr = 22050
S = []
labelled = []


# Let's make and display a mel-scaled power (energy-squared) spectrogram
# Convert to log scale (dB). We'll use the peak power as reference.
for i in range(size):
    melSpec = librosa.feature.melspectrogram(input1[i], sr=sr, n_mels=128)
    log_S = librosa.logamplitude(melSpec, ref_power=np.max)
    S.append(log_S1)
    # reshape the input arrays to be col matrix
    S[i] = S[i].reshape((128*44,1))
    # label data
    if i < math.floor(seconds_to_get/2): # label 1 for female
        labelled.append((S[i], 1))
    else:                                # else 0 for male
        labelled.append((S[i], 0))

# put files into json
inp = open("input_to_feed.json", "w")
json.dump(inputData,inp, cls=NumpyEncoder)
inp.close()
print labelled_D[0][0]
