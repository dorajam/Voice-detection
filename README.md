## Sound recognition with neural networks
This is an experiment to see how well MelFrequency Cepstral Coefficients (MFCC’s) and Chroma analysis are doing in extracting features. I then use a classical neural network to classify different pitches. 

 - see the soundTransformation directory for my implementation of the MelFrequency Cepstral Coefficients (MFCC’s). For most of the transformation I used librosa
 - see all preprocessing in the music directory       

I. run ```chromogram.py``` to get the cleaned up sound input from sound_input.wav -> this contains a data array of 1 second CQT transformed clips.   
II. run network by ```test.py```


###### DONE    
- cleaning up and processing of two audiobooks with male & female voices (concatenated two files, trimmed to equal lengths, removed silence below 20 decibels)
- implementation of the sound transformation both with MFCCs, and CQT
- placed 1 second clips of the audio data into a numpy array
- network all set up -> 99% accuracy in predicting   

###### TODO
- robustness check: train on a new data array with a bigger variety of females/male voices
- create a larger test data set
- if all works, try with music!



