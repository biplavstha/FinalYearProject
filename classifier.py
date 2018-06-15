import numpy as np, scipy
from sklearn import svm
import pickle
import os
from sklearn import preprocessing
import random
import pandas as pd

MFCC_dir="F:\\projects\\python\\FinalYearProject\\mfcc\\"
FFT_dir="F:\\projects\\python\\FinalYearProject\\fft\\"
#emotions = ['neutral', 'calm', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised']
emotions = ['1','2','3','4','5','6','7','8']

def read_fft():
    ffts=[]
    labels=[]
    for emo in emotions:
        fftDir=FFT_dir+emo+"\\train"
        for file in os.listdir(fftDir):
            fft_values=scipy.load(fftDir+"\\"+file)
            fft_values=abs(fft_values)
            ffts.append(fft_values)
            labels.append(emo)
    return [ffts, labels]

def read_mfcc():
    mfccs=[]
    mfcc2 = []
    # i = 0
    for emo in emotions:
        mfccDir=MFCC_dir+emo+"\\train"
        for file in os.listdir(mfccDir):
            mfcc_values=scipy.load(mfccDir+"\\"+file)
            mfccs.append(mfcc_values)
            # length = len(mfccs[i])
            # if length < 526:
            #     mfcc_values = np.pad(mfccs[i], (0, (526 - length)), 'constant', constant_values=(1))
            #     mfcc2.append(mfcc_values)
            # else:
            #     mfcc2.append(mfcc_values)
            # i=i+1
    # print(mfccs.shape)
    for i in range(len(mfccs)):
        # print(len(mfccs[i]))
    #     # print(mfccs[i].shape)
        length = len(mfccs[i])
    #     # print("...........")
    #     if len(mfccs[i]) == 526:
    #         print(mfccs[i][525])
    #     # print("old length" + str(length))
        if length < 526:
            mfccs[i].resize((526,13),refcheck=False)
        # else:
        #     mfcc2.append(mfccs[i])
    #     # print("new length")
    #     # print(len(mfcc2[i]))
    #     # print("and")
    #     print(mfccs[i].shape)
    #     print(mfccs[i])
    # temp = 0
    # for i in range(len(mfccs)):
    #     if temp < len(mfccs[i]):
    #         temp = len(mfccs[i])
    # print("min val")
    # print(temp)
    # print("thulo")
    return mfccs

def readFeatures():
    fft_and_label=read_fft()
    return fft_and_label[0], read_mfcc(), fft_and_label[1]

def getFeatures():
    features=[]
    ffts, mfccs, labels=readFeatures()
    print(len(ffts))
    print(len(mfccs))
    # print('***')
    print("insside get after read")
    for n in range(len(ffts)):
        individual_feature=[]

        # print(n)
        individual_feature = np.concatenate((np.array(ffts[n]), individual_feature), axis=0)
        # print('######')
        for val in mfccs[n][:526]:
            # print(val)
            individual_feature = np.concatenate((np.array(val), individual_feature), axis=0)
        features.append(individual_feature)
    features = preprocessing.scale(features)
    # print("Feature To Use....")
    #print(features)

    # print(labels)
    # print(len(features),len(labels))
    # print(len(features[0]))
    return [features, labels]

npa = np.array([])
npl = np.array([])
print("Training..................")
featureList=getFeatures()
print("ajshfd")
print(featureList)
features=featureList[0]
labels=featureList[1]


# print(features)
supportVM = svm.SVC(kernel='linear', C=100, probability=True)
print("svmsvc vayo")
npa = np.asarray(features)
npl = np.asarray(labels)

# npap = preprocessing.scale(npa)
print("array banayo")
# for i in range(len(npa)):
#     print(len(npa[i]))
# print(npa)
# npa = sklearn.preprocessing.scale(npa)
data = supportVM.fit(npa, npl)
print("fit vayo")
pickle.dump(data, open('classifier.pkl', 'wb'))
print("Score (approx).......................")
print(supportVM.predict_proba(npa))
print ("success!")
