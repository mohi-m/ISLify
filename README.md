# ISLify
**ISLify is an application that serves as an Indian Sign Language (ISL) Interpreter Assistant. It bridges the communication gap between spoken language and Indian Sign Language by converting speech to ISL gestures and alphabets.**

## Features
- Real-time speech recognition
- Conversion of recognized speech to ISL gestures (GIFs)
- Display of ISL alphabet images for unrecognized words
- User-friendly graphical interface

## Project Structure
```text
ISLify/
├── resources/
│   ├── isl_gifs/
│   │   └── [ISL gesture GIF files]
│   ├── letters/
│   │   └── [Alphabet image files]
│   ├── signlang.png
│   └── supported_phrases.json
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
│   └── utils.py
│
└── README.md

```

## Installation
1. Clone the repository:
`git clone https://github.com/yourusername/islify.git`

2. Navigate to the project directory:
`cd islify`

3. Install the required dependencies:
`pip install -r requirements.txt`

## Usage
1. Run the main script to start the application:
`python main.py`

2. Follow the on-screen instructions to use the speech recognition feature and view the corresponding ISL gestures or alphabet images.

## Dependencies
- speech_recognition
- numpy
- easygui
- Pillow
- tkinter

## Contributing
Contributions to ISLify are welcome! Please feel free to submit a Pull Request.