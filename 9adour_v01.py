import threading
import sys
from pydoc import importfile
import speech_recognition as sr
import pyttsx3
import pvporcupine
import pyaudio
import struct
from datetime import datetime
import webbrowser
from StringRelated import extract_search_query
from FileRealated import execute_executable
from InternetRelated import play_song_on_youtube
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import os
Access_key = os.getenv('PICOVOICE_ACCESS_KEY')

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Global flag to stop background threads
running = True


def listen_and_recognize():
    """Listens to the user's voice and converts it to text using Google Speech Recognition."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, the service is down.")


def speak(text):
    """Converts text to speech using the pyttsx3 engine."""
    engine.say(text)
    engine.runAndWait()


def detected_callback():
    """Callback function triggered when the wake word is detected."""
    print("Wake word detected!")
    speak("What do you need, sir?")
    command = listen_and_recognize()
    if command:
        handle_command(command)

def handle_command(command):

    """Handles user commands and performs corresponding actions."""
    # Convert the command to lowercase to ensure case-insensitive matching
    command = command.lower()
    if "clip" in command:
        speak(f"I will {command} sir")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}.")
    elif "search for" in command:
        query = extract_search_query(command,"search for")
        if query:
            speak(f"Searching for {query} on the web.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "play" in command:
        query = extract_search_query(command, "play")
        if query:
            speak(f"Playing {query} on YouTube.")
            play_song_on_youtube(query)
            speak("I have opened YouTube with the top search results for you.")

    elif "trial reset" in command:
        speak("Opening the trial reset file")
        execute_executable("D:\\Trials\\IDM.Trial.Reset.v1.0.0\\IDM Trial Reset.exe")
    elif any(keyword in command for keyword in ["turn off", "shutdown", "shut down"]):
        speak("Turning off. Have a good night, sir.")
        stop_application()
    else:
        speak("I'm sorry, I can't help with that yet.")

def start_porcupine():
    """Initializes Porcupine for wake word detection and starts listening."""
    global running
    model_path = "D:\\software and studying\\9adour\\wake-up-kadour_en_windows_v3_0_0.ppn"
    porcupine = pvporcupine.create(
        access_key=Access_key,  # Replace with your Picovoice access key
        keyword_paths=[model_path]
    )
    audio_stream = pyaudio.PyAudio().open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Listening for the wake word...")
    try:
        while running:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                detected_callback()
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        audio_stream.close()
        porcupine.delete()


def stop_application():
    """Stops the application gracefully."""
    global running
    running = False
    icon.stop()
    sys.exit()


def create_tray_icon():
    """Creates a system tray icon."""
    # Create a simple image for the icon
    image = Image.new('RGB', (64, 64), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill="blue")

    # Define menu options
    menu = Menu(
        MenuItem("Quit", lambda: stop_application())
    )

    return Icon("Voice Assistant", image, "Voice Assistant", menu)


if __name__ == "__main__":
    # Start Porcupine in a background thread
    porcupine_thread = threading.Thread(target=start_porcupine, daemon=True)
    porcupine_thread.start()

    # Create and run the system tray icon
    icon = create_tray_icon()
    icon.run()
