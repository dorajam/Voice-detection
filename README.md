## Sound recognition with neural networks
This was an experiment to see how well Mel Frequency Cepstral Coefficients (MFCC’s) and Chroma analysis are doing in extracting features from audio signals. To do this, I wanted to compare different artists' pitches and detect whether some song belongs to Chet Baker or Beyonce. This turned out horribly difficult to accomplish, so I moved onto simpler data and used raw audio books to detect if some voice is of a women or man.
Next, I transformed the preprocessed audio snippets, and fed them all into a neural network to classify different pitches.
   
- see the soundTransformation directory for my implementation of the Mel Frequency Cepstral Coefficients (MFCC’s). For most of the transformation I used the Python Librosa library   
- see all preprocessing in the music directory       
- run ```chromogram.py``` to get the cleaned up sound input from sound_input.wav -> this contains a data array of 1 second CQT transformed clips.    
- run network by ```test.py```


#### DONE    
- [x] cleaning up and processing of two audiobooks with male & female voices (concatenated two files, trimmed to equal lengths, removed silence below 20 decibels)
- [x] implementation of the sound transformation both with MFCCs, and CQT
- [x] placed 1 second clips of the audio data into a numpy array
- [x] network all set up -> 99% accuracy when testing on people from the training sample
- [x] 84% accuracy when testing on people different from the training sample

#### Ideas for the future
 For robustness: train on a new data array with a bigger variety of females/male voices -> problematic as there is no data
 In terms of trying different models, for more complex tasks, a recurrcent neural network would be more appropriate, so an idea could be to try that with on a larger dataset -> again, tough to get a larger sample.



