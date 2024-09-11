import speech_recognition as sr
import os
import pyttsx3


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language="en-us")
        print(f"User said: {query}")
        return query

if __name__ == '__main__':
    print('J.A.R.V.I.S')
    say("Hi, I am Cadbury, how can I assist you")
    print("Listening...")
    text = takeCommand()
    say(text)
