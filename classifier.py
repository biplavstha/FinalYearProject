import numpy as np, scipy
from sklearn.metrics import confusion_matrix
from sklearn import svm
import pickle
import os
from matplotlib import pylab
MFCC_dir="F:\\projects\\python\\FinalYearProject\\mfcc\\"
FFT_dir="F:\\projects\\python\\FinalYearProject\\fft\\"
emotions = ['neutral']


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
    for emo in emotions:
        mfccDir=MFCC_dir+emo+"\\train"
        for file in os.listdir(mfccDir):
            mfcc_values=scipy.load(mfccDir+"\\"+file)
            mfccs.append(mfcc_values)
    return mfccs

def readFeatures():
    fft_and_label=read_fft()
    return fft_and_label[0], read_mfcc(), fft_and_label[1]

def getFeatures():
    features=[]
    ffts, mfccs, labels=readFeatures()
    for n in range(len(ffts)):
        individual_feature=[]
        individual_feature = np.concatenate((np.array(ffts[n]), individual_feature), axis=0)
        for val in mfccs[n][:2992]:
            individual_feature = np.concatenate((np.array(val), individual_feature), axis=0)
        features.append(individual_feature)
    print("Feature To Use....")
    print(features)
    print(labels)
    print(len(features),len(labels))
    return [features, labels]

print("Training..................")
featureList=getFeatures()
features=featureList[0]
labels=featureList[1]
supportVM = svm.SVC(kernel='linear', C=100.0, probability=True)
npa = np.asarray(features)
npl = np.asarray(labels)
data = supportVM.fit(npa, npl)
pickle.dump(data, open('classifier.pkl', 'wb'))
print("Score (approx).......................")
print(supportVM.predict_proba(npa))
print ("success!")
