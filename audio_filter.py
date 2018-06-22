from pydub import AudioSegment
# from scipy.signal import butter, lfilter
#
# import numpy as np
# import scipy as sp
# from scipy.io.wavfile import read
# from scipy.io.wavfile import write     # Imported libaries such as numpy, scipy(read, write), matplotlib.pyplot
# from scipy import signal



# In[10]:


# Replace this with the location of your downloaded file.
# def noisered():
#     (Frequency, array) = read("F:\\projects\\python\\FinalYearProject\\testingdata\\monotest.wav")  # Reading the sound file.
#
#     # In[11]:
#
#
#     len(array)  # length of our array
#
#     # In[12]:
#
#
#
#     # In[13]:
#
#
#     FourierTransformation = sp.fft(array)  # Calculating the fourier transformation of the signal
#
#     # In[14]:
#
#
#
#
#     # In[15]:
#
#
#
#
#     # In[16]:
#
#
#     GuassianNoise = np.random.rand(len(FourierTransformation))  # Adding guassian Noise to the signal.
#
#     # In[17]:
#
#
#     NewSound = GuassianNoise + array
#
#     # In[18]:
#
#
#     write("F:\\projects\\python\\FinalYearProject\\testingdata\\New-Sound-Added-With-Guassian-Noise.wav", Frequency, NewSound)  # Saving it to the file.
#
#     # In[19]:
#
#
#     b, a = signal.butter(5, 1000 / (Frequency / 2), btype='highpass')  # ButterWorth filter 4350
#
#     # In[20]:
#
#
#     filteredSignal = signal.lfilter(b, a, NewSound)
#
#
#     # In[21]:
#
#
#     c, d = signal.butter(5, 380 / (Frequency / 2), btype='lowpass')  # ButterWorth low-filter
#     newFilteredSignal = signal.lfilter(c, d, filteredSignal)  # Applying the filter to the signal
#
#
#     # In[22]:
#
#
#     write("F:\\projects\\python\\FinalYearProject\\testingdata\\ekdamnayatest.wav", Frequency, newFilteredSignal)  # Saving it to the file.
#
#
# # Replace this with the location of your downloaded file.
def mono():
    sound = AudioSegment.from_wav("F:\\projects\\python\\FinalYearProject\\testingdata\\test.wav") #imports the audio file
    sound = sound.set_channels(1) #change recorded audio to mono
    sound.export("F:\\projects\\python\\FinalYearProject\\testingdata\\monotest.wav", format="wav") #save mono audio file

# noisered()
# mono()

