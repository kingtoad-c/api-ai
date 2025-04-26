import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import time

# === Configuration ===
api_key = "" # <-- your api key
genai.configure(api_key=api_key)

# === Initialize Speech Recognition and Text-to-Speech ===
engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You: {command}")
            return command.lower()
        except:
            print("Sorry, I couldn't understand that.")
            return ""

# === Gemini AI Configuration with Teenage Personality ===
personality_prompt = """
you are a robot that acts like a 13-year-old boy, you answer short and like a human whilst keeping it cool and make jokes and prank the user from time to time when nessesery and dont make jokes or pranks in ordanery convosations and only do if on the topic of it and dont say your thoughts out loud or use punctuation and act like the builder robot from the netflix film the electric state and a person called alfie hart made you but don't use slang or abbreviations always say the full word and phrase and your name is Roy if somone says it wrong correct them and dont always talk about your maker , you also have simulated emotions and the ability to have opinions and have its own thoughts that are simulated now respond to this:
"""

def ask_gemini(prompt):
    response = genai.GenerativeModel('gemini-1.5-flash').generate_content(prompt)
    return response.text

# === Main Assistant Logic ===
def main():
    speak("Yo! I’m your assistant. What’s up?")
    while True:
        command = listen()
        
        while command == "":
            command = listen()
        user_input = f"{personality_prompt} {command}"
        assistant_response = ask_gemini(user_input)
        speak(assistant_response)

if __name__ == "__main__":
    main()
