import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def voice_assistant():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said: " + command)

            if "hello" in command:
                speak("Hello! How can I assist you today?")

            elif "what's the time" in command:
                import datetime
                time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {time}.")

            elif "headache" in command:
                speak("I can suggest a few general tips for dealing with a headache. You might want to try drinking water, resting in a dark and quiet room, or taking over-the-counter pain relievers. If the headache persists, its essential to consult a medical professional for proper advice")
                print("Remedy")
                print("Sumo tablets dispensed ")
                print("Take rest, sleep well, don't strain yourself")
                exit()

            elif "cold" in command:
                speak("For a cold, its a good idea to rest, drink plenty of fluids, and use over-the-counter cold medications as needed. If your symptoms worsen or persist, consult a doctor for further guidance")
                print("Remedy")
                print("Clean the nose often. Have warm water, avoid cold and oily food")
                print("Ceteizine Dispensed")
                exit()
            
            elif "fever" in command:
                speak("If you have a fever, its important to monitor your temperature and stay hydrated. You may consider taking fever-reducing medication, but if the fever persists or worsens, seek medical advice")
                print("Remedy")
                print("Dolo 650 dispensed  ")
                print("Please drink warm water and take rest ")
                exit()
            
            else:
                speak("I'm sorry, I don't understand that can you speek again.")

        except sr.UnknownValueError:
            print("Sorry, I could not understand your command.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Main loop
if _name_ == "_main_":
    speak("Hello! I am your Health ATM.")
    while True:
        voice_assistant()
