#goal make a piano that will take in the number buttons and play notes
#ex 1->A, 2->B, ect
#step 1) make a way to play each note
#setp 2) 

#from re import A
import numpy as np
import sounddevice as sd

import numpy as np
import sounddevice as sd

def generate_frequency(frequency, duration, samplerate=44100, amplitude=0.3):

    # Generate the audio signal for the note
    t = np.linspace(0, duration, int(duration * samplerate), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)

    return signal

def play(note):
    sd.play(note, samplerate=44100)
    sd.wait()

# Define note
A= generate_frequency(220, duration=1)
B= generate_frequency(246.94, duration=1)
C= generate_frequency(261.63, duration=1)
D= generate_frequency(293.66, duration=1)
E= generate_frequency(329.63, duration=1)
F= generate_frequency(349.23, duration=1)
G= generate_frequency(392, duration=1)


play(G)
play(A)



