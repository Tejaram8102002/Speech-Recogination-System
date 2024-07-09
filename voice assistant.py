
import speech_recognition as sr 
import playsound
from gtts import gTTS
import random
import webbrowser
import pyjokes
import os
import time
import pyttsx3
import pywhatkit
import datetime
import wikipedia


class person:
    name = ''

    def setName(self, name):
        self.name = name


class asis:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()


# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down')
        print("You", voice_data.lower())
        return voice_data.lower()


def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(asis_obj.name + ":", audio_string)
    os.remove(audio_file)



def respond(voice_data):

# Greeting
    if there_exists(['hey', 'hi', 'hello', 'hai']):
        greetings = ["hey, how can i help out" + person_obj.name, "How can i help you?" + person_obj.name, "Hello" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

# What's A.I Name
    if there_exists(["what's your name", "what is your name", "Tell us your name", "what should i call you", "tell me your name"]):
        if person_obj.name:
            engine_speak("whats with my name ")
        else:
            engine_speak("I am Bixby, Pleasure meeting you")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name)  # remember name in person object

    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("i have a name, Bixby. but i will remember that name " + asis_name)
        asis_obj.setName(asis_name)


# Google Time
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("search for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")


# Need Stock Prices
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

# Search on amazon
    if there_exists(["amazon"]):
        search_term = voice_data.replace('on amazon', '')
        url = "https://www.amazon.in/" + search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for" + search_term + "on amazon.com")

# Make a Note
    if there_exists(["make a note"]):
        search_term = voice_data.split("for")[-1]
        url = "https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here you can make notes")

# It's IG time
    if there_exists(["open instagram", "IG "]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram")

# Let's open whatsapp web
    if there_exists(["open whatsapp", "whatsapp"]):
        search_term = voice_data.split("for")[-1]
        url = "https://web.whatsapp.com/"
        webbrowser.get().open(url)
        engine_speak("Opening Whatsapp")

# Let's open twitter
    if there_exists(["open twiiter", "twitter"]):
        search_term = voice_data.split("for")[-1]
        url = "https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("Opening Twitter")

# Weather
    if there_exists(["weather", "tell me the weather report", "whats the condition outside"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")

# Mail to See
    if there_exists(["open my mail", "gmail", "check my email"]):
        search_term = voice_data.split("for")[-1]
        url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail")



#  Toss a coin
    if there_exists(["toss", "flip", "coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        engine_speak("The computer chose " + cmove)

# YouTube for Music
    if 'play' in voice_data:
        song = voice_data.replace('play', '')
        engine_speak('playing ' + song)
        print('playing ' + song)
        pywhatkit.playonyt(song)

# what is the time ?
    elif 'time' in voice_data:
        time = datetime.datetime.now().strftime('%I %M %p')
        engine_speak('Current time is ' + time)
        print(time)

# Wikipedia
    elif 'what is' in voice_data:
        meaning = voice_data.replace('what is', '')
        info = wikipedia.summary(meaning, 1)
        print(info)
        engine_speak(info)


# Need some Computer eng. Jokes
    elif 'joke' in voice_data:
        engine_speak(pyjokes.get_joke())

# Curious Question and Answers

    elif 'draw' in voice_data:
        engine_speak("No, but i am learning")

    elif 'sleep' in voice_data:
        engine_speak("Yes, I do sleep and dream too ")

    elif 'eat' in voice_data:
        engine_speak("I eat bits and bytes, I love mega bytes")

    elif 'what do you dream' in voice_data:
        engine_speak("I dream of a nice environment and nature in future")

    elif 'explain me your code' in voice_data:
        engine_speak("It's very simple, all the modules when combine together help me to speak and answer your questions and if i could use neural machine learning I would learn on my own")

    elif 'leader' in voice_data:
        engine_speak("It's Tejaram. Everyone knows that")

    elif ('scripted you') in voice_data:
        engine_speak("It was Anushka.")

    elif ('coded you') in voice_data:
        engine_speak("It was Anushka.")

    elif ('program you') in voice_data:
        engine_speak("It was Anushka.")

# Bixby Calculate
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/",]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Try Again")



# End Comes

    if there_exists(["exit", "quit", "goodbye", "close", "shut", "bye"]):
        engine_speak("kudo's. Have a good day" + person_obj.name)
        exit()


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Bixby'
engine = pyttsx3.init()

while (1):
    voice_data = record_audio("i am listening")
    print("Done")
    print("Q:", voice_data)
    respond(voice_data)