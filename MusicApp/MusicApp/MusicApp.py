#goal make a piano that will take in the number buttons and play notes
#ex 1->A, 2->B, ect
#step 1) make a way to play each note
#setp 2) 

import numpy as np
import sounddevice as sd
import keyboard
import time

def generate_frequency(frequency,duration=1.0, samplerate=44100, amplitude=0.3):
    
    # Generate the audio signal for the note
    t = np.linspace(0, duration, int(duration * samplerate), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)

    return signal

def play(note):
    sd.play(note, samplerate=44100)
    sd.wait()
def play_note(key,frequency):
    if key in key_mapping:
        play(frequency)
        
# Define note
A= generate_frequency(220)
B= generate_frequency(246.94)
C= generate_frequency(261.63)
D= generate_frequency(293.66)
E= generate_frequency(329.63)
F= generate_frequency(349.23)
G= generate_frequency(392)

key_mapping={
    '1':A,
    '2':B,
    '3':C,
    '4':D,
    '5':E,
    '6':F,
    '7':G,
    }


for key,frequency in key_mapping.items():
    keyboard.on_press_key(key, lambda event, k=key,freq=frequency: play_note(k,freq))
keyboard.wait('esc')




