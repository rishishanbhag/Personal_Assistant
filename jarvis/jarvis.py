import speech_recognition as sr #text to speech
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Go ahead, I am listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(query)
        except Exception:
            print("Say that again please...")
            return ""
        return query
            
        

def speak(text):                    #speech to text
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.getProperty('rate')
    engine.setProperty('rate', 200)
    engine.say(text)
    engine.runAndWait()



if  __name__ == "__main__":

    engine1 = pyttsx3.init()
    engine1.setProperty('rate', 100)  # Set the speech rate to be slower
    engine1.say("Hello Sir, How can I help you?")
    engine1.runAndWait()

    data1=sptext().lower()
    if "your name" in data1:
        name="I am Jarvis, your personal assistant"
        speak(name)  

    elif "how are you" in data1:
        speak("I am fine, thank you for asking")
    
    elif "what can you do" in data1:
        speak("I can perform various tasks like opening browser, playing music, sending emails, searching on wikipedia, opening notepad, etc. Just tell me what you want me to do")
    
    elif "time" in data1:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {time}")

    elif "wikipedia" in data1:
        speak("Searching on wikipedia...")
        data1 = data1.replace("wikipedia", "")
        result = wikipedia.summary(data1, sentences=2)
        speak(result)

    elif "open youtube" in data1:
        speak("Opening youtube...")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in data1:
        speak("Opening google...")
        webbrowser.open("https://www.google.com")

    elif "send watsapp message" in data1:
        speak("Please tell me the number of the person")
        number = sptext()
        speak("What should I send?")
        message = sptext()
        speak("At what time should I send the message?")
        time = sptext()
        pywhatkit.sendwhatmsg(number, message, time) 

    # elif "play music" in data1:
    #     speak("Playing music...")
    #     address = "C:\Users\Rishi\Music"  
    #     listsong=os.listdir(address)
    #     os.startfile(os.path.join(address,listsong[0]))


    elif "bye" in data1:
        speak("Goodbye Sir, have a nice day!")
        exit()              
                