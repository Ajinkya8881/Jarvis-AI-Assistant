import datetime
import pyttsx3
import webbrowser
import speech_recognition as sr
import wikipedia

MASTER = "Master AK"
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty("voices")[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_user():
    current_time = datetime.datetime.now().hour
    if 0 <= current_time <= 12:
        speak(f"Good morning {MASTER}")
    
    elif 12 <= current_time <= 18:
        speak(f"Good afternoons {MASTER}")

    else:
        speak(f"Good evening {MASTER}")

    speak("How can i assist you today?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Listening.....")
        return r.recognize_google(audio, language = 'en-in' ) .lower()
    except Exception as e:
        speak("sorry somethng went wrong!")
        return ""
    
def search_wikipedia(query):
    try:
        speak("searching wikipedia...")
        result = wikipedia.summary(query, sentences = 2)
        speak(result)

    except Exception as e:
        speak("sorry i could'nt find any information")

def main():
    speak("Initializing jarvis......")
    greet_user()

    while True:
        query = take_command()

        if query:
            if "wikipedia" in query:
                search_wikipedia(query.replace('wikipedia', ""))

            if "open youtube" in query:
                webbrowser.open("https://www.youtube.com")
            if "open google" in query:
                webbrowser.open("https://www.google.com")
            if "the time" in query:
                current_time = datetime.datetime.now().strftime("%H, %M, %S ")
            if "exit" in query:
                speak("goodbye!!!")
                break

if __name__ == "__main__":
    main()


    
    
