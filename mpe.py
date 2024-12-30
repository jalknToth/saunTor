import pretty_midi
import subprocess  # For command-line interaction

# Create a PrettyMIDI object
midi_data = pretty_midi.PrettyMIDI()
instrument_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=instrument_program)

# Create a longer melody (example, you can modify this)
notes = []
current_time = 0
for i in range(30):  # Create 30 notes
    pitch = 60 + i % 12  # C4 to B4
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=current_time, end=current_time + 0.5)
    notes.append(note)
    current_time += 0.5

piano.notes.extend(notes)
midi_data.instruments.append(piano)
midi_data.write('sounds/melody.mid')

# Synthesize MIDI to WAV using Timidity
try:
    subprocess.run(['timidity', 'sounds/melody.mid', '-Ow', '-o', 'sounds/melody.wav'], check=True)
    print("MIDI synthesized to WAV.")

    # Convert WAV to MP3 using FFmpeg (optional)
    try:
        subprocess.run(['ffmpeg', '-i', 'sounds/melody.wav', 'sounds/melody.mp3'], check=True)
        print("WAV converted to MP3.")
    except FileNotFoundError:
        print("FFmpeg not found. WAV file created, but MP3 conversion failed.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting WAV to MP3: {e}")


except FileNotFoundError:
    print("Timidity++ not found. MIDI file created, but synthesis failed.")  # More informative message
except subprocess.CalledProcessError as e:
    print(f"Error during MIDI synthesis: {e}")