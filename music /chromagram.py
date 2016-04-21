# Dora Jambor
# April 2016
'''
Takes each second of the raw .wav file, transforms it with Chromagram CQT 
and puts it into a data array. This is then saved for the neural network as input_to_feed.json.
Note, the original slicing up of the .wav file will take a while, 
so make sure you write this into a json so that you can experiment with the transformations.
'''

# We'll need numpy for some mathematical operations
import numpy as np
import json
import math
import os
import sys

# Librosa for audio
import librosa

# matplotlib for displaying the output
import matplotlib.pyplot as plt
# And seaborn to make it look nice
import seaborn
seaborn.set(style='ticks')

# and IPython.display for audio output
import IPython.display
from numpyEncoder import *

# --------- use the following commands for the cleanup -----------
''' make sure that .wav files are of same channels'''
# concanate .wav files, get rid of silences under -20 decibels and trim -> 11.10mins for each sample on one file
# ffmpeg -f concat -i <( for f in *.wav; do echo "file '$(pwd)/$f'"; done ) output.wav
# ffmpeg -i output.wav -t 8280 -acodec copy output_trimmed.wav
# ffmpeg -i output_trimmed.wav -af silenceremove=0:0:0:-1:1:-20dB sound_input.wav
# ----------------------------------------------------------------

# # 11.10 mins of each artist
# audio_path = 'sound_input.wav'

input1 = []
seconds_to_get = 1221

# for i in range(seconds_to_get):
#     y, sr = librosa.load(audio_path, duration=1.0, offset=i)
#     input1.append(y)


# # ------------- store both samples in one ---------------
# inp = open("audiobook.json", "w")
# json.dump(input1, inp, cls=NumpyEncoder)
# inp.close()

# ------------- load merged audio from file ---------------
f = open("audiobook.json")
inputData = json.load(f, object_hook=json_numpy_obj_hook)
f.close()

# ------------- transform sound data + label ---------------
size = len(inputData)
print size
sr = 22050
S = []
labelled = []

# add each 1 sec CQT chromogram as one input for the NN (formatted as a col matrix)
for i in range(size):
    sample = inputData[i]
    if sample.shape == (22050,): # sample rate of 22050 --> 20580 for sample[235] and 0s after-> messes up
        
        # C = np.abs(librosa.cqt(y=sample, sr=sr, real=False))
        C = librosa.feature.melspectrogram(y=sample, sr=sr, S=None, n_fft=512)

        # You can try getting the harmonic and do CQT on that, or on the whole sample! see below!
        # y_harmonic, y_percussive = librosa.effects.hpss(sample)
        # This is also an option - less clear features
        # C = librosa.feature.chroma_cqt(y=sample, sr=sr)

        S.append(C)
        # print S[i].shape
        S[i] = S[i].reshape((128*44,1))
        # S[i] = S[i].reshape((84*44,1))
        if i < math.floor(seconds_to_get/2): # label 0 for male
            labelled.append((S[i], np.array([[1],[0]])))
        # elif i in range(int(math.floor(seconds_to_get/3)), int(math.floor(seconds_to_get/3*2))):
        #     labelled.append((S[i], 1))
        else: # else female
            labelled.append((S[i], np.array([[0],[1]])))

    else:
        print "Sample rate is messy"

print len(S), len(S[0]), len(S[0][0])
print type(S), type(S[0]), type(S[0][0])


# ------------- store both samples in one ---------------
f = open("audiobook_toFeed.json", "w")
json.dump(labelled, f, cls=NumpyEncoder)
f.close()
