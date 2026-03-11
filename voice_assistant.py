import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen to microphone
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

# Command handler
def execute_command(command):

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The current time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "search" in command:
        speak("What do you want to search?")
        query = listen()
        if query:
            webbrowser.open("https://www.google.com/search?q=" + query)
            speak("Searching for " + query)

    elif "open notepad" in command:
         speak("Opening Notepad")
         os.startfile("notepad.exe")

    elif "open calculator" in command:
         speak("Opening Calculator")
         os.startfile("calc.exe")

    elif "open chrome" in command:
         speak("Opening Google Chrome")
         os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif "open youtube" in command:
         speak("Opening YouTube")
         webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
         speak("Opening Google")
         webbrowser.open("https://www.google.com")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I don't know that command yet.")

# Main program
speak("Voice assistant started")

while True:
    command = listen()
    if command:
        execute_command(command)