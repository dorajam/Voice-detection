## Sound recognition with neural networks
####  - still in progress -
This is an experiment to see how well MelFrequency Cepstral Coefficients (MFCC’s) and Chroma analysis are doing in differentiating between pitches. I use a classical neural network to detect features.

 - see the soundTransformation directory for my implementation of the MelFrequency Cepstral Coefficients (MFCC’s). For most of the transformation I used librosa
 - see all preprocessing in the music directory    

I. run ```chromogram.py``` to get the cleaned up sound input from sound_input.wav -> this contains a data array of 1 second CQT transformed clips.   
II. run network by ```test.py```


