import numpy as np
import sounddevice as sd

def play_note(note, duration, amplitude=0.3):
    # Define the frequency of the note
    frequency = 440.0 * 2**(note/12.0)

    # Generate the time values for the specified duration
    t = np.linspace(0, duration, int(duration * 44100), endpoint=False)

    # Generate the audio signal for the note
    signal = amplitude * np.sin(2 * np.pi * frequency * t)

    # Play the audio signal
    sd.play(signal, samplerate=44100)
    sd.wait()

# Play A note at 440 Hz for 1 second
play_note(note=0, duration=1)
play_note(note=0, duration=1)
play_note(note=5, duration=1)
play_note(note=5, duration=1)
play_note(note=7, duration=1)
play_note(note=7, duration=1)
play_note(note=5, duration=2)

play_note(note=3, duration=1)
play_note(note=3, duration=1)
play_note(note=2, duration=1)
play_note(note=2, duration=1)
play_note(note=1, duration=1)
play_note(note=1, duration=1)
play_note(note=0, duration=2)



