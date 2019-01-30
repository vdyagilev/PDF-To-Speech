import subprocess
import pyttsx3
from gtts import gTTS

def convert_pdf_to_raw_text(pdf: str) -> str:
    """Converts a pdf into text with pdf2txt.py program"""
    process = subprocess.Popen(['pdf2txt.py', pdf], stdout=subprocess.PIPE)
    raw_text = process.communicate()[0]

    return raw_text.decode("utf-8")

def sanitize_text(text: str) -> str:
    """Sanitizes and removes all useless characters from the text, returns sanitized text string"""
    alphanum_text = ""
    for letter in list(text):
        if letter.isalnum() or letter == " " or letter in "!?.,:;\'\"&()$%#@~":
            alphanum_text += letter

    return alphanum_text

def speak(text: str, rate: int, speaker: str):
    engine = pyttsx3.init()
    # good voice id is com.apple.speech.synthesis.voice.daniel or com.apple.speech.synthesis.voice.samantha
    engine.setProperty('voice', "com.apple.speech.synthesis.voice." + speaker)
    engine.setProperty('rate', engine.getProperty('rate') + rate)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def text_to_mp3(text: str, file_output: str):
    tts = gTTS(text, lang='en')
    tts.save(file_output+ '.mp3')

def run(file: str):
    text = convert_pdf_to_raw_text(file+".pdf")
    text = sanitize_text(text)
    text_to_mp3(text, file)


run('nsp')
run
