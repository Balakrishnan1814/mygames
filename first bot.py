import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

lis=sr.Recognizer()
machine = pyttsx3.init()
tones = machine.getProperty('voices')
machine.setProperty('voice', tones[1].id)


def chat(talk):
    machine.say(talk)
    machine.runAndWait()


def tell_ai():
    try:
        with sr.Microphone() as source:
            print('listening')
            vc = lis.listen(source)
            text = lis.recognize_google(vc)
            text = text.lower()
            print(text)
    except:
        pass
    return text


def run_ai():
    order = tell_ai()
    if "play" in order:
        music = order.replace("play","")
        chat("playing"+ music)
        pywhatkit.playonyt(music)
    elif "time" in order:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        chat("now the time is" + time)
    else:
        chat("wait i will tell u")
        thing = order.replace("tell about", "")
        about = wikipedia.summary(thing,2)
        print(about)
        chat(about)


run_ai()