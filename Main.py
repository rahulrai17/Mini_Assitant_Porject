import pyttsx3
import speech_recognition as sr 
import datetime
import pywhatkit
import wikipedia as googleScrap
import Features
import webbrowser as web
import os
import automation


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)
engine.setProperty('rate' ,170)

def speak(audio):
    print("    ")
    print(f": {audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(": Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f": your Command : {query}\n")

    except:
        return ""


    return query.lower()            
 

if __name__ == "__main__":
    Features.wishMe()
    speak("what would you like my help with sir, there are a list of commands i can help you with")
    print("1.My Introduction (command - introduce yourself)")
    print("2.Bowser (command - browser)")
    print("3.Tell Time (command - time)")
    print("4.Play Music (command - play music)")
    print("5.Open Apps (command - open apps)")
    print("6.send message in whatsapp (command - use whatsapp)")
    command = TakeCommand()
    if 'introduce yourself' in command:
        Features.introduction()
    elif 'browser' in command:
        Features.browser()
    elif 'time' in command:
        Features.TimeTeller()
    elif 'play music' in command:
        Features.playMusic()
    elif 'open apps' in command:
        Features.openApps()
    elif 'use whatsapp' in command:
        automation.whatsapp()    
     
    else:
        speak("sorry sir , i am unable to help you with this right now")             
            