import tkinter as tk
from PIL import Image, ImageTk
import os
import pygame
import urllib.request

pygame.mixer.init()

callsound_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio', 'callsound.mp3')
sadaudio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio', 'sadaudio.mp3')
freakyaudio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio', 'freakyaudio.mp3')

callsound_playing = False
freaky_audio_played = False

def play_callsound():
    pygame.mixer.music.load(callsound_path)
    pygame.mixer.music.play(loops=-1)
    global callsound_playing
    callsound_playing = True

def stop_audio():
    pygame.mixer.music.stop()

def play_sad_audio():
    stop_audio()  # Stop any current audio
    pygame.mixer.music.load(sadaudio_path)
    pygame.mixer.music.play()
    
    sad_audio_length = pygame.mixer.Sound(sadaudio_path).get_length()
    root.after(int(sad_audio_length * 1000 + 2000), play_callsound)

webUrl=urllib.request.urlopen('https://www.python.org/')
def play_freaky_audio():
    stop_audio() 
    pygame.mixer.music.load(freakyaudio_path)
    pygame.mixer.music.play()
    global freaky_audio_played
    freaky_audio_played = True  

def on_click(event):
    global callsound_playing, freaky_audio_played
    if callsound_playing and not freaky_audio_played:
        play_freaky_audio() 

script_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(script_dir, 'Images', 'front.jpg')  # Adjust the filename if necessary


root = tk.Tk()
root.title("FreakBob PhoneCall")

image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=photo.width(), height=photo.height(), highlightthickness=0)
canvas.pack()

canvas.create_image(0, 0, anchor='nw', image=photo)

canvas.create_rectangle(152, 440, 252, 490, fill='', outline='', tags='clickable_area')
canvas.tag_bind('clickable_area', '<Button-1>', on_click)

root.after(1000, play_sad_audio)  # Delay to ensure the GUI is initialized


root.mainloop()
