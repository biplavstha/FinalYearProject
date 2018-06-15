import featureExtraction
import pickle
import numpy as np
from sklearn.metrics import confusion_matrix
import os
import scipy
from sklearn import preprocessing
from sklearn import svm
from matplotlib import pylab

MFCC_dir="F:\\projects\\python\\FinalYearProject\\mfcc\\"
FFT_dir="F:\\projects\\python\\FinalYearProject\\fft\\"
emotions = ['1','3','8','4','7','5','6','2']

def read_fft():
    ffts=[]
    labels=[]
    for emo in emotions:
        fftDir=FFT_dir+emo+"\\test"
        for file in os.listdir(fftDir):
            fft_values=scipy.load(fftDir+"\\"+file)
            fft_values=abs(fft_values)
            ffts.append(fft_values)
            labels.append(emo)
    return [ffts, labels]

def read_mfcc():
    mfccs=[]
    mfccs2=[]
    for emo in emotions:
        mfccDir=MFCC_dir+emo+"\\test"
        for file in os.listdir(mfccDir):
            mfcc_values=scipy.load(mfccDir+"\\"+file)

            mf = np.mean(mfcc_values)
            mfccs.append(mfcc_values)
    for i in range(len(mfccs)):
        # print(len(mfccs[i]))
        #     # print(mfccs[i].shape)
        length = len(mfccs[i])
        #     # print("...........")
        #     if len(mfccs[i]) == 526:
        #         print(mfccs[i][525])
        #     # print("old length" + str(length))
        if length < 526:
            mfccs[i].resize((526, 13), refcheck=False)
    # for i in range(len(mfccs)):
    #     print(len(mfccs[i]))
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

    for n in range(len(ffts)):
        individual_feature=[]
        individual_feature = np.concatenate((np.array(ffts[n]), individual_feature), axis=0)
        for val in mfccs[n][:526]:
            individual_feature = np.concatenate((np.array(val), individual_feature), axis=0)
        features.append(individual_feature)
    features = preprocessing.scale(features)
    print("Feature To Use....")
    #print(features)

    # print(labels)
    # print(len(features),len(labels))
    # print(len(features[0]))
    return [features, labels]

print("Testing....")
result=[]
count=0
featureExtraction.computeFeatures()
featureList = getFeatures()
features = featureList[0]
# features = preprocessing.scale(features)
labels = featureList[1]
print('features length')
print(len(features))

# individual testing
# ffts=[]
# mfccs=[]
# features=[]
#
# fft_values=scipy.load('03-01-08-01-01-01-01.wavfft.csv.npy')
# fft_values=abs(fft_values)
# ffts.append(fft_values)
#
# mfcc_values = scipy.load('03-01-08-01-01-01-01.wavmfcc.csv.npy')
# mfccs.append(mfcc_values)
# print("lakjhsdf")
#
# mfccs[0].resize((526, 13), refcheck=False)
#
# for n in range(len(ffts)):
#     individual_feature = []
#     individual_feature = np.concatenate((np.array(ffts[n]), individual_feature), axis=0)
#     for val in mfccs[n][:526]:
#         individual_feature = np.concatenate((np.array(val), individual_feature), axis=0)
#     features.append(individual_feature)
#
# t_data = pickle.load(open('classifier.pkl','rb'))
# ans=t_data.predict(np.asanyarray(features).reshape(1,-1))[0]
# print("asnwer is")
# print(ans)

print(len(labels))
t_data = pickle.load(open('classifier.pkl', 'rb'))
for i in range(len(labels)):
    ans=t_data.predict(np.asanyarray(features[i]).reshape(1,-1))[0]
    if ans==labels[i]:
        count=count+1
    result.append(ans)

print("result")
print(result)
print("labels")
print(labels)
accuracy=count/len(labels)
cm=confusion_matrix(labels,result)
print("confusion matrix:")
print(cm)
print("success!")
print(cm, accuracy)
print("accuracy")
print(accuracy)