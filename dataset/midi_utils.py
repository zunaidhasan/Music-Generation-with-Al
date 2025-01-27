import music21
from midiutil import MIDIFile

def midi_to_notes(midi_file):
    notes = []
    midi = music21.converter.parse(midi_file)
    for element in midi.flat.notes:
        if isinstance(element, music21.note.Note):
            notes.append(str(element.pitch))  # could convert to MIDI number here if needed
    return notes

def create_midi_file(notes, filename):
    midi = MIDIFile(1)
    track = 0
    time = 0

    midi.addTrackName(track, time, "Generated Music")
    midi.addTempo(track, time, 60)

    for note in notes:
        midi.addNote(track, 0, int(note), time, 1, 100)  # Ensure notes are in int format
        time += 1

    with open(filename, "wb") as f:
        midi.writeFile(f)
