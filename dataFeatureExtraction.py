import numpy as np
import scipy
from scipy import fft
import os
from python_speech_features import mfcc, numpy
from scipy.io import wavfile
import math
import pandas as pd

data_dir = "F:\\projects\\python\\datasets\\"
mfcc_dir = "F:\\projects\\python\\mfcc\\"
fft_dir = "F:\\projects\\python\\fft\\"


def get_window(N):
    window=[]
    for i in range(N):
        intermediate=(2*math.pi*i)/(N-1)
        val=0.54-0.46*math.cos(intermediate)
        window.append(val)
    return window

for f in os.listdir(data_dir):
    sample_rate, data = scipy.io.wavfile.read(data_dir + f,'r')
    convert_16_bit = float(2 ** 15)
    data=data/convert_16_bit
    data=np.array(data[:2048])
    win_data=data*get_window(len(data))
    fft_feature=fft(win_data)
    # base_filename, ext=os.path.splitext(file)
    # base_filename=base_filename.rsplit("\\",1)[1]
    # new_filename=base_filename+".csv"
    # save(FFT_dir+"\\"+key, fft_feature, new_filename, genre, "FFT")
    np.save(fft_dir+f+"fft.csv",fft_feature)

# for f in os.listdir(data_dir):
#     (rate, sig) = scipy.io.wavfile.read(data_dir + f, 'r')
#     convert_16_bit = float(2 ** 15)
#     sig = sig / convert_16_bit
#     musicData = np.array(sig)
#     ceps = mfcc(sig, samplerate=rate, preemph=0, nfft=1200)
#     np.save(mfcc_dir+f+"mfcc.csv",ceps)
    # df = pd.DataFrame(ceps)
    # df.to_csv(mfcc_dir + f + "-mfcc.csv")


