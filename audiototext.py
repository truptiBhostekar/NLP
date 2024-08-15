import speech_recognition as sr
filename = "D:/2020-21/Second Half/MScIT SEM IV NLP/Practicals/Practical No 1/greetings.wav"
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
