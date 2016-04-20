
# We'll need numpy for some mathematical operations
import numpy as np
import json
import math

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

# add each 1 sec CQT chromogram as one input for the NN (formatted as a col matrix)
for i in range(size):
    sample = inputData[i]
    if sample.shape == (22050,): # sample rate of 22050 --> 20580 for sample[235] and 0s after-> messes up
        # y_harmonic, y_percussive = librosa.effects.hpss(sample)
        # C = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)

        # This is also an option - less clear features
        C = librosa.feature.chroma_cqt(y=sample, sr=sr)

        S.append(C)
        S[i] = S[i].reshape((12*44,1))
        if i < math.floor(seconds_to_get/2): # label 1 for Beyonce
            labelled.append((S[i], 1))
        # elif i in range(int(math.floor(seconds_to_get/3)), int(math.floor(seconds_to_get/3*2))):
        #     labelled.append((S[i], 1))
        else: # else Chet Baker
            labelled.append((S[i], 0))

    else:
        print "Sample rate is messy"

print len(S), len(S[0]), len(S[0][0])
print type(S), type(S[0]), type(S[0][0])


# # ------------- store both samples in one ---------------
f = open("input_to_feed2.json", "w")
json.dump(labelled, f, cls=NumpyEncoder)
f.close()

# ------------------------------------------ test for features -------------------------------------------------
# # try to see features on a sample
# sample = input1[0]
# C = librosa.feature.chroma_cqt(y=sample, sr=sr)
# y_harmonic, y_percussive = librosa.effects.hpss(sample) # 13s
# C1 = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr) # 5s
# # In[63]:

# # Make a new figure
# plt.figure(figsize=(12,4))

# # Display the spectrogram on a mel scale
# plt.subplot(2,1,1)

# # sample rate and hop length parameters are used to render the time axis
# librosa.display.specshow(C, sr=sr, x_axis='time', y_axis='mel')

# plt.subplot(2,1,2)
# librosa.display.specshow(C1, sr=sr, x_axis='time', y_axis='mel')
# # Put a descriptive title on the plot
# plt.title('CQT')

# # draw a color bar
# plt.colorbar(format='%+02.0f dB')

# # Make the figure layout compact
# plt.tight_layout()
# # ------------------------------------------------- end -------------------------------------------------


# # In[23]:

# y_harmonic, y_percussive = librosa.effects.hpss(y)


# # In[24]:

# IPython.display.Audio(data=y_harmonic, rate=sr)


# # In[25]:

# IPython.display.Audio(data=y_percussive, rate=sr)


# # In[26]:

# # What do the spectrograms look like?
# # Let's make and display a mel-scaled power (energy-squared) spectrogram
# S_harmonic   = librosa.feature.melspectrogram(y_harmonic, sr=sr)
# S_percussive = librosa.feature.melspectrogram(y_percussive, sr=sr)

# # Convert to log scale (dB). We'll use the peak power as reference.
# log_Sh = librosa.logamplitude(S_harmonic, ref_power=np.max)
# log_Sp = librosa.logamplitude(S_percussive, ref_power=np.max)

# # Make a new figure
# plt.figure(figsize=(12,6))

# plt.subplot(2,1,1)
# # Display the spectrogram on a mel scale
# librosa.display.specshow(log_Sh, sr=sr, y_axis='mel')

# # Put a descriptive title on the plot
# plt.title('mel power spectrogram (Harmonic)')

# # draw a color bar
# plt.colorbar(format='%+02.0f dB')

# plt.subplot(2,1,2)
# librosa.display.specshow(log_Sp, sr=sr, x_axis='time', y_axis='mel')

# # Put a descriptive title on the plot
# plt.title('mel power spectrogram (Percussive)')

# # draw a color bar
# plt.colorbar(format='%+02.0f dB')

# # Make the figure layout compact
# plt.tight_layout()


