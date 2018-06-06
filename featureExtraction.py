from pyexpat import features
import numpy as np
import scipy
from scipy import fft
import os
from python_speech_features import mfcc, numpy
from scipy.io import wavfile
import pandas as pd
MFCC_dir="F:\\projects\\python\\FinalYearProject\\mfcc_csv"


mfccs=[]
file='test.wav'
print (file)
(rate,sig) = scipy.io.wavfile.read(file)
convert_16_bit = float(2 ** 15)
sig = sig / convert_16_bit
musicData = np.array(sig)
ceps = mfcc(sig,samplerate=rate,preemph=0,nfft=1103)
df = pd.DataFrame(ceps)
df.to_csv("mfcctest1.csv")
print(ceps)
