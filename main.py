import os
import random
import tkinter as tk
from tkinter import ttk
from pydub import AudioSegment
from pydub.generators import Sine



# Dictionary mapping notes to frequencies (equal temperament tuning)
notes_to_frequencies = {    
    "C": 261.63,
    "C#": 277.18,
    "D": 293.66,
    "D#": 311.13,
    "E": 329.63,
    "F": 349.23,
    "F#": 369.99,
    "G": 392.00,
    "G#": 415.30,
    "A": 440.00,
    "A#": 466.16,
    "B": 493.88,
}

# Dictionary mapping modes to note steps (whole and half)
modes_to_steps = {
    "ionian (major)":       [2, 2, 1, 2, 2, 2, 1],
    "aeolian (minor)":      [2, 1, 2, 2, 1, 2, 2],
    "phrygian":             [1, 2, 2, 2, 1, 2, 2],
    "lydian":               [2, 2, 2, 1, 2, 2, 1],
    "mixolydian":           [2, 2, 1, 2, 2, 1, 2],
    "dorian":               [2, 1, 2, 2, 2, 1, 2],
    "locrian":              [1, 2, 2, 1, 2, 2, 2],
    "major pentatonic":     [2, 2, 3, 2, 3],
    "minor pentatonic":     [3, 2, 2, 3, 2],
    "blues":                [3, 2, 1, 1, 3, 2],
    "harmonic minor":       [2, 1, 2, 2, 1, 3, 1],
    "melodic minor asc":    [2, 1, 2, 2, 2, 2, 1],
}

# note_duration_options = [
#     ("1/32",    7500.0),
#     ("1/16",    15000.0),
#     ("1/8",     30000.0),
#     ("1/6",     40000.0),
#     ("1/4",     60000.0),
#     ("1/3",     80000.0),
#     ("1/2",     120000.0),
#     ("1",       240000.0),
# ]



#############################################################################
#  __       __  ________  ________  __    __   ______   _______    ______   #
# /  \     /  |/        |/        |/  |  /  | /      \ /       \  /      \  #
# $$  \   /$$ |$$$$$$$$/ $$$$$$$$/ $$ |  $$ |/$$$$$$  |$$$$$$$  |/$$$$$$  | #
# $$$  \ /$$$ |$$ |__       $$ |   $$ |__$$ |$$ |  $$ |$$ |  $$ |$$ \__$$/  #
# $$$$  /$$$$ |$$    |      $$ |   $$    $$ |$$ |  $$ |$$ |  $$ |$$      \  #
# $$ $$ $$/$$ |$$$$$/       $$ |   $$$$$$$$ |$$ |  $$ |$$ |  $$ | $$$$$$  | #
# $$ |$$$/ $$ |$$ |_____    $$ |   $$ |  $$ |$$ \__$$ |$$ |__$$ |/  \__$$ | #
# $$ | $/  $$ |$$       |   $$ |   $$ |  $$ |$$    $$/ $$    $$/ $$    $$/  #
# $$/      $$/ $$$$$$$$/    $$/    $$/   $$/  $$$$$$/  $$$$$$$/   $$$$$$/   #
#                                                                           #
#############################################################################

def get_scale(root_note, mode):
    scale = [root_note]
    steps = modes_to_steps[mode]
    current_note = root_note
    for step in steps:
        index = list(notes_to_frequencies.keys()).index(current_note)
        next_index = (index + step) % len(notes_to_frequencies)
        current_note = list(notes_to_frequencies.keys())[next_index]
        scale.append(current_note)
    return scale

def generate_music():
    mode = mode_var.get()
    bpm = int(bpm_var.get())
    root_note = note_var.get()
    length = int(length_var.get())

    # Create an empty audio segment to store the notes
    melody = AudioSegment.empty()

    # Randomly select notes and their durations to create the melody
    note_duration_options = [30000/bpm, 60000/bpm]  # Milliseconds (1/8, 1/4, 1/2, 1 second)
    total_duration = 0

    # Get the scale for the selected root note and mode
    scale = get_scale(root_note, mode)

    while total_duration < length * 1000:
        # Randomly select a note from the scale
        note = random.choice(scale)
        frequency = notes_to_frequencies[note]
        duration = random.choice(note_duration_options)
        note_segment = Sine(frequency).to_audio_segment(duration=duration)
        melody += note_segment
        total_duration += duration

    # Export the melody to a WAV file
    output_filename = f"{bpm}bpm_{root_note}_{mode}.wav"
    melody.export(output_filename, format="wav")

    # Show a success message
    output_label.config(text=f"{output_filename} generated successfully!")
    
    

