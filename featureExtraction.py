import math
import numpy as np
import scipy
from python_speech_features import mfcc, numpy
from scipy.io import wavfile
import pandas as pd
import audio_filter

feature_dir = "F:\\projects\\python\\FinalYearProject\\testdatafeatures\\" #directory to save the extracted features
file = "F:\\projects\\python\\FinalYearProject\\testingdata\\monotest.wav" #input audio file from the user

def get_window(N):
    window=[]
    for i in range(N):
        intermediate=(2*math.pi*i)/(N-1)
        val=0.54-0.46*math.cos(intermediate)
        window.append(val)
    return window

def extractFeatures():
    audio_filter.mono()
    # audio_filter.noisered()
    #fft extraction
    print("here")
    sample_rate, data = scipy.io.wavfile.read(file,'r')
    convert_16_bit = float(2 ** 15)
    data=data/convert_16_bit
    data=np.array(data[:2048])
    print(data.shape)
    win_data=data*get_window(len(data))
    fft_feature= scipy.fft(win_data)
    # df = pd.DataFrame(fft_feature)
    # df.to_csv(fft_dir + f + "-fft.csv")
    np.save(feature_dir+"fft.csv",fft_feature)


    #mfcc extraction
    (rate, sig) = scipy.io.wavfile.read(file, 'r')
    convert_16_bit = float(2 ** 15)
    sig = sig / convert_16_bit
    sig = np.array(sig)
    ceps = mfcc(sig, samplerate=rate, preemph=0, nfft=1200)
    np.save(feature_dir+"mfcc.csv",ceps)
    # df = pd.DataFrame(ceps)
    # df.to_csv(mfcc_dir + f + "-mfcc.csv")

# extractFeatures()