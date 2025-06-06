import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from datetime import datetime, timedelta


r = sr.Recognizer()
engine = pyttsx3.init()
nasaapi = "LBFM3Rtr9BdRQGommKopAK63v0JLdMwQ9BxSb8Nr"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    c = c.lower()
#open links as named.

    if "open chat" in c:
        webbrowser.open("https://chatgpt.com/")
    elif "open google" in c:
        webbrowser.open("https://google.com/")
    elif "open chessboard" in c:
        webbrowser.open("https://chess.com/")
    elif "open insta" in c:
        webbrowser.open("https://instagram.com/")
    elif "corporate labour chowk" in c:
        webbrowser.open("https://linkedin.com/")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com/")
        #plays music from spotify.
    elif c.startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "geomagnetic storm" in c.lower():
        end_date = datetime.today().strftime('%Y-%m-%d')
        start_date = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')  # past 7 days
        url = f"https://api.nasa.gov/DONKI/GST?startDate={start_date}&endDate={end_date}&api_key={nasaapi}"
        try:
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                if data:
                    for storm in data:
                        speak(f"Storm detected on {storm.get('startTime', 'unknown date')}")
                else:
                    speak("No geomagnetic storms detected in the past week.")
            else:
                speak("NASA API request failed.")
        except Exception as e:
            speak(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Listening for 'Jarvis'...")
        try:
            print("Recognising...")
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
                word = r.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yes?")
                    with sr.Microphone() as source:
                        audio = r.listen(source, timeout=5)
                        command = r.recognize_google(audio)
                        process_command(command)
        except sr.WaitTimeoutError:
            continue  # Don't print anything, just wait again
        except sr.UnknownValueError:
            print("Didn't catch that.")
        except Exception as e:
            print(f"Jarvis error: {e}")








