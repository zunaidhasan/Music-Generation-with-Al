from keras.models import Sequential
from keras.layers import LSTM, Dense, Embedding

def create_model(vocab_size, max_sequence_length):
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=256, input_length=max_sequence_length))
    model.add(LSTM(256, return_sequences=True))
    model.add(LSTM(256))
    model.add(Dense(vocab_size, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model
