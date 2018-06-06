from pyexpat import features
import numpy as np
import scipy
from scipy import fft
import os
from python_speech_features import mfcc, numpy
from scipy.io import wavfile
import pandas as pd
from sox.core import sox, soxi

data_dir = "F:\\projects\\python\\datasets\\"
mfcc_dir = "F:\\projects\\python\\mfcc\\"
meta_dir = "F:\\projects\\python\\metadatastrip\\"

for f in os.listdir(data_dir):
    (rate, sig) = scipy.io.wavfile.read(data_dir + f, 'r')
    convert_16_bit = float(2 ** 15)
    sig = sig / convert_16_bit
    musicData = np.array(sig)
    ceps = mfcc(sig, samplerate=rate, preemph=0, nfft=1200)
    df = pd.DataFrame(ceps)
    df.to_csv(mfcc_dir + f + "-mfcc.csv")


