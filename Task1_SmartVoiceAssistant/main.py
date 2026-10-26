
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from urllib.parse import quote_plus

engine = pyttsx3.init()
engine.setProperty("rate", 170)

recognizer = sr.Recognizer()


def speak(message):
    print("Assistant:", message)
    engine.say(message)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(
                source, timeout=5, phrase_time_limit=8
            )

        command = recognizer.recognize_google(audio).lower().strip()
        print("You:", command)
        return command

    except sr.WaitTimeoutError:
        speak("I did not hear anything. Please try again.")
    except sr.UnknownValueError:
        speak("Sorry, please repeat your command.")
    except sr.RequestError:
        speak("Please check your internet connection.")
    except OSError:
        speak("Please check your microphone.")

    return ""


def process_command(command):
    if not command:
        return True

    if command in ["exit", "quit", "goodbye", "stop"]:
        speak("Goodbye! Have a nice day.")
        return False

    elif "hello" in command or command == "hi":
        speak("Hello! How can I help you?")

    elif "how are you" in command:
        speak("I am fine. Thank you!")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open gmail" in command:
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com")

    elif command.startswith("search "):
        query = command[len("search "):].strip()

        if query:
            speak("Searching Google for " + query)
            webbrowser.open(
                "https://www.google.com/search?q=" + quote_plus(query)
            )
        else:
            speak("Please tell me what to search.")

    else:
        speak("I do not know that command. Try saying search followed by your topic.")

    return True


def main():
    print("=" * 40)
    print("       SMART VOICE ASSISTANT")
    print("=" * 40)
    print("Try: Hello, What is the time, What is the date")
    print("Try: Open Google, Open YouTube, Search Python")
    print("Say Exit to close the assistant.")

    speak("Hello! Your smart voice assistant is ready.")

    while True:
        command = listen()
        if not process_command(command):
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("Voice assistant stopped.")
