import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import pyaudio
import wikipedia
import requests
#it has a male voice by default
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
def input():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("speak....")
        r.pause_threshold=2
        spoken=r.listen(source)
        try:
            print("Listening and trying to recognize")
            statement=r.recognize_google(spoken)
            print(f"user said -{statement}")
        except Exception as e:
            speak("Could not recognize ... Please repeat")
            return None
        return statement
def wishes():
    hours=datetime.datetime.now().hour
    if hours>=0 and hours<12:
        speak("Hi ,Good Morning")
        print("Hi,Good Morning")
    elif hours>=12 and hours<18:
        speak("Hi ,good afternoon")
        print("Hi, Good Afternoon")
    else:
        speak("Hi good evening")
        print("Hi good evening")
    speak("I am your assistant and my name is Pinaka")
def name_user():
    speak("may i know your name")
    user_name=input()
    speak(f"{user_name}")
    print(f"{user_name}...how may i help you today")
    speak("how may I help you today")


#now the main function starts here
wishes()
name_user()


'''Search 
Wikipedia
How are you
Open youtube
Fine
Exit
What is your name
weather'''
while True:
    query=input().lower()
    if "Search" in query or "Wikipedia" in query:
        speak("tell your query")
        query=input()
        results=wikipedia.summary(query,sentences=4)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif "How are you" in query:
       print("i am fine and what about you")
       speak("I am fine and what about you")
    elif "I am fine" in query or "I am good" in query:
        print("glad to hear that you are fine")
        speak("glad to hear that you are fine")
    elif "what is your name" in query:
        print("My name is Pinaka")
        speak("My name is Pinaka")
    elif "what is the weather today" in query:
        speak("city name")
        print("city name:")
        city=input()
        api_key=API
        x = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=={api_key}").json()
        y = x["main"]
        current_temperature = y["temp"]-273.15
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature " + str(
            current_temperature) + "\n atmospheric pressure = " + str(
            current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(
            weather_description))
        speak(" Temperature " + str(
            current_temperature) + "\n atmospheric pressure = " + str(
            current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(
            weather_description))
    elif "exit" or "quit" in query:
        print("thankyou for your time")
        exit()