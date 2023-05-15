import wave
import random
import math

# Define parameters for the wave file
sample_width = 2  # 16-bit audio
num_channels = 1  # mono audio
sample_rate = 44100  # CD quality audio
bpm = 120

# Define the length of the audio sample in seconds
duration = 12

# A Major:
# A3, B3, C#4, D4, E4, F#4, G#4
# Bb Major:
# Bb3, C4, D4, Eb4, F4, G4, A4
# B Major:
# B3, C#4, D#4, E4, F#4, G#4, A#4
# C Major:
# C4, D4, E4, F4, G4, A4, B4
# C# Major:
# C#4, D#4, F4, F#4, G#4, A#4, C5
# D Major:
# D4, E4, F#4, G4, A4, B4, C#5
# Eb Major:
# Eb4, F4, G4, Ab4, Bb4, C5, D5
# E Major:
# E4, F#4, G#4, A4, B4, C#5, D#5
# F Major:
# F4, G4, A4, Bb4, C5, D5, E5
# F# Major:
# F#4, G#4, A#4, B4, C#5, D#5, F5
# G Major:
# G4, A4, B4, C5, D5, E5, F#5
# Ab Major:
# Ab4, Bb4, C5, Db5, Eb5, F5, G5

# A Major F♯ minor:
# 220.00, 246.94, 277.18, 293.66, 329.63, 369.99, 415.30 
# A♯ Major G minor:
# 233.08, 277.18, 311.13, 329.63, 369.99, 415.30, 466.16
# B Major G♯ minor:
# 246.94, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88 
# C Major A minor:
# 261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88 
# C♯ Major A♯ minor:
# 277.18, 311.13, 349.23, 369.99, 415.30, 466.16, 523.25
# D Major B minor:
# 293.66, 329.63, 369.99, 392.00, 440.00, 493.88, 554.37
# D♯ Major B♯ minor:
# 311.13, 349.23, 392.00, 415.30, 466.16, 523.25, 587.33 
# E Major C♯ minor:
# 329.63, 369.99, 415.30, 440.00, 493.88, 554.37, 622.25
# F Major D minor:
# 349.23, 392.00, 440.00, 466.16, 523.25, 587.33, 659.25
# F♯ Major D♯ minor:
# 369.99, 415.30, 466.16, 493.88, 554.37, 622.25, 698.46
# G Major E minor:
# 392.00, 440.00, 493.88, 523.25, 587.33, 659.25, 739.99
# G♯ Major E♯ minor:
# 415.30, 466.16, 523.25, 554.37, 622.25, 698.46, 783.99


# Lydian:
# F#: 369.99, 415.30, 466.16, 523.25, 587.33, 659.26, 739.99
# Pentatonic Major:
# C: 261.63, 329.63, 392.00, 493.88, 587.33
# Pentatonic Minor:
# A: 220.00, 261.63, 311.13, 392.00, 440.00
# Blues:
# F: 349.23, 392.00, 440.00, 466.16, 523.25, 587.33, 659.26

# Define parameters for the notes
notes = [349.23, 392.00, 440.00, 466.16, 523.25, 587.33, 659.26]  # frequencies of C4 - B4 notes
notes_2x_CM_Am = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 522.26, 587.32, 659.26, 698.46, 784.00, 880.00, 987.76]  # frequencies of C4 - B5 notes

note_duration_4 = bpm/60/4  # duration of each note in seconds
note_duration_8 = bpm/60/8
note_duration_16 = bpm/60/16
note_duration = random.choice([note_duration_4, note_duration_8, note_duration_16])
note_samples = int(note_duration_4 * sample_rate)  # number of audio samples for each note

# Create a new wave file and set its parameters
with wave.open("random_music.wav", "w") as audio_file:
    audio_file.setparams((num_channels, sample_width, sample_rate, 0, "NONE", "not compressed"))

    # Generate audio samples and write them to the wave file
    for i in range(int(sample_rate * duration)):
        if i % note_samples == 0:
            # Generate a new note every note_samples audio samples
            frequency = random.choice(notes)
            amplitude = random.randint(5000, 15000)
            phase = random.uniform(0, 2 * math.pi)
        sample = int(amplitude * math.sin(2 * math.pi * frequency * i / sample_rate + phase))
        audio_file.writeframes(sample.to_bytes(sample_width, byteorder="little", signed=True))
