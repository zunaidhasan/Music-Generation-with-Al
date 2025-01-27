import numpy as np
from keras.models import load_model
from midi_utils import create_midi_file

def generate_music(model, start_seed, num_notes=100):
    generated = start_seed
    for _ in range(num_notes):
        input_sequence = np.array(generated[-50:]).reshape(1, 50)
        predicted = model.predict(input_sequence, verbose=0)
        next_note = np.argmax(predicted)
        generated.append(next_note)
    return generated

if __name__ == "__main__":
    model = load_model('music_model.h5')
    start_seed = [60, 62, 64]  # Example seed (MIDI note values)
    generated_notes = generate_music(model, start_seed)
    create_midi_file(generated_notes, 'generated_music.mid')
