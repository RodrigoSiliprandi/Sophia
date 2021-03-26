#Our main file.
 ''''
import speech_recognition as sr
#Cria um reconhecedor
r = sr.Recognizer()

#Abrir o microfone para captura
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)
    
        print(r.recognize_google(audio, language='pt-PT'))
''''

from vosk import Model, KaldiRecognizer
import os 
import pyaudio

model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stram = p.open(format=pyaudio.paInt16, chanels=1, rate=16000, input=True, frames_per_buffer=8000)
stram.start_stream()

while True:
    data = stram.read(4000)
    if len(data) == 0:
        break
    if AcceptWaveForm(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())
        
print(rec.FinalResult())


