import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy import signal
import os
from pydub import AudioSegment

# for f in os.listdir("F:\\projects\\python\\FinalYearProject\\testingdata\\"):
#     print(f)

sound = AudioSegment.from_wav("F:\\projects\\python\\FinalYearProject\\testingdata\\test.wav")
sound = sound.set_channels(1)
sound.export("F:\\projects\\python\\FinalYearProject\\testingdata\\monotest.wav", format="wav")

# # Replace this with the location of your downloaded file.
# (Frequency, array) = read('testingdata\\test.wav') # Reading the sound file.
#
# len(array) # length of our array
#
# FourierTransformation = sp.fft(array) # Calculating the fourier transformation of the signal
#
# scale = sp.linspace(0, Frequency, len(array))
#
# GuassianNoise = np.random.rand(len(FourierTransformation)) # Adding guassian Noise to the signal.
#
# GuassianNoise = GuassianNoise[:, np.newaxis] #add dimension to gaussian
#
# NewSound = GuassianNoise + array
#
# write("testingdata\\New-Sound-Added-With-Guassian-Noise.wav", Frequency, NewSound) # Saving it to the file.
#
# b, a = signal.butter(5, 1000/(Frequency/2), btype='highpass') # ButterWorth filter 4350
#
#
# # In[20]:
#
#
# filteredSignal = signal.lfilter(b,a,NewSound)
#
#
#
# # In[21]:
#
#
# c,d = signal.butter(5, 380/(Frequency/2), btype='lowpass') # ButterWorth low-filter
# newFilteredSignal = signal.lfilter(c,d,filteredSignal) # Applying the filter to the signal
#
#
# # In[22]:
#
#
# write("testingdata\\NewTest.wav", Frequency, newFilteredSignal) # Saving it to the file.

# sound = AudioSegment.from_wav("F:\\projects\\python\\FinalYearProject\\testingdata\\NewTest.wav")
# sound = sound.set_channels(1)
# sound.export("F:\\projects\\python\\FinalYearProject\\testingdata\\monotest.wav", format="wav")