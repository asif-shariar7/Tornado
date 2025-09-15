import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key= os.getenv("API_KEY"))


recognizer = sr.Recognizer()


def speak(text):
    print(f"Tornado: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def askGemini(user_input):

    prompt = f"You are an AI assistant named Tornado, and you work like Alexa. Always present lists as numbered items (1., 2., 3., …). Never use asterisks (*) or bullet points in your response. The question is: '{user_input}'"

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text.strip()
        elif hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].content.parts[0].text.strip()
        else:
            return "Sorry, I didn't get any response from Gemini."
            
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, I couldn't connect to Gemini."


def processCommand(command):
    c = command.lower()

    if c == "open google":
        speak("Opening Google...")
        webbrowser.open("https://google.com")
    elif c == "open youtube":
        speak("Opening YouTube...")
        webbrowser.open("https://youtube.com")
    elif c == "open github":
        speak("Opening GitHub...")
        webbrowser.open("https://github.com")
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")   
    elif c in ["exit", "quit", "stop"]:
        speak("Goodbye!")
        exit()
    else:
        output = askGemini(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Tornado...")
    while True:
        try:
            print("Waiting for wake word...")
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                
                if word.lower() == "hello tornado":
                    speak("Yes, I am listening...")
                    
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
        except Exception as e: 
            print(f"Error: {e}")