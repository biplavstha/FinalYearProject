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

(rate,sig) = scipy.io.wavfile.read(file)
convert_16_bit = float(2 ** 15)
sig = sig / convert_16_bit
musicData = np.array(sig)
ceps = mfcc(sig,samplerate=rate,preemph=0,nfft=1103)
df = pd.DataFrame(ceps)
df.to_csv("mfcctest1.csv")
print(ceps)
# new_filename = "mfcctest.csv"
# save(MFCC_dir,ceps, new_filename)


# def save(dir, fft_feature, file, genre):
#     dest=dir+"\\"+genre+"\\"+file
#     np.save(dest, fft_feature)
#     print("%s file %s of genre %s saved." % ( file, genre))
#
# def computeMFCC(file, genre):
#     sample_rate, musicData = scipy.io.wavfile.read(file)
#     convert_16_bit = float(2 ** 15)
#     musicData = musicData / convert_16_bit
#     musicData = np.array(musicData)
#     ceps = mfcc(musicData, samplerate=sample_rate,preemph=0)
#     # mfcc_feature=np.mean(ceps, axis=0)
#     base_filename, ext = os.path.splitext(file)
#     base_filename=base_filename.rsplit("\\",1)[1]
#     new_filename = base_filename + ".csv"
#     # save(MFCC_dir+"\\"+key,mfcc_feature, new_filename, genre, "MFCC")
#     save(MFCC_dir+"\\"+ceps, new_filename, genre, "MFCC")


# def read_mfcc(key):
#     mfccs=[]
#     for genre in MainServices.CHOSEN_GENRES:
#         mfccDir=MFCC_dir+"\\"+key+"\\"+genre
#         for file in os.listdir(mfccDir):
#             mfcc_values=scipy.load(mfccDir+"\\"+file)
#             #mfcc_values=np.pad(mfcc_values, (0,987), 'constant')
#             mfccs.append(mfcc_values)
#     return mfccs
#
# def computeFeatures(key):
#     for genre in MainServices.CHOSEN_GENRES:
#         MainServices.clean_dir(FFT_dir+"\\"+key+"\\"+genre)
#         MainServices.clean_dir(MFCC_dir+"\\"+key+"\\"+genre)
#         dir=MainServices.GENRE_WAV+"\\"+key+"\\"+genre
#         for f in os.listdir(dir):
#             computeFFT(dir+"\\"+f,genre, key)
#             computeMFCC(dir+"\\"+f,genre, key)
