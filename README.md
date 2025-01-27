# AI-Powered Music Generation Tool

This project leverages deep learning techniques to create an AI model that generates original music compositions based on a dataset comprised of MIDI files. We utilize a Recurrent Neural Network (RNN) architecture to learn musical patterns and compositions.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Generating Music](#generating-music)
- [Data Processing](#data-processing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Overview

This project aims to generate original music using deep learning techniques. The model is trained on a dataset of MIDI files, learning the structure, patterns, and notes to create new musical compositions. The generated music is output as MIDI files, which can be played back using any standard MIDI player or software.

## Requirements

To run this project, you will need the following packages:

- Python 3.x
- TensorFlow (includes Keras)
- NumPy
- music21
- MIDIUtil

## Project Structure

```
codealpha_tasks/
│
├── dataset/                  # Folder for storing MIDI files
│   ├── your_midi_file1.mid
│   ├── your_midi_file2.mid
│   └── ...
│
├── train_model.py            # Script to train the model
├── generate_music.py         # Script to generate music
├── midi_utils.py             # Utilities for MIDI processing
├── models.py                 # Model architecture definitions
├── config.py                 # Configuration settings
├── README.md                 # Project description and instructions
└── requirements.txt          # Required Python packages
```

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/codealpha_tasks.git
   cd codealpha_tasks
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On MacOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install Required Packages**:
   Use the following command to install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Your Dataset**:
   Place your MIDI files in the `dataset/` directory. Make sure the files are in the `.mid` format.

## Usage

### Training the Model

1. **Preprocess the Data**:
   Before training, you need to convert the MIDI files into a usable format. Run the following command:
   ```bash
   python prepare_data.py
   ```
   This script will create `notes_sequences.npy` and `processed_data.npy` files.

2. **Train the Model**:
   Run the model training script:
   ```bash
   python train_model.py
   ```
   This will train the model on the dataset and save the trained model as `music_model.h5`.

### Generating Music

Once the model has been trained, you can generate new music by running:
```bash
python generate_music.py
```
The generated music will be saved as `generated_music.mid`.

## Data Processing

- **MIDI Processing**: The `midi_utils.py` file contains methods for converting MIDI files to note sequences and vice versa, essential for the model's input and output.

- **Note Encoding**: The project includes functionality to encode musical notes into integer forms suitable for deep learning training.

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements, or if you fixed a bug or added features, please submit a pull request or open an issue.

1. Fork the project.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- **OpenAI**: For developing the technology that powers this project.
- **music21**: For providing a robust toolkit for music analysis and manipulation.
- **MIDIUtil**: For simplifying the MIDI file creation process.

--- 
Author,</br>
Zunaid Hasan</br>
hasan15-6033@diu.edu.bd