########################################################################################################################
#   ______   __    __  ______        ________  __        ________  __       __  ________  __    __  ________  ______   #
#  /      \ /  |  /  |/      |      /        |/  |      /        |/  \     /  |/        |/  \  /  |/        |/      \  #
# /$$$$$$  |$$ |  $$ |$$$$$$/       $$$$$$$$/ $$ |      $$$$$$$$/ $$  \   /$$ |$$$$$$$$/ $$  \ $$ |$$$$$$$$//$$$$$$  | #
# $$ | _$$/ $$ |  $$ |  $$ |        $$ |__    $$ |      $$ |__    $$$  \ /$$$ |$$ |__    $$$  \$$ |   $$ |  $$ \__$$/  #
# $$ |/    |$$ |  $$ |  $$ |        $$    |   $$ |      $$    |   $$$$  /$$$$ |$$    |   $$$$  $$ |   $$ |  $$      \  #
# $$ |$$$$ |$$ |  $$ |  $$ |        $$$$$/    $$ |      $$$$$/    $$ $$ $$/$$ |$$$$$/    $$ $$ $$ |   $$ |   $$$$$$  | #
# $$ \__$$ |$$ \__$$ | _$$ |_       $$ |_____ $$ |_____ $$ |_____ $$ |$$$/ $$ |$$ |_____ $$ |$$$$ |   $$ |  /  \__$$ | #
# $$    $$/ $$    $$/ / $$   |      $$       |$$       |$$       |$$ | $/  $$ |$$       |$$ | $$$ |   $$ |  $$    $$/  #
#  $$$$$$/   $$$$$$/  $$$$$$/       $$$$$$$$/ $$$$$$$$/ $$$$$$$$/ $$/      $$/ $$$$$$$$/ $$/   $$/    $$/    $$$$$$/   #
#                                                                                                                      #
########################################################################################################################

# Create the main Tkinter window
root = tk.Tk()
root.title("RandMusicGen")
root.geometry("330x220")

# BPM Selector
bpm_label = ttk.Label(root, text="BPM:")
bpm_label.pack()
bpm_var = tk.StringVar(value="120")
bpm_entry = ttk.Entry(root, textvariable=bpm_var)
bpm_entry.pack()

# Music Note Selector
note_label = ttk.Label(root, text="Note:")
note_label.pack()
note_var = tk.StringVar(value="C")
note_combo = ttk.Combobox(root, textvariable=note_var, values=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"])
note_combo.pack()

# Music Mode Selector
mode_label = ttk.Label(root, text="Mode:")
mode_label.pack()
mode_var = tk.StringVar(value="ionian (major)")
mode_combo = ttk.Combobox(root, textvariable=mode_var, values=[
    "ionian (major)", 
    "aeolian (minor)", 
    "phrygian", 
    "lydian", 
    "mixolydian", 
    "dorian", 
    "locrian", 
    "major pentatonic", 
    "minor pentatonic", 
    "blues", 
    "harmonic minor", 
    "melodic minor asc"
    ])

mode_combo.pack()

# Audio Sample Length
length_label = ttk.Label(root, text="Length (seconds):")
length_label.pack()
length_var = tk.StringVar(value="12")
length_entry = ttk.Entry(root, textvariable=length_var)
length_entry.pack()

# Generate Button
generate_button = ttk.Button(root, text="Generate Melody", command=generate_music)
generate_button.pack()

# Output Label
output_label = ttk.Label(root, text="")
output_label.pack()



#####################################################################################
#  __       __   ______   ______  __    __  __         ______    ______   _______   #
# /  \     /  | /      \ /      |/  \  /  |/  |       /      \  /      \ /       \  #
# $$  \   /$$ |/$$$$$$  |$$$$$$/ $$  \ $$ |$$ |      /$$$$$$  |/$$$$$$  |$$$$$$$  | #
# $$$  \ /$$$ |$$ |__$$ |  $$ |  $$$  \$$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |__$$ | #
# $$$$  /$$$$ |$$    $$ |  $$ |  $$$$  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$    $$/  #
# $$ $$ $$/$$ |$$$$$$$$ |  $$ |  $$ $$ $$ |$$ |      $$ |  $$ |$$ |  $$ |$$$$$$$/   #
# $$ |$$$/ $$ |$$ |  $$ | _$$ |_ $$ |$$$$ |$$ |_____ $$ \__$$ |$$ \__$$ |$$ |       #
# $$ | $/  $$ |$$ |  $$ |/ $$   |$$ | $$$ |$$       |$$    $$/ $$    $$/ $$ |       #
# $$/      $$/ $$/   $$/ $$$$$$/ $$/   $$/ $$$$$$$$/  $$$$$$/   $$$$$$/  $$/        #
#                                                                                   #
#####################################################################################
# Start the Tkinter event loop
root.mainloop()
