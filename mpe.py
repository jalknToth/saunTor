import pretty_midi
import subprocess  # For command-line interaction

# Create a PrettyMIDI object (same as before)
midi_data = pretty_midi.PrettyMIDI()
instrument_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=instrument_program)
notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=0, end=0.5),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=0.5, end=1.0), # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.0, end=1.5), # E4
]
piano.notes.extend(notes)
midi_data.instruments.append(piano)
midi_data.write('sounds/melody.mid')


# Use Timidity to synthesize MIDI to WAV
try:
    # The -Ow flag tells Timidity to output a WAV file.  Adjust as needed.
    # The -o option specifies the output file.
    subprocess.run(['timidity', 'sounds/melody.mid', '-Ow', '-o', 'sounds/melody.wav'], check=True) 

    # Convert WAV to MP3 using FFmpeg
    try:
        subprocess.run(['ffmpeg', '-i', 'sounds/melody.wav', 'sounds/melody.mp3'], check=True)
        print("MIDI and MP3 files created!")
    except FileNotFoundError:
        print("FFmpeg not found. WAV file created, but MP3 conversion requires FFmpeg.")
        print("Install FFmpeg (e.g., 'sudo apt-get install ffmpeg' on Debian/Ubuntu).")
    except subprocess.CalledProcessError as e:
        print(f"Error converting WAV to MP3 using FFmpeg: {e}")

except FileNotFoundError:
    print("Timidity not found.  MIDI file created, but audio conversion requires Timidity++.")
    print("Install Timidity++ (e.g., 'sudo apt-get install timidity' on Debian/Ubuntu).")
except subprocess.CalledProcessError as e:
    print(f"Error synthesizing MIDI with Timidity: {e}")