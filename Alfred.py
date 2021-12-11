import speech_recognition as sr 
import datetime
import pyttsx3
import time
import webbrowser
import os
import random
import wikipedia

#Bases
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Respuestas basicas
Answers = ["As you wish sir","Working on it Sir", "As you wish master", "As you wish Bauti", "Working on it Bauti"]
Names = ["Master","Sir","Bauti"]
MayIHelp = ["How may I help you?", "What can I do for you?", "What do you need?"]
date = datetime.datetime.now()

# Aca se hace la funcion para que hable
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Respuesta Random
def random_answer(option):
    Fanswer = random.choice(option)
    return Fanswer

#Abrir apps
def open_apps(app):
    os.system(f"open /Applications/{app}.app")

#Navegar
def browse(site):
    webbrowser.open(f"https://www.{site}.com")

#Atajo Programar
def programming():
    browse("reddit")
    browse("stackoverflow")
    browse("github")
    webbrowser.open("https://open.spotify.com/playlist/3DIjw8eboATMgRN2RC6mz6?si=1bd4d333ccf246d6&nd=1")
    open_apps('"Visual Studio Code"')

#Saludo personalizado
def Personal_Greeting():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning" + random_answer(Names))

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + random_answer(Names))
    
    else:
        speak("Good Evening" + random_answer(Names))

    speak(random_answer(MayIHelp))

#inicializar
def initialating():
    speak("Initialating...")
    Personal_Greeting()

#wikipedia
def wiki(subject):
    speak(f"This is what I found about {subject}")
    webbrowser.open(wikipedia.page(subject).url)

#Que escuche y de respuestas
def operating():
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = r.listen(source)
                rec = r.recognize_google(voice)
                print(rec)
                #Abrir apps
                if "open" in rec:
                    speak(random_answer(Answers))
                    rec_app = list(rec.split(" "))
                    rec_app.pop(0)
                    rec_app = " ".join(rec_app)
                    open_apps(f"'{rec_app}'")
                #Buscxar en Safari
                elif "browse" in rec:
                    speak(random_answer(Answers))
                    rec_site = list(rec.split(" "))
                    rec_site.pop(0)
                    rec_site = "".join(rec_site)
                    browse(rec_site)
                #programar
                elif "programming" in rec:
                    speak(random_answer(Answers))
                    programming()
                    continue
                #day
                elif "day" in rec:
                    print(f"{date.strftime('%A')} {date.strftime('%d')}")
                    speak(f"{date.strftime('%A')} {date.strftime('%d')}")
                    continue
                #month
                elif "month" in rec:
                    print(date.strftime("%B"))
                    speak(date.strftime("%B"))
                    continue
                #time
                elif "time" in rec or "hour" in rec:
                    print(f"{date.strftime('%H')} with {date.strftime('%M')} minutes")
                    speak(f"{date.strftime('%H')} with {date.strftime('%M')} minutes")
                    continue
                #Answer to who are you
                elif rec == "who are you":
                    speak("I'm Alfred, Bauti's personal assistance")
                    continue
                elif rec == "nevermind" or rec == "shut up" or rec == "bye":
                    speak("ok, bye")
                    break
                #wikipedia
                elif "Search" in rec or "search" in rec:
                    rec_site = list(rec.split(" "))
                    rec_site.pop(0)
                    rec_site = "".join(rec_site)
                else:
                    speak("I didn't hear you well, repeat pleace") 
                    continue
        except:
            pass

initialating()
operating()
