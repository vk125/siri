import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def input_command():
    try:
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            my_command = listener.recognize_google(voice)
            my_command = my_command.lower()
            if 'siri' in my_command:
                print(my_command)

    except:
        my_command="exception"
        print("microphone not working properly")
    return my_command

def start_siri():
    command = input_command()
    command = command.replace("hey siri","")
    if 'time' in command:
        current_time = datetime.datetime.now().strftime('%H:%M')
        talk(current_time)
    elif 'play' in command:
        song = command.replace("play","")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif "tell me about"  in command:
        keyword = command.replace("tell me about","")
        info = wikipedia.summary(keyword,1)
        talk(info)
    else:
        talk("Sorry! I didn't get that!")

while(True):
    start_siri()









