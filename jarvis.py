import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak ("Hello I am jarvis, How may I help you?")

def takeCommand():
    #It takes microphone inputfrom the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1 #gives times before considered phase is complete
        audio = r.listen(source)

    try:
        print("recogninzing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
    
    except Exception as e:
        print(e)

        print("Say that Again Please...")
        return "None"
    return query

if __name__ == "__main__":
    #speak("Pratik is good boy")
    WishMe()
    #while True:
    if 1:
        #query = takeCommand().lower()
        query = 'please quit yourself'
    #Logic for executing the tasks based on query
        if 'wikipedia' in query:
            speak('Searchin wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary('query', sentences=2)
            speak("Acccording to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open geekforgeeks' in query:
            webbrowser.open("geekforgeeks.com")


        elif 'play music' in query:
            music_dir  = ""
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif "quit yourself" in query:
            exit
        
