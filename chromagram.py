
# coding: utf-8

# In[2]:

# from __future__ import print_function

# In[1]:

# We'll need numpy for some mathematical operations
import numpy as np
import json

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



# In[30]:

audio_path = './Dora01D.wav'
audio_path2 = './Sean01D.wav'

# input1 = np.array([])
# input2 = np.array([])
input1 = []
input2 = []
seconds_to_get = 90

for i in range(seconds_to_get):
    y, sr = librosa.load(audio_path, duration=1.0, offset=i)
    input1.append(y)

for i in range(seconds_to_get):
    y2, sr = librosa.load(audio_path2, duration=1.0, offset=i)
    input2.append(y2)
    
print type(input1[0])
print len(input1[0])
print len(input1)
print input1[0].shape

print('HAS_SAMPLERATE: ', librosa.core.audio._HAS_SAMPLERATE)


# IPython.display.Audio(data=y, rate=sr)
# IPython.display.Audio(data=input1[0], rate=sr)

import json


inputData = input1 + input2
size = len(inputData)
S = []
labelled = []


# Let's make and display a mel-scaled power (energy-squared) spectrogram
# Convert to log scale (dB). We'll use the peak power as reference.
for i in range(size):
    sample = inputData[i]
    y_harmonic, y_percussive = librosa.effects.hpss(sample)
    C = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)
    # This is also an option - less clear features
    # C = librosa.feature.chroma_cqt(y=sample, sr=sr)
    S.append(C)
    S[i] = S[i].reshape((12*44,1))
    if i < seconds_to_get: # label 1 for Dora
        labelled.append((S[i], 1))
    else: # else Sean
        labelled.append((S[i], 0))

print len(S), len(S[0]), len(S[0][0])
print type(S), type(S[0]), type(S[0][0])

inputData = labelled
inp = open("inputdata.json", "w")
json.dump(inputData,inp, cls=NumpyEncoder)
inp.close()




# In[66]:
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


# # In[ ]:



