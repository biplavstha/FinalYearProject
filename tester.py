import pickle
import numpy as np
from sklearn.metrics import confusion_matrix
import os
import scipy
from sklearn import preprocessing
from matplotlib import pylab
import featureExtraction

MFCC_dir="F:\\projects\\python\\FinalYearProject\\mfcc\\"
FFT_dir="F:\\projects\\python\\FinalYearProject\\fft\\"
emotions = ['happy','sad','anger','fearful']
def plot_confusion_matrix(cm, genre_list, title):
    pylab.clf()
    pylab.matshow(cm, fignum=False, cmap='Blues',
                      vmin=0, vmax=20)
    ax = pylab.axes()
    ax.set_xticks(range(len(genre_list)))
    ax.set_xticklabels(genre_list)
    ax.xaxis.set_ticks_position("bottom")
    ax.set_yticks(range(len(genre_list)))
    ax.set_yticklabels(genre_list)
    pylab.title(title)
    pylab.colorbar()
    pylab.grid(False)
    pylab.xlabel('Predicted class')
    pylab.ylabel('True class')
    pylab.grid(False)
    pylab.show()

#multiple
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
    for emo in emotions:
        mfccDir=MFCC_dir+emo+"\\test"
        for file in os.listdir(mfccDir):
            mfcc_values=scipy.load(mfccDir+"\\"+file)

            mf = np.mean(mfcc_values)
            mfccs.append(mfcc_values)
    for i in range(len(mfccs)):
        length = len(mfccs[i])
        if length < 526:
            mfccs[i].resize((526, 13), refcheck=False)
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
    return [features, labels]
def all():
    print("Testing....")
    result=[]
    count=0
    featureList = getFeatures()
    features = featureList[0]
    features = preprocessing.scale(features)
    labels = featureList[1]
    print('features length')
    print(len(features))

    #accuracy testing
    print(len(labels))
    t_data = pickle.load(open('classifier//linearclassifier.pkl', 'rb'))
    for i in range(len(labels)):
        ans=t_data.predict(np.asanyarray(features[i]).reshape(1,-1))[0]
        if ans==labels[i]:
            count=count+1
        result.append(ans)

    print("result")
    print(count)
    print(result)
    print("labels")
    print(labels)
    accuracy=count/len(labels)
    cm=confusion_matrix(labels,result)
    print("confusion matrix:")
    print(cm)
    plot_confusion_matrix(cm, emotions, "Confusion Matrix")
    print(count/len(labels))
    print("success!")





# individual testing
def individual():
    # featureExtraction.extractFeatures()
    ffts=[]
    mfccs=[]
    features=[]

    fft_values=scipy.load('testdatafeatures//fft.csv.npy')
    # fft_values=scipy.load('03-01-06-01-01-01-01.wavfft.csv.npy')
    fft_values=abs(fft_values)
    ffts.append(fft_values)

    mfcc_values = scipy.load('testdatafeatures//mfcc.csv.npy')
    # mfcc_values = scipy.load('03-01-06-01-01-01-01.wavmfcc.csv.npy')
    mfccs.append(mfcc_values)
    print("lakjhsdf")

    mfccs[0].resize((526, 13), refcheck=False)

    for n in range(len(ffts)):
        individual_feature = []
        individual_feature = np.concatenate((np.array(ffts[n]), individual_feature), axis=0)
        for val in mfccs[n][:526]:
            individual_feature = np.concatenate((np.array(val), individual_feature), axis=0)
        features.append(individual_feature)

    t_data = pickle.load(open('classifier//linearclassifier.pkl','rb'))
    ans=t_data.predict(np.asanyarray(features).reshape(1,-1))[0]
    print("answer is")
    print(ans)
    return (ans)

all()
# individual()
