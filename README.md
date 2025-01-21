
# Voice Assistant Project

This is a Python-based voice assistant that listens for commands and executes various tasks such as opening websites, playing music, and controlling system actions. It uses **speech recognition**, **text-to-speech**, and **wake word detection** to interact with the user.

## Features

- **Voice Wake Word**: Uses Picovoice's Porcupine for wake word detection (Arabic or English).
- **Voice Commands**: Responds to commands like playing music, checking time, and searching the web.
- **Text-to-Speech**: Converts responses into speech using the pyttsx3 library.
- **System Tray Icon**: The assistant runs in the background with a system tray icon that allows you to quit the application.
- **Speech-to-Text**: Converts user speech into text using the Google Speech API.
- **Command Handling**: Supports a variety of actions such as playing songs on YouTube, resetting trials, and shutting down the system.
## Requirements

Make sure you have the following dependencies installed before running the application:

- **Python 3.x**
- **pip** (Python's package installer)

### Install dependencies

```bash
pip install -r requirements.txt
```

### Dependencies:
- `pyttsx3`: Text-to-speech engine for voice responses.
- `speechrecognition`: Recognizes spoken language and converts it to text.
- `pvporcupine`: Used for detecting the wake word.
- `pyaudio`: Provides audio functionality.
- `webbrowser`: Used for opening URLs in the default browser.
- `pystray`: Creates a system tray icon for managing the application.
- `Pillow`: Handles image processing for the system tray icon.
- `python-dotenv`: Loads environment variables from a `.env` file for sensitive information like access keys.

## Setup

1. **Clone this repository**:

    ```bash
    git clone https://github.com/your-username/voice-assistant.git
    cd voice-assistant
    ```

2. **Set your Picovoice Access Key**:
   - Create a `.env` file in the project directory with the following line:
   
     ```
     PICOVOICE_ACCESS_KEY=your_picovoice_access_key_here
     ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Program**:

    ```bash
    python assistant.py
    ```

   The assistant will start listening for the wake word and then process voice commands such as:
   - "Play [song name]" (plays the song on YouTube)
   - "Search for [query]" (searches the web for a query)
   - "What's the time?" (responds with the current time)
   - "Shutdown" (shuts down the program)

2. **To quit the program**, you can click on the system tray icon and select "Quit".

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request. Make sure to follow the contribution guidelines and ensure that all changes are well-documented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Picovoice** for providing the wake word detection library.
- **Google Speech Recognition API** for converting speech to text.
- **pyttsx3** for text-to-speech synthesis.
- **pystray** for the system tray functionality.

---

ps: this is just a fun little project that iv work at for two days , so if there are any flaws or errors feel free to correct them. Gobbi Mohaned 21/01/2025