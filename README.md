# SignBridge

**SignBridge is an application that serves as an Indian Sign Language (ISL) and American Sign Language (ASL) Interpreter Assistant.
It bridges the communication gap between spoken language and Indian Sign Language by converting speech to ISL gestures and alphabets.**

## Features

- Real-time speech recognition
- Conversion of recognized speech to ISL/ASL gestures (GIFs)
- Display of alphabet images sign for unrecognized words
- User-friendly graphical interface

## Demo

- SignBridge > demo > [SignBridge.mp4](demo/SignBridge.mp4)

- Watch Demo on [YouTube](https://www.youtube.com/watch?v=FtxN6E09L_Y)

## Project Structure

```text
SignBridge/
├── resources/
│   ├── isl_gifs/
│   │   └── [ISL gesture GIF files]
│   ├── asl_gifs/
│   │   └── [ASL gesture GIF files]
│   ├── letters/
│   │   └── [Alphabet image files]
│   ├── signlang.png
│   ├── supported_isl_phrases.json
│   └── supported_asl_phrases.json
│
├── src/
│   ├── interface/
│   │   └── gui.py
│   │
│   ├── processor/
│   │   ├── image_processor.py
│   │   └── speech_processor.py
│   │
│   ├── main.py
│   └── my_utils.py
│
└── README.md

```

## Installation

1. Clone the repository:
   `git clone https://github.com/mohi-m/SignBridge.git`

2. Navigate to the project directory:
   `cd SignBridge`

3. Install the required dependencies:
   `pip install -r requirements.txt`

## Usage

1. Run the main script to start the application:
   `python main.py`

2. Follow the on-screen instructions to use the speech recognition feature and view the corresponding ISL/ASL gestures or alphabet images.

## Dependencies

- speech_recognition
- numpy
- easygui
- Pillow
- tkinter

## Contributing

Contributions to SignBridge are welcome! Please feel free to submit a Pull Request.
