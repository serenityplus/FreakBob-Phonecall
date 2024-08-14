import tkinter as tk
from PIL import Image, ImageTk
import os
import pygame
import urllib.request

# Initialize Pygame Mixer for audio playback
pygame.mixer.init()

# Define the paths to the audio files
callsound_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio', 'callsound.mp3')
sadaudio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio', 'sadaudio.mp3')
freakyaudio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio', 'freakyaudio.mp3')

# Flag to track the state of the audio
callsound_playing = False
freaky_audio_played = False

# Function to play the initial audio file in a loop
def play_callsound():
    pygame.mixer.music.load(callsound_path)
    pygame.mixer.music.play(loops=-1)
    global callsound_playing
    callsound_playing = True

# Function to stop the current audio
def stop_audio():
    pygame.mixer.music.stop()

# Function to play the sad audio file once
def play_sad_audio():
    stop_audio()  # Stop any current audio
    pygame.mixer.music.load(sadaudio_path)
    pygame.mixer.music.play()
    
    # Wait for the sad audio to finish, then wait 2 seconds before playing callsound
    sad_audio_length = pygame.mixer.Sound(sadaudio_path).get_length()
    root.after(int(sad_audio_length * 1000 + 2000), play_callsound)

webUrl=urllib.request.urlopen('https://www.python.org/')
# Function to play the freaky audio file once
def play_freaky_audio():
    stop_audio()  # Stop any current audio
    pygame.mixer.music.load(freakyaudio_path)
    pygame.mixer.music.play()
    global freaky_audio_played
    freaky_audio_played = True  # Set the flag that freaky audio has been played

# Function to handle the button click
def on_click(event):
    global callsound_playing, freaky_audio_played
    if callsound_playing and not freaky_audio_played:
        play_freaky_audio()  # Play the freaky audio if callsound is playing and freaky hasn't been played

# Get the path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Relative path to the image in the "Images" folder
image_path = os.path.join(script_dir, 'Images', 'front.jpg')  # Adjust the filename if necessary

# Create the main window
root = tk.Tk()
root.title("FreakBob PhoneCall")

# Load and set the image as the background
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create a canvas to display the image
canvas = tk.Canvas(root, width=photo.width(), height=photo.height(), highlightthickness=0)
canvas.pack()

# Add the image to the canvas
canvas.create_image(0, 0, anchor='nw', image=photo)

# Create a transparent clickable area on the canvas
canvas.create_rectangle(152, 440, 252, 490, fill='', outline='', tags='clickable_area')
canvas.tag_bind('clickable_area', '<Button-1>', on_click)

# Start by playing the sad audio
root.after(1000, play_sad_audio)  # Delay to ensure the GUI is initialized

# Run the application
root.mainloop()
