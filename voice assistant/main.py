import os
import time
import playsound
from gtts import gTTS
import speech_recognition as sr
import pyaudio

def speak(text):
      tts = gTTS(text=text)
      filename = "voice.mp3"
      tts.save(filename)
      playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         audio = r.listen(source)
         said = ""

    try:
        said = r.recognize_google(audio)
        print(said)
        return said

    except Exception as e:
        print("exception: "+ str(e))
        
text = get_audio()




if  "developed"and "develop" in text:
    speak("i am developed by ayan chavand!!!")

if "hello" in text:
    speak("hi!, my name is zeedTech!!")

if "my name" in text:
    speak("your name is harsha")

if "father" in text:
    speak("your fathers name is anil!")

if "Ayan" and "who is Ayan" in text:
    speak("my god!") 

if "about developer" and "about Ayan" in text:
    speak("i am developed by ayan chavand. A student of Kendriya vidyalaya ,in class 9th B.")
   
