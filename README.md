# Tornado – Voice Activated Virtual Assistant

**Tornado** is a Python-based voice assistant, similar to Alexa. It listens for a wake word, executes spoken commands, interacts with websites, plays music, and provides intelligent responses using **Google Gemini API**.

---

## Features

- **Wake Word Detection** – Activates when you say *“Hello Tornado”*.  
- **Speech Recognition** – Converts your voice into text using `speech_recognition`.  
- **Text-to-Speech** – Responds with natural voice using `pyttsx3`.  
- **Web Shortcuts** – Quickly open Google, YouTube, and GitHub.  
- **Music Playback** – Plays songs from a custom `musicLibrary`.  
- **Gemini AI Integration** – Provides context-aware answers using Google Gemini API.  
- **Exit Commands** – Stop the assistant with *“exit”*, *“quit”*, or *“stop”*.  

---

### Example Commands to Try After Activation
Say "Hello Tornado" to start listening:
- `Open Google` → Opens Google in your default browser  
- `Open YouTube` → Opens YouTube in your default browser  
- `Play [songname]` → Plays a song from `musicLibrary`  
- `Tell me about AI` → Gets a smart response from Gemini AI  
- `Exit / Quit / Stop` → Shuts down the assistant

---

> **Note:** Refine the prompt to enhance the quality and naturalness of the voice output.

---

## Tech Stack

- **Python** – Core language  
- **speech_recognition** – Voice-to-text conversion  
- **pyttsx3** – Text-to-speech output  
- **webbrowser** – Open websites via commands  
- **dotenv** – Manage environment variables  
- **google-generativeai** – Connects to Google Gemini API  

---

## Installation Commands

```bash
# 1. Clone the repository
git clone https://github.com/asif-shariar7/Tornado.git
cd Tornado

# 2. Create and activate a virtual environment
python -m venv venv
# Windows PowerShell
.\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a file named .env in the Tornado folder and add this line inside it:
# API_KEY=your_gemini_api_key_here

# 5. Run the assistant
python tornado.py