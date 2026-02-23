import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sounddevice as sd

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()


def listen():
    """Capture audio using sounddevice and convert to text."""
    duration = 5  # seconds
    samplerate = 16000
    print("Listening...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    audio_bytes = audio_data.tobytes()
    audio = sr.AudioData(audio_bytes, samplerate, 2)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
def process_command(command):
    """Process recognized voice commands."""
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "play music" in command:
        music_dir = "C:/Users/Public/Music"  # Change path to your music folder
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")
        else:
            speak("No music files found.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I can’t do that yet, but I’m learning.")

def main():
    speak("Hello Aineen, I am your voice assistant Xain. How can I help you?")
    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
