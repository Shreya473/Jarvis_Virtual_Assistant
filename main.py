from openai import OpenAI
import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclib
from gtts import gTTS
import pygame
import os
recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
#use all these with a mp3 file only    
# gtts is use to convert text-to-speech   
# def speak (text):
#       tts= gTTS(text)
#       tts.savee('temp.mp3') 
     
      


# # Initialize Pygame mixer
# pygame.mixer.init()

# # Load the MP3 file
# pygame.mixer.music.unload()

# # Play the MP3 file
# pygame.mixer.music.play()

# # Keep the script running so the music can play
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)
# os.remove('temp.mp3')
      
def aiProcess(command):
    client=OpenAI(
        api_key="# Enter your own secret key #",
    )
    completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a Virtual Assistant name Jarvis skilled like Alexa and Google Cloud, give short responses please"},
    {"role": "user", "content": command}
  ]
)
    return completion.choices[0].message.content 
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open canva" in c.lower():
        webbrowser.open("https://www.canva.com/")    
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclib.music[song]
        webbrowser.open(link)
    else:
      output= aiProcess(c)
      speak(output) 
      
       
if __name__ == "__main__":
    speak("Maam,How may I help you")
    while True:
        #Listen for the wake word "Jarvis"
        #Obtain audio from the microphone
        r=sr.Recognizer()    
        print("recognizing...")
        try: 
            with sr.Microphone() as source:
                print("Listening....")
                audio=r.listen(source)
            word= r.recognize_google(audio)
            if (word.lower()=="hello jarvis"):
                speak("Ya")
                
            #Listen for the command
            
            with sr.Microphone() as source:
                    print("Jarvis Activate....")
                    audio=r.listen(source, timeout=2, phrase_time_limit=5)
                    command= r.recognize_google(audio)
            
                    processCommand(command )
            
        except Exception as e:
            print("Error;{0}".format(e))
         