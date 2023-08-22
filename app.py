from flask import Flask, render_template, Response
import pyttsx3
import speech_recognition as sr
import threading

app = Flask(__name__)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(engine,audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        speak("Unable to Recognize your voice, can you please say that again!!")
        return "None"
    return query

def bot():
    while True:
        query = takeCommand().lower()

        if 'hi' in query or 'hello' in query:
            yield "Yoco here, Team Livewires welcomes you"
        elif "yoco" in query:
            yield "How may I help you"
        
        # Add more responses and actions for different queries here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    def generate():
        for message in bot():
            yield f"data: {message}\n\n"
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    threading.Thread(target=app.run, kwargs={'debug': True}).start()
    bot(engine)
