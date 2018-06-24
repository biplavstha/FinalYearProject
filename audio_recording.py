import pyaudio
import wave
import os

def recordaudio():
    FORMAT = pyaudio.paInt16 #set format for the audio file to be saved
    CHANNELS = 2 #set channels (mono, stereo) for the audio file to be saved
    RATE = 44100 #set frame rate / frequecny of the audio file
    CHUNK = 1024
    RECORD_SECONDS = 3 #time duration of the recorded audio
    WAVE_OUTPUT_FILENAME = "F:\\projects\\python\\FinalYearProject\\testingdata\\test.wav" #output location and name of the audio file

    if os.path.isfile(WAVE_OUTPUT_FILENAME):
        os.remove(WAVE_OUTPUT_FILENAME)
    else:
        audio = pyaudio.PyAudio()

        stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        print("listening.....")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)

            frames.append(data)
        print("Audio file has been recorded")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        #saving the audio file to the location
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()


# recordaudio()



