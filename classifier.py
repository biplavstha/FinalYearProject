import numpy as np, scipy
from sklearn import svm, preprocessing, datasets
import pickle
import os
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer


MFCC_dir="F:\\projects\\python\\FinalYearProject\\mfcc\\" #directory of stored mfcc values
FFT_dir="F:\\projects\\python\\FinalYearProject\\fft\\" #directory of stored fft values

emotions = ['happy','sad','anger','fearful']
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
    for i in range(len(mfccs)):
        length = len(mfccs[i])
        if length < 526:
            mfccs[i].resize((526,13),refcheck=False)
    return mfccs

def readFeatures():
    fft_and_label=read_fft()
    return fft_and_label[0], read_mfcc(), fft_and_label[1]

def getFeatures():
    features=[]
    ffts, mfccs, labels=readFeatures()
    print(len(ffts))
    print(len(mfccs))
    print("insside get after read")
    for n in range(len(ffts)):
        individual_feature=[]
        individual_feature = np.concatenate((np.array(ffts[n]), individual_feature), axis=0)
        for val in mfccs[n][:526]:
            individual_feature = np.concatenate((np.array(val), individual_feature), axis=0)
        features.append(individual_feature)
    features = preprocessing.scale(features)
    return [features, labels]

npa = np.array([])
npl = np.array([])
print("Training..................")
featureList=getFeatures()
print("ajshfd")
print(featureList)
shuffle(featureList)
features=featureList[0]
labels=featureList[1]
print()

# print(features)
supportVM = svm.SVC(kernel='linear', C=100, probability=True)
print("svmsvc vayo")
npa = np.asarray(features)
npa = np.subtract(npa,np.mean(npa))
npl = np.asarray(labels)

print("array banayo")
data = supportVM.fit(npa, npl)
print("fit vayo")
pickle.dump(data, open('classifier//linearclassifier.pkl', 'wb'))
print("Score (approx).......................")

print(supportVM.predict_proba(npa))
print ("success!")
