#!/bin/bash

for i in $(ls *[^t].wav); do
	ffmpeg -ss 30 -i $i -t 120 -acodec copy $(basename $i .wav)t.wav
	
done 




for i in $(ls *t.wav); do
	ffmpeg -i $i -ac 1 $(basename $i .wav)mono.wav
done
