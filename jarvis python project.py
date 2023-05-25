import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour< 12:
        speak("good morning!")
    elif hour>= 12 and hour< 18:

        speak ("good afternoon")
    else:

        speak("good evenning")

    speak( "hello sir  can i help you")
def takeCommand():
        # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e :
            # print (e)   
        print("say that again please...")
        return "None"

    return query
        
if __name__ ==  "__main__":

    # speak("rupesh is a good boy")
    wishMe()
    while True: 

        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query , sentences = 2)
            speak("accoerding to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackflow ' in query:
            webbrowser.open("stackflow.com")
