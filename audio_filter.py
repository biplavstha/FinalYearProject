from pydub import AudioSegment

# Replace this with the location of your downloaded file.
def mono():
    sound = AudioSegment.from_wav("F:\\projects\\python\\FinalYearProject\\testingdata\\test.wav") #imports the audio file
    sound = sound.set_channels(1) #change recorded audio to mono
    sound.export("F:\\projects\\python\\FinalYearProject\\testingdata\\monotest.wav", format="wav") #save mono audio file



